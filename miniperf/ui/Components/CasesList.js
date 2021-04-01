import React, {useEffect, useState} from "react";
import {
    CircularProgress,
    Dialog,
    DialogContent,
    DialogTitle as MuiDialogTitle, 
    IconButton,
    Button,
    Typography,
    LinearProgress,
    List, ListItem, ListItemSecondaryAction,
    ListItemText
} from "@material-ui/core";
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {useInterval} from "../Util/Util";
import {PlayCircleFilled, Publish} from "@material-ui/icons";

const useStyle = makeStyles((theme)=>({
    '@global': {
        '.MuiButton-startIcon.MuiButton-iconSizeSmall': {
            marginRight: 3,
        }
    },
    root: {
        width: '100%',
    },
    listContent:{
        width:'360px',
        maxHeight: 480,
    },
    dialogTitle: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        paddingBottom: 5
    },
    addBtn: {
        '&: hover': {
            background: '#424242'
        }
    }
}))

export default function CaseList(props){
    const classes = useStyle()
    const { onClose, open, load, isRunning, isRecording, ShowMsg} = props;
    const [casesList,setCasesList] = useState([])

    const getCases = () =>{
        window.pywebview.api.loadCasesList().then((res)=>{
            if(res['ok']){
                setCasesList(res['msg'])
            }
        })
    }
    // 添加脚本
    const addFile = () =>{
        window.pywebview.api.addFile().then((res)=>{
            if(res){
                ShowMsg(res['msg'],res['ok'])
                getCases()
            }else{
                // showMsg("已取消添加脚本")
            }
        })
    }

    useEffect(()=>{
        if(open){
            getCases()
        }
    },[open])

    const DialogTitle = withStyles(useStyle)((props) => {
        const { children, classes, ...other } = props;
        return (
            <MuiDialogTitle disableTypography {...other}>
            <Typography variant="h6">{children}</Typography>
                <Button size="small" style={{backgroundColor: '#424242'}} startIcon={<i className="iconfont">&#xe60d;</i>} title={'添加案例'} onClick={addFile} disabled={isRecording || isRunning}>
                    添加案例
                </Button>
            </MuiDialogTitle>
        );
    });

    return(
        <Dialog open={open} onClose={onClose} className={classes.root}>
            <DialogTitle id="simple-dialog-title" className={classes.dialogTitle}>
                案例列表
            </DialogTitle>
            <DialogContent className={classes.listContent}>
                <List component="nav" aria-label="secondary mailbox folders">

                    {casesList.map((v,i)=>(

                    <ListItem button>
                        <ListItemText primary={v.tag + '(' + v.run_case + '.py)'} />
                        <ListItemSecondaryAction>
                            <IconButton edge="end" aria-label="Publish" title={'加载'} onClick={(e)=>{load(v.run_case)}} id={v.run_case}>
                                <Publish/>
                            </IconButton>
                        </ListItemSecondaryAction>
                    </ListItem>

                    ))}

                    {/*<ListItem button>*/}
                    {/*    <ListItemText primary="Trash" />*/}
                    {/*    <ListItemSecondaryAction>*/}
                    {/*        <IconButton edge="end" aria-label="delete">*/}
                    {/*            <PlayCircleFilled/>*/}
                    {/*        </IconButton>*/}
                    {/*    </ListItemSecondaryAction>*/}
                    {/*</ListItem>*/}

                </List>
            </DialogContent>
        </Dialog>
    )
}