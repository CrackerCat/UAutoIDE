import React, {useEffect, useRef, useState} from "react";
import {
    Button,
    Card,
    CardContent,
    CardHeader,
    CircularProgress, Dialog, DialogContent, DialogTitle,
    IconButton, Input, InputAdornment,
    makeStyles,
    TextareaAutosize, TextField, Toolbar
} from "@material-ui/core";
import {
    Adb, AddCircle,
    Backup,
    GetApp,
    MissedVideoCall, OpenInBrowser,
    PauseCircleFilled, PlayCircleFilled,
    RotateLeft,
    Save,
    SendOutlined, Settings,
    Stop
} from "@material-ui/icons";
import AceEditor from "react-ace";
import 'brace/mode/python'
import 'brace/theme/pastel_on_dark'

import {useInterval,useUpdate} from "../Util/Util"
import CaseList from "./CasesList";

const useStyles = makeStyles((theme) => ({
    root: {
        width : '100%',
        height: '100%',
        // background:'lightgrey'
    },
    content:{
        height: '90%',
        position:'relative',
        padding:0,
    },
    hightLight:{
        color:'red'
    },
    textArea:{
        height: '100% !important',
        width: '100% !important',
        position:'relative',
        padding:0
    },
    recoverContent:{
        position: 'absolute',
        top:0,
        left:0,
        right:0,
        bottom:0,
        background:'lightgrey',
        opacity: 0.5,
        'z-index':5
    },
    recoverProgress: {
        color: 'red',
        position: 'absolute',
        top: '50%',
        left: '50%',
        marginTop: -12,
        marginLeft: -12,
        'z-index':6
    },
    upload: {
        display: 'none',
    }
}));


export default function EditorCard (props) {
    const {ShowMsg,isConnected,tutorials,setTutorialsMode,changeADV} = props
    const [scriptsData,setScriptsData] = React.useState('')
    const [isRecording,setIsRecording] = React.useState(false)
    const [isRunning,setIsRunning] = React.useState(false)
    const [needSave,setNeedSave] = React.useState(false)
    const [isPausing,setIsPausing] = React.useState(false)
    const [casesWindowOpen,setCasesWindowOpen] = useState(false)//案例文件弹窗
    const [caseName,setCaseName] = useState('')//当前案例名称
    const [createWindowOpen,setCreateWindowOpen] = useState(false)//创建案例文件弹窗

    const [createCaseName,setCreateCaseName] = useState('')//创建案例文件案例名
    const [createCaseFileName,setCreateCaseFileName] = useState('')//创建案例文件文件名

    const [settingWindowOpen,setSettingWindowOpen] = useState(false)//设置弹窗
    const [workSpacePath,setWorkSpacePath] = useState('')//设置案例工作区路径

    const classes = useStyles()

    useInterval(()=>{
        //更新脚本信息
        if(isRecording)
        {
            window.pywebview.api.updateScripts({'caseName':caseName}).then((res)=>{
                setScriptsData(res['msg'])
            })
        }
    },1000)

    useEffect(()=>{
        if(!isConnected){
            init()
        }
        else{
            if(tutorials){
                window.pywebview.api.getDemoScripts().then((res)=>{
                    setScriptsData(res['msg'])
                })
            }
            else{
                window.pywebview.api.updateScripts({'caseName':caseName}).then((res)=>{
                    setScriptsData(res['msg'])
                })
            }
        }
    },[isConnected])


    let init = function (){
        // setScriptsData('')
        setIsRecording(false)
        setIsRunning(false)
        setCaseName('')
    }
    //案例文件弹窗关闭事件
    let handleCloseCases = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCasesWindowOpen(false);
    };
    //创建案例文件弹窗关闭事件
    let handleCloseCreate = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCreateWindowOpen(false);
    };
    //设置弹窗关闭事件
    let handleCloseSetting = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setWorkSpacePath('')
        setSettingWindowOpen(false);
    };

    let setWorkSpace = (v) => {
        if(workSpacePath === '')
            return
        window.pywebview.api.setWorkSpace({'path':workSpacePath}).then((res)=>{
            if(res['ok']){
                setWorkSpacePath('')
                handleCloseSetting('','')
                setCaseName('')
                setScriptsData('')
                ShowMsg(res['msg'],res['ok'])
            }else{
                ShowMsg(res['msg'],res['ok'])
            }
        })
    }

    let createFile = (v) => {
        if(createCaseFileName === '' || createCaseName === '')
            return
        window.pywebview.api.createCase({'name':createCaseFileName,'caseName':createCaseName}).then((res)=>{
            if(res['ok']){
                setCreateCaseName('')
                setCreateCaseFileName('')
                handleCloseCreate('','')
                setCaseName(res['msg'])
                setScriptsData('')
            }else{
                setCreateCaseName('')
                setCreateCaseFileName('')
                handleCloseCreate('','')
                ShowMsg(res['msg'],res['ok'])
            }
        })
    }


    function record(){
        setIsRecording(true)
        ShowMsg('开始录制，长按屏幕5秒结束录制')
        window.pywebview.api.record({'caseName': caseName}).then((res)=>{
            ShowMsg(res['msg'])
            setIsRecording(false)
            setNeedSave(false)
        })
    }

    function runCase(){
        setIsRunning(true)
        ShowMsg('开始运行')
        window.pywebview.api.runCase({'fileInfo':scriptsData,'caseName':caseName}).then((res)=>{
            ShowMsg(res['msg'],res['ok'])
            setIsRunning(false)
            setNeedSave(false)
            if(tutorials){
                setTutorialsMode(false)
            }

        })
    }
    function saveAs() {

        const element = document.createElement("a");

        const file = new Blob([scriptsData], {type: 'text/plain'});

        element.href = URL.createObjectURL(file);

        element.download = "code.py";

        document.body.appendChild(element); // Required for this to work in FireFox

        element.click();

    }
    function save(){
        // ShowMsg(scriptsData)
        window.pywebview.api.saveTempFile({'fileInfo':scriptsData}).then((res)=>{
            ShowMsg(res['msg'])
            setNeedSave(false)
        })
    }
    //暂停案例运行
    const pause = () =>{
        window.pywebview.api.pause().then((res)=>{
            ShowMsg(res['msg'])
            setIsPausing(true)
        })
    }
    //继续脚本运行
    const continuePlay = ()=>{
        window.pywebview.api.continuePlay().then((res)=>{
            ShowMsg(res['msg'])
            setIsPausing(false)
        })
    }
    //通过vs code打开
    const openInVS = () =>{
        window.pywebview.api.openInVS().then((res)=>{
            ShowMsg(res['msg'],res['ok'])
        })
    }

    const changeHandle = (e) =>{
        setScriptsData(e)
        setNeedSave(true)
    }
    let upload = function (v){
        window.pywebview.api.loadCase({'caseName':v}).then((res)=>{
            setCaseName(v)
            ShowMsg(v,res['ok'])
            setIsPausing(false)
            setScriptsData(res['msg'])
            handleCloseCases('','')
        })
    }
    return (
        <Card variant={'outlined'} className={classes.root}>
            <CardHeader title={'Coding'} action={[
                <span>当前文件：{caseName}</span>,
                <IconButton aria-label="settings" title={'录制'} onClick={record} disabled={isRecording || isRunning || !isConnected || tutorials}>
                    <MissedVideoCall/>
                </IconButton>,
                <IconButton aria-label="settings" title={'运行'} onClick={runCase} disabled={isRecording || isRunning || !isConnected}>
                    <SendOutlined/>
                </IconButton>,
                <IconButton aria-label="settings" title={'选择脚本'} onClick={()=>{setCasesWindowOpen(true)}} disabled={isRecording || isRunning || tutorials}>
                    <Backup/>
                </IconButton>,
                // <IconButton aria-label="settings" title={'保存'} onClick={save} disabled={isRecording || isRunning || !isConnected || tutorials} className={needSave?classes.hightLight:''}>
                //     <Save/>
                // </IconButton>,
                <IconButton aria-label="settings" title={'通过VS CODE打开工作区'} onClick={()=>{openInVS()}} disabled={isRecording || isRunning}>
                    <OpenInBrowser/>
                </IconButton>,
                <IconButton aria-label="settings" title={'继续'} onClick={continuePlay} disabled={isRecording || !isConnected || !isRunning || !isPausing}>
                    <PlayCircleFilled/>
                </IconButton>,
                <IconButton aria-label="settings" title={'暂停'} onClick={pause} disabled={isRecording || !isConnected || !isRunning || isPausing}>
                    <PauseCircleFilled/>
                </IconButton>,
                <IconButton aria-label="settings" title={'导出脚本'} onClick={saveAs} disabled={isRecording || isRunning || tutorials}>
                    <GetApp/>
                </IconButton>,
                <IconButton aria-label="settings" title={'新建脚本'} onClick={()=>{setCreateWindowOpen(true)}} disabled={isRecording || isRunning || tutorials}>
                    <AddCircle/>
                </IconButton>,
                <IconButton aria-label="settings" title={'设置'} onClick={()=>{setSettingWindowOpen(true)}} disabled={isConnected}>
                    <Settings/>
                </IconButton>
                //disabled={isRecording || !isConnected || tutorials}
                // <IconButton aria-label="settings" title={'重置'} disabled={isRecording || !isConnected || true}>
                //     <RotateLeft/>
                // </IconButton>
            ]}/>
            {/*创建新案例窗口*/}
            <Dialog open={createWindowOpen}>
                <DialogTitle>新建案例</DialogTitle>
                <DialogContent>
                        <TextField id="outlined-basic" label="案例名称" variant="outlined" value={createCaseName}
                                   onChange={(e)=>{setCreateCaseName(e.target.value)}}
                        />
                        <TextField id="outlined-basic" label="案例文件名" variant="outlined" value={createCaseFileName}
                                   onChange={(e)=>{setCreateCaseFileName(e.target.value)}}
                        />
                        <br/>
                        <Button variant="contained" color="primary"
                                onClick={(e)=>{
                                    createFile(e)
                            }}
                        >
                            创建
                        </Button>
                        <Button variant="contained" color="secondary" onClick={(e)=>{handleCloseCreate('','')}}>
                            取消
                        </Button>
                </DialogContent>
            </Dialog>
            <Dialog open={settingWindowOpen} onClose={handleCloseSetting}>
                <DialogTitle>设置</DialogTitle>
                <DialogContent>
                    <TextField id="outlined-basic" label="工作区路径" variant="outlined" value={workSpacePath}
                               onChange={(e)=>{setWorkSpacePath(e.target.value)}}
                    />
                    <br/>
                    <Button variant="contained" color="primary"
                            onClick={(e)=>{
                                setWorkSpace(e)
                            }}
                    >
                        设置或创建
                    </Button>
                    <Button variant="contained" color="secondary" onClick={(e)=>{handleCloseSetting('','')}}>
                        取消
                    </Button>
                </DialogContent>
            </Dialog>
            <CardContent className={classes.content}>
                <AceEditor
                    mode="python"
                    theme="pastel_on_dark"
                    name="UNIQUE_ID_OF_DIV"
                    editorProps={{ $blockScrolling: true }}
                    className={classes.textArea}
                    value={scriptsData}
                    onChange={changeHandle}
                />
                {isRecording &&
                <div className={classes.recoverContent}>
                    <CircularProgress size={24} className={classes.recoverProgress}/>
                </div>
                }
            </CardContent>
            <CaseList
                open={casesWindowOpen}
                onClose={handleCloseCases}
                load={upload}
            />
        </Card>

    )
}