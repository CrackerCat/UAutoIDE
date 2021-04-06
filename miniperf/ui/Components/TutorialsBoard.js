import React, {useEffect, useState} from "react";
import {CircularProgress, Dialog, DialogContent, DialogTitle, LinearProgress, Typography, IconButton} from "@material-ui/core";
import { DoneOutline, Close } from '@material-ui/icons'
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {useInterval} from "../Util/Util";
import HighlightOffIcon from '@material-ui/icons/HighlightOff';

const useStyle = makeStyles((theme)=>({
    root: {
        '& > *': {
            margin: theme.spacing(1),
            'text-align':'center'
        },
    },
    Finish:{
        color:'green'
    },
    tutorialInfo: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    dialogContent: {
        paddingBottom: 40
    },
    close: {
        left:200
    }
}))
const styles = (theme) => ({
    root: {
        margin: 0,
        padding: theme.spacing(2),
    },
    closeButton: {
    position: 'absolute',
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
    },
})
const MuiDialogTitle = withStyles(styles)((props) => {
    const { children, classes, onClose, ...other } = props;
    return (
        <DialogTitle disableTypography className={classes.root} {...other}>
        <Typography variant="h6">{children}</Typography>
        {onClose ? (
            <IconButton aria-label="close" className={classes.closeButton} onClick={onClose}>
            <Close />
            </IconButton>
        ) : null}
        </DialogTitle>
    );
});

export default function TutorialsBoard(props){
    const classes = useStyle()
    const { onClose, open ,isConnected,loading,connect,phoneList,showMsg,userOnClose} = props;
    const [isOpenDemo,setIsOpenDemo] = useState(false)
    const [opening,setOpening] = useState(false)
    const [progress,setProgress] = useState(0)
    useInterval(()=>{
        if(!open){
            return
        }
        if(!isOpenDemo&&!opening){
            setOpening(true)
            window.pywebview.api.openDemo().then((res)=>{
                showMsg(res['msg'])
                setIsOpenDemo(true)
                setProgress(33)
            })
        }
        if(isOpenDemo){
            if(!isConnected && !loading){
                if(phoneList.length === 1){
                    connect('',phoneList[0]['sn'],phoneList[0]['name'])
                }
            }
        }

    },5000)

    useEffect(()=>{
        if(open){
            setIsOpenDemo(false)
            setOpening(false)
            setProgress(0)
        }
    },[open])
    useEffect(()=>{
        if(isConnected){
            setProgress(66)
            setTimeout(()=>{
                setProgress(100)
                onClose('','')
            },1000)
        }
    },[isConnected])

    return(
        <Dialog open={open} className={classes.root}>
            <MuiDialogTitle id="simple-dialog-title" onClose={() => onClose('', '')}>演示脚本</MuiDialogTitle>
            <DialogContent className={classes.dialogContent}>
                <p style={{fontSize: 14}} className={isOpenDemo?classes.Finish:''}>正在打开演示Demo，如未安装将自动安装（请确保有且仅有1台设备连接于电脑）</p>

                <div className={classes.tutorialInfo}>
                    <p>1.检测设备</p>
                    {progress < 33 && <CircularProgress size={24} style={{color: '#fff'}} />}
                    {progress >= 33 && <DoneOutline size={24} style={{color: '#4F7038'}}/>}
                </div>
                <div className={classes.tutorialInfo}>
                    <p>2.连接设备</p>
                    {!isConnected && <CircularProgress size={24} style={{color: '#fff'}} />}
                    {isConnected && <DoneOutline size={24} style={{color: '#4F7038'}} />}
                </div>
                <div className={classes.tutorialInfo}>
                    <p>3.运行脚本</p>
                    {!isConnected && <CircularProgress size={24} style={{color: '#fff'}} />}
                    {isConnected && isOpenDemo && <DoneOutline size={24} style={{color: '#4F7038'}} />}
                </div>
                {/* <LinearProgress variant="determinate" value={progress} /> */}
            </DialogContent>
        </Dialog>
    )
}