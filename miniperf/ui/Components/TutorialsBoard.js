import React, {useEffect, useState} from "react";
import {CircularProgress, Dialog, DialogContent, DialogTitle, LinearProgress,IconButton} from "@material-ui/core";
import {makeStyles} from "@material-ui/core/styles";
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
    close: {
        left:200
    }
}))

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
                    connect('',phoneList[0]['sn'],phoneList[0]['name'],false)
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
            <DialogTitle id="simple-dialog-title">
                演示案例
                <IconButton className={classes.close} onClick={()=>{userOnClose('','')}}>
                    <HighlightOffIcon/>
                </IconButton>
            </DialogTitle>
            <DialogContent>
                <p className={isOpenDemo?classes.Finish:''}>1.正在打开演示Demo，如未安装将自动安装（请确保有且仅有1台设备连接于电脑）</p>
                {!isOpenDemo && <p>检测中<CircularProgress size={24}/></p>}
                <p className={isConnected?classes.Finish:''}>2.连接中</p>
                {isOpenDemo && !isConnected && <p>检测中<CircularProgress size={24}/></p>}
                <p className={!open?classes.Finish:''}>3.运行案例</p>
                {isConnected && open && <p>检测中<CircularProgress size={24}/></p>}
                <LinearProgress variant="determinate" value={progress} />
            </DialogContent>
        </Dialog>
    )
}