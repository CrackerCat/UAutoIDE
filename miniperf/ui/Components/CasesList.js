import React, {useEffect, useState} from "react";
import {
    CircularProgress,
    Dialog,
    DialogContent,
    DialogTitle as MuiDialogTitle, 
    DialogActions,
    IconButton,
    Button,
    Typography,
    LinearProgress,
    List, ListItem, ListItemSecondaryAction,
    TextField,
    ListItemText
} from "@material-ui/core";
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {useInterval} from "../Util/Util";
import {PlayCircleFilled, Publish} from "@material-ui/icons";

const useStyle = makeStyles((theme)=>({
    '@global': {
        '.MuiButton-startIcon.MuiButton-iconSizeSmall': {
            marginRight: 3,
        },
        '.MuiListItemText-root .MuiTypography-root': {
            overflow: 'hidden',
            textOverflow: 'ellipsis',
            whiteSpace: 'nowrap',
        },
    },
    root: {
        width: '100%',
    },
    listContent:{
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
    },
    dialogContent: {
        overflow: 'hidden',
        display: 'flex',
        flexFlow: 'column',
        justifyContent: 'space-between',
        // alignItems: 'center'
    },
    notchedOutline: {},
    focused: {
        "& $notchedOutline": {
            borderColor: "#fff !important"
        }
    },
    dialogBtn: {
        backgroundColor: '#1890ff',
        color: '#fff',
        '&:hover': {
            backgroundColor: '#096dd9',
        },
        '&:nth-child(2n + 1)': {
            marginRight: '20px'
        }
    },
    dialogActions: {
        padding: 24
    },
}))

export default function CaseList(props){
    const classes = useStyle()
    const { 
        onClose, 
        open, 
        load, 
        isRunning, 
        isRecording, 
        ShowMsg,
        caseName,
        onChangeCaseName,
        scriptsData,
        onChangeScriptsData,
    } = props;
    const [casesList,setCasesList] = useState([])
    const [createWindowOpen,setCreateWindowOpen] = useState(false)//创建案例文件弹窗
    const [createCaseName,setCreateCaseName] = useState('')//创建案例文件案例名
    const [createCaseFileName,setCreateCaseFileName] = useState('')//创建案例文件文件名

    const getCases = () =>{
        window.pywebview.api.loadCasesList().then((res)=>{
            if(res['ok']){
                setCasesList(res['msg'])
            }
        })
    }
    // 导入脚本
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

    let createFile = (v) => {
        if(createCaseFileName === '' || createCaseName === '') {
            ShowMsg('脚本名称或脚本文件名不能为空', false)
            return
        }
            
        window.pywebview.api.createCase({'name':createCaseFileName,'caseName':createCaseName}).then((res)=>{
            if(res['ok']){
                setCreateCaseName('')
                setCreateCaseFileName('')
                handleCloseCreate('','')
                onChangeCaseName(res['msg'])
                onChangeScriptsData('')
                ShowMsg('脚本' + res['msg'] +'.py' + '创建成功')
                getCases()
            }else if(res['exist']) {
                setCreateCaseName('')
                setCreateCaseFileName('')
                ShowMsg(res['msg'],res['ok'])
            }else{
                setCreateCaseName('')
                setCreateCaseFileName('')
                handleCloseCreate('','')
                ShowMsg(res['msg'],res['ok'])
            }
        })
    }
    //创建案例文件弹窗关闭事件
    let handleCloseCreate = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCreateWindowOpen(false);
    };

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
                <div>
                    <Button size="small" style={{backgroundColor: '#424242', marginRight: 10}} startIcon={<i className="iconfont">&#xe61d;</i>} title={'新建脚本'} onClick={()=>{setCreateWindowOpen(true)}} disabled={isRecording || isRunning}>
                        新建脚本
                    </Button>
                    <Button size="small" style={{backgroundColor: '#424242'}} startIcon={<i className="iconfont">&#xe65d;</i>} title={'导入脚本'} onClick={addFile} disabled={isRecording || isRunning}>
                        导入脚本
                    </Button>
                </div>
                
            </MuiDialogTitle>
        );
    });

    return(
        <React.Fragment>
            <Dialog open={open} fullWidth={true} maxWidth="xs" onClose={onClose} className={classes.root}>
                <DialogTitle id="simple-dialog-title" className={classes.dialogTitle}>
                    脚本列表
                </DialogTitle>
                <DialogContent className={classes.listContent}>
                    <List component="nav" aria-label="secondary mailbox folders">

                        {casesList.map((v,i)=>(

                        <ListItem button>
                            <ListItemText primary={v.tag + '(' + v.run_case + '.py)'}/>
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
            <Dialog open={createWindowOpen} fullWidth={true} maxWidth="sm">
                <MuiDialogTitle>新建脚本</MuiDialogTitle>
                <DialogContent className={classes.dialogContent}>
                        <TextField 
                            style={{width: '100%', marginBottom: '20px'}} 
                            id="outlined-basic" 
                            label="脚本名称"
                            placeholder="请输入脚本名称"
                            variant="outlined" 
                            value={createCaseName}
                            InputProps={{
                                classes: {
                                    notchedOutline: classes.notchedOutline,
                                    focused: classes.focused
                                }
                            }}
                            onChange={(e)=>{setCreateCaseName(e.target.value)}}
                        />
                        <TextField 
                            style={{width: '100%'}}
                            id="outlined-basic" 
                            label="脚本文件名" 
                            placeholder="请输入脚本文件名(不需要加.py)"
                            variant="outlined" 
                            value={createCaseFileName}
                            InputProps={{
                                classes: {
                                    notchedOutline: classes.notchedOutline,
                                    focused: classes.focused
                                }
                            }}
                            onChange={(e)=>{setCreateCaseFileName(e.target.value)}}
                        />
                </DialogContent>
                <DialogActions classes={{root: classes.dialogActions}}>
                <Button variant="contained" classes={{root: classes.dialogBtn}} onClick={(e)=>{createFile(e)}}>
                    创建
                </Button>
                <Button variant="contained" color="primary" onClick={(e)=>{handleCloseCreate('','')}}>
                    取消
                </Button>
                </DialogActions>
            </Dialog>
        </React.Fragment>
    )
}