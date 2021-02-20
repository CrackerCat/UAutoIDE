import React, {useEffect, useRef} from "react";
import {
    Button,
    Card,
    CardContent,
    CardHeader,
    CircularProgress,
    IconButton,
    makeStyles,
    TextareaAutosize, Toolbar
} from "@material-ui/core";
import {
    Adb,
    Backup,
    GetApp,
    MissedVideoCall,
    PauseCircleFilled, PlayCircleFilled,
    RotateLeft,
    Save,
    SendOutlined,
    Stop
} from "@material-ui/icons";
import AceEditor from "react-ace";
import 'brace/mode/python'
import 'brace/theme/pastel_on_dark'

import {useInterval,useUpdate} from "../Util/Util"

const useStyles = makeStyles((theme) => ({
    root: {
        width : '100%',
        height: '60%',
        // background:'lightgrey'
    },
    content:{
        height: '70%',
        position:'relative',
        flex:'1'
    },
    hightLight:{
        color:'red'
    },
    textArea:{
        height: '100% !important',
        width: '100% !important',
        position:'absolute',
        left:0,
        right:0,
        bottom:0,
        top:0
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
    const {ShowMsg,isConnected} = props
    const [scriptsData,setScriptsData] = React.useState('')
    const [isRecording,setIsRecording] = React.useState(false)
    const [isRunning,setIsRunning] = React.useState(false)
    const [needSave,setNeedSave] = React.useState(false)
    const [isPausing,setIsPausing] = React.useState(false)
    const classes = useStyles()

    useInterval(()=>{
        //更新脚本信息
        if(isRecording)
        {
            window.pywebview.api.updateScripts().then((res)=>{
                setScriptsData(res['msg'])
            })
        }
    },1000)
    // useUpdate(()=>{
    //     if(!isConnected){
    //         init()
    //     }
    //     else{
    //         window.pywebview.api.updateScripts().then((res)=>{
    //             setScriptsData(res['msg'])
    //
    //         })
    //     }
    // },isConnected)

    useEffect(()=>{
        if(!isConnected){
            init()
        }
        else{
            window.pywebview.api.updateScripts().then((res)=>{
                setScriptsData(res['msg'])
            })
        }
    },[isConnected])


    let init = function (){
        // setScriptsData('')
        setIsRecording(false)
        setIsRunning(false)
    }

    function record(){
        setIsRecording(true)
        ShowMsg('开始录制，长按屏幕5秒结束录制')
        window.pywebview.api.record().then((res)=>{
            ShowMsg(res['msg'])
            setIsRecording(false)
            setNeedSave(false)
        })
    }

    function runCase(){
        setIsRunning(true)
        ShowMsg('开始运行')
        window.pywebview.api.runCase().then((res)=>{
            ShowMsg(res['msg'])
            setIsRunning(false)
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

    const changeHandle = (e) =>{
        setScriptsData(e)
        setNeedSave(true)
    }
    const upload = function (e){
        const reader = new FileReader();
        reader.readAsText(e.target.files[0])
        reader.onload = function (e){
            setScriptsData(e.target.result)
            setNeedSave(true)
        }
    }
    return (
        <Card variant={'outlined'} className={classes.root}>
            <input
                id="contained-button-file"
                className={classes.upload}
                multiple
                type="file"
                onChange={upload}
                accept={'.py'}
            />
            <CardHeader title={'Coding'} action={[
                <IconButton aria-label="settings" title={'录制'} onClick={record} disabled={isRecording || isRunning || !isConnected}>
                    <MissedVideoCall/>
                </IconButton>,
                <IconButton aria-label="settings" title={'运行'} onClick={runCase} disabled={isRecording || isRunning || !isConnected}>
                    <SendOutlined/>
                </IconButton>,
                <IconButton aria-label="settings" title={'保存'} onClick={save} disabled={isRecording || isRunning || !isConnected} className={needSave?classes.hightLight:''}>
                    <Save/>
                </IconButton>,
                <IconButton aria-label="settings" title={'下载脚本'} onClick={saveAs} disabled={isRecording || isRunning}>
                    <GetApp/>
                </IconButton>,
                <IconButton aria-label="settings" title={'调试'} disabled={isRecording || !isConnected || true}>
                    <Adb/>
                </IconButton>,
                <IconButton aria-label="settings" title={'继续'} onClick={continuePlay} disabled={isRecording || !isConnected || !isRunning || !isPausing}>
                    <PlayCircleFilled/>
                </IconButton>,
                <IconButton aria-label="settings" title={'暂停'} onClick={pause} disabled={isRecording || !isConnected || !isRunning || isPausing}>
                    <PauseCircleFilled/>
                </IconButton>,
                <label htmlFor="contained-button-file">
                    <IconButton component={"span"} aria-label="settings" title={'上传'} disabled={isRecording || !isConnected}>
                        <Backup/>
                    </IconButton>
                    {/*<Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button}>test</Button>*/}
                </label>
                // <IconButton aria-label="settings" title={'重置'} disabled={isRecording || !isConnected || true}>
                //     <RotateLeft/>
                // </IconButton>
            ]}/>
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
        </Card>

    )
}