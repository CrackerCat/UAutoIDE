import React, {useEffect, useRef, useState} from "react";
import {
    Button,
    Card,
    CardContent,
    CardHeader,
    CardActions,
    CircularProgress, Dialog, DialogContent, DialogTitle,
    IconButton, Input, InputAdornment,
    makeStyles,
    withStyles,
    TextareaAutosize, TextField, Toolbar
} from "@material-ui/core";
import {
    Adb, AddCircle,
    Backup,
    GetApp,
    MissedVideoCall, OpenInBrowser,
    PauseCircleFilled, PlayCircleFilled,
    RotateLeft,
    SaveAlt,
    SendOutlined, Settings,
    Stop,
    PlayArrow, Pause, Code
} from "@material-ui/icons";
import CaseList from "./CasesList";
import AceEditor from "react-ace";
import "ace-builds/src-noconflict/mode-python";
import "ace-builds/src-noconflict/theme-pastel_on_dark";
import 'ace-builds/src-min-noconflict/ext-language_tools'
import 'ace-builds/src-min-noconflict/snippets/python'
import 'ace-builds/src-min-noconflict/ext-searchbox'
import 'ace-builds/src-min-noconflict/ext-emmet'
import 'ace-builds/src-min-noconflict/keybinding-vscode'

import {useInterval,useUpdate} from "../Util/Util"

const useStyles = makeStyles((theme) => ({
    '@global': {
        '.MuiButton-label': {
            height: 20
        }
    },
    root: {
        width : '100%',
        height: '100%',
        // background:'lightgrey',
    },
    content:{
        height: 'calc(100% - 32px)',
        position:'relative',
        flex:1,
        padding:0,
        '&:last-child': {
            paddingBottom: 0,
        }
    },
    hightLight:{
        color:'red'
    },
    textArea:{
        // 'height':'500px',
        // width: '100% !important',
        // position:'relative',
        // padding:0
        // position:'absolute',
        // left:0,
        // right:0,
        // bottom:0,
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
    },
    cardHeader: {
        maxHeight: 22,
        padding: '5px 5px 5px 24px',
        background: '#424242',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    cardHeaderTitle: {
        fontSize: 14,
        color: '#fff'
    },
    cardHeaderAction: {
        margin: 0,
    },
    MuiButtonRoot: {
        padding: 0,
    },
    MuiCardContentRoot: {
        padding: 0,
        '&:last-child': {
            paddingBottom: 0,
        }
    },
    '.ace_content': {
        overflow: 'auto'
    }
}));

const EditorBtn = withStyles({
    root: {
        padding: '0 5px',
    }
})(Button);

export default function EditorCard (props) {
    const {
        ShowMsg,
        isConnected,
        tutorials,
        setTutorialsMode,
        changeADV,
        isRecording,
        needSave,
        isRunning,
        caseName,
        scriptsData,
        isPausing,
        onChangeRecording,
        onChangeNeedSave,
        onChangeRunning,
        onChangeCaseName,
        onChangeScriptsData,
        onChangeIsPausing,
    } = props
    const [casesWindowOpen,setCasesWindowOpen] = useState(false)//案例文件弹窗
    const [runned, setRunned] = React.useState(false)

    const classes = useStyles()

    useInterval(()=>{
        //更新脚本信息
        if(isRecording)
        {
            window.pywebview.api.updateScripts({'caseName':caseName}).then((res)=>{
                onChangeScriptsData(res['msg'])
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
                    onChangeScriptsData(res['msg'])
                })
            }
            else{
                window.pywebview.api.updateScripts({'caseName':caseName}).then((res)=>{
                    onChangeScriptsData(res['msg'])
                })
            }
        }
    },[isConnected])


    let init = function (){
        // setScriptsData('')
        // setIsRecording(false)
        onChangeRecording(false)
        onChangeRunning(false)
        onChangeCaseName('')
        setRunned(false)
    }
    //案例文件弹窗关闭事件
    let handleCloseCases = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCasesWindowOpen(false);
    };
    //创建案例文件弹窗关闭事件
    // let handleCloseCreate = (event, reason) => {
    //     if (reason === 'clickaway') {
    //         return;
    //     }
    //     setCreateWindowOpen(false);
    // };
    //设置弹窗关闭事件
    // let handleCloseSetting = (event, reason) => {
    //     if (reason === 'clickaway') {
    //         return;
    //     }
    //     setWorkSpacePath('')
    //     setSettingWindowOpen(false);
    // };

    // let setWorkSpace = () => {
    //     window.pywebview.api.openUAUTOFile().then((res)=>{
    //         if(res){
    //             ShowMsg(res['msg'],res['ok'])
    //         }else{
    //             ShowMsg("已取消工作区打开")
    //         }
    //         handleCloseSetting('','')
    //     })
    // }

    // let createuserWorkSpace = (e) => {
    //     window.pywebview.api.createuserWorkSpace().then((res)=>{
    //         if(res){
    //             ShowMsg(res['msg'],res['ok'])
    //         }else{
    //             ShowMsg("已取消工作区创建")
    //         }
    //         handleCloseSetting('','')
    //     })
    // }

    // let createFile = (v) => {
    //     if(createCaseFileName === '' || createCaseName === '')
    //         return
    //     window.pywebview.api.createCase({'name':createCaseFileName,'caseName':createCaseName}).then((res)=>{
    //         if(res['ok']){
    //             setCreateCaseName('')
    //             setCreateCaseFileName('')
    //             handleCloseCreate('','')
    //             setCaseName(res['msg'])
    //             setScriptsData('')
    //         }else{
    //             setCreateCaseName('')
    //             setCreateCaseFileName('')
    //             handleCloseCreate('','')
    //             ShowMsg(res['msg'],res['ok'])
    //         }
    //     })
    // }


    function runCase(){
        onChangeRunning(true)
        setRunned(true)
        ShowMsg('开始运行')
        window.pywebview.api.runCase({'fileInfo':scriptsData,'caseName':caseName}).then((res)=>{
            ShowMsg(res['msg'],res['ok'])
            onChangeRunning(false)
            onChangeNeedSave(false)
            if(tutorials){
                setTutorialsMode(false)
            }
            setRunned(false)
        })
        // .then(() => {alert(`record: ${isRecording}  !connect:${!isConnected}  !run:${!isRunning}  !pause:${!isPausing}`)})
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
            onChangeNeedSave(false)
        })
    }

    //暂停案例运行
    const pause = () =>{
        window.pywebview.api.pause().then((res)=>{
            ShowMsg(res['msg'])
            onChangeIsPausing(true)
        })
    }

    //继续脚本运行
    const continuePlay = ()=>{
        window.pywebview.api.continuePlay().then((res)=>{
            ShowMsg(res['msg'])
            onChangeIsPausing(false)
        })
    }
    //通过vs code打开
    const openInVS = () =>{
        window.pywebview.api.openInVS().then((res)=>{
            ShowMsg(res['msg'],res['ok'])
        })
    }


    const changeHandle = (e) =>{
        onChangeScriptsData(e)
        onChangeNeedSave(true)
    }
    let upload = function (v){
        window.pywebview.api.loadCase({'caseName':v}).then((res)=>{
            onChangeCaseName(v)
            ShowMsg(v,res['ok'])
            onChangeIsPausing(false)
            onChangeScriptsData(res['msg'])
            handleCloseCases('','')
        })
    }
    return (
        // <Card variant={'outlined'} className={classes.root}>
        //     <CardHeader title={'Coding'} action={[
        //         <span>当前文件：{caseName}</span>,
        //         <IconButton aria-label="settings" title={'录制'} onClick={record} disabled={isRecording || isRunning || !isConnected || tutorials}>
        //             <MissedVideoCall/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'运行'} onClick={runCase} disabled={isRecording || isRunning || !isConnected}>
        //             <SendOutlined/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'选择脚本'} onClick={()=>{setCasesWindowOpen(true)}} disabled={isRecording || isRunning || tutorials}>
        //             <Backup/>
        //         </IconButton>,
        //         // <IconButton aria-label="settings" title={'保存'} onClick={save} disabled={isRecording || isRunning || !isConnected || tutorials} className={needSave?classes.hightLight:''}>
        //         //     <Save/>
        //         // </IconButton>,
        //         <IconButton aria-label="settings" title={'通过VS CODE打开工作区'} onClick={()=>{openInVS()}} disabled={isRecording || isRunning}>
        //             <OpenInBrowser/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'继续'} onClick={continuePlay} disabled={isRecording || !isConnected || !isRunning || !isPausing}>
        //             <PlayCircleFilled/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'暂停'} onClick={pause} disabled={isRecording || !isConnected || !isRunning || isPausing}>
        //             <PauseCircleFilled/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'导出脚本'} onClick={saveAs} disabled={isRecording || isRunning || tutorials}>
        //             <GetApp/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'新建脚本'} onClick={()=>{setCreateWindowOpen(true)}} disabled={isRecording || isRunning || tutorials}>
        //             <AddCircle/>
        //         </IconButton>,
        //         <IconButton aria-label="settings" title={'设置'} onClick={()=>{setSettingWindowOpen(true)}} disabled={isConnected}>
        //             <Settings/>
        //         </IconButton>
        //         //disabled={isRecording || !isConnected || tutorials}
        //         // <IconButton aria-label="settings" title={'重置'} disabled={isRecording || !isConnected || true}>
        //         //     <RotateLeft/>
        //         // </IconButton>
        //     ]}/>
        //     {/*创建新案例窗口*/}
        //     <Dialog open={createWindowOpen}>
        //         <DialogTitle>新建案例</DialogTitle>
        //         <DialogContent>
        //                 <TextField id="outlined-basic" label="案例名称" variant="outlined" value={createCaseName}
        //                            onChange={(e)=>{setCreateCaseName(e.target.value)}}
        //                 />
        //                 <TextField id="outlined-basic" label="案例文件名" variant="outlined" value={createCaseFileName}
        //                            onChange={(e)=>{setCreateCaseFileName(e.target.value)}}
        //                 />
        //                 <br/>
        //                 <Button variant="contained" color="primary"
        //                         onClick={(e)=>{
        //                             createFile(e)
        //                     }}
        //                 >
        //                     创建
        //                 </Button>
        //                 <Button variant="contained" color="secondary" onClick={(e)=>{handleCloseCreate('','')}}>
        //                     取消
        //                 </Button>
        //         </DialogContent>
        //     </Dialog>
        //     <Dialog open={settingWindowOpen} onClose={handleCloseSetting}>
        //         <DialogTitle>设置</DialogTitle>
        //         <DialogContent>
        //             <TextField id="outlined-basic" label="工作区路径" variant="outlined" value={workSpacePath}
        //                        onChange={(e)=>{setWorkSpacePath(e.target.value)}}
        //             />
        //             <br/>
        //             <Button variant="contained" color="primary"
        //                     onClick={(e)=>{
        //                         setWorkSpace(e)
        //                     }}
        //             >
        //                 设置或创建
        //             </Button>
        //             <Button variant="contained" color="secondary" onClick={(e)=>{handleCloseSetting('','')}}>
        //                 取消
        //             </Button>
        //         </DialogContent>
        //     </Dialog>
        //     <CardContent className={classes.content}>
        //         <AceEditor
        //             mode="python"
        //             theme="pastel_on_dark"
        //             name="UNIQUE_ID_OF_DIV"
        //             editorProps={{ $blockScrolling: true }}
        //             value={scriptsData}
        //             onChange={changeHandle}
        //             // style={{height:'90%',width:'100%'}}
        //             width={'100%'}
        //             height={'100%'}
        //         />
        //         {isRecording &&
        //         <div className={classes.recoverContent}>
        //             <CircularProgress size={24} className={classes.recoverProgress}/>
        //         </div>
        //         }
        //     </CardContent>  
        //     <CaseList
        //         open={casesWindowOpen}
        //         onClose={handleCloseCases}
        //         load={upload}
        //     />
        // </Card> 
            <div className={classes.root}>
                <div className={classes.cardHeader}>
                    <div className={classes.cardHeaderTitle}>Script Window{caseName && `   ：${caseName}`}</div>
                    <div className={classes.cardHeaderAction}>
                        <EditorBtn aria-label="settings" title={'脚本列表'} onClick={()=>{setCasesWindowOpen(true)}} disabled={isRecording || isRunning}>
                            <i className="iconfont">&#xe600;</i>
                        </EditorBtn>
                        <EditorBtn aria-label="settings" title={runned ? '继续' : '开始'} onClick={runned ? continuePlay : runCase} disabled={runned ? (isRecording || !isConnected || !isRunning || !isPausing) : (isRecording || isRunning || !isConnected)}>
                            <PlayArrow fontSize="small" />
                        </EditorBtn>
                        <EditorBtn aria-label="settings" title={'暂停'} onClick={pause} disabled={isRecording || !isConnected || !isRunning || isPausing}>
                            <Pause fontSize="small" />
                        </EditorBtn>
                        <EditorBtn aria-label="settings" title={'通过VS CODE打开工作区'} onClick={()=>{openInVS()}} disabled={isRecording || isRunning}>
                            {/* <Code fontSize="small" /> */}
                            <i className="iconfont">&#xe66c;</i>
                        </EditorBtn>
                        <EditorBtn aria-label="settings" title={'导出脚本'} onClick={saveAs} disabled={isRecording || isRunning}>
                            <SaveAlt fontSize="small" />
                        </EditorBtn>
                    </div>
                </div>
                <div className={classes.content}>
                    <AceEditor
                        className={classes.editor}
                        mode="python"
                        theme="pastel_on_dark"
                        name="UNIQUE_ID_OF_DIV"
                        editorProps={{ $blockScrolling: true }}
                        value={scriptsData}
                        onChange={changeHandle}
                        width={'100%'}
                        height={'100%'}
                        commands={[{
                            name: 'saveFile', //键绑定的名称。
                            bindKey: {win: 'Ctrl-S', mac: 'Command-S'}, //用于命令的组合键。
                            exec: ()=> {}
                        }]}
                        setOptions={{
                            enableBasicAutocompletion: true,   //启用基本自动完成功能
                            enableLiveAutocompletion: true,   //启用实时自动完成功能 （比如：智能代码提示）
                            enableSnippets: true,  //启用代码段
                            showLineNumbers: true,
                            wrap: true,
                        }}
                        onLoad={editorInstance => {
                            editorInstance.container.style.resize = "both";
                            // mouseup = css resize end
                            document.addEventListener("mouseup", e => (
                            editorInstance.resize()
                            ));
                        }}
                    />
                    {isRecording &&
                    <div className={classes.recoverContent}>
                        <CircularProgress size={24} className={classes.recoverProgress}/>
                    </div>
                    }
                </div>
                <CaseList
                    open={casesWindowOpen}
                    onClose={handleCloseCases}
                    load={upload}
                    isRunning={isRunning}
                    isRecording={isRecording}
                    ShowMsg={ShowMsg}
                    caseName={caseName}
                    onChangeCaseName={(s) => onChangeCaseName(s)}
                    scriptsData={scriptsData}
                    onChangeScriptsData={(s) => onChangeScriptsData(s)}
                />
            </div>
    )
}