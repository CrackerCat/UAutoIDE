import React, {useEffect, useRef, useState} from 'react'
import MuiAlert from '@material-ui/lab/Alert';
import {
    AppBar,
    ButtonGroup, Button, CircularProgress, Dialog, DialogContent, DialogTitle, FormControl, FormControlLabel,
    Input,
    InputAdornment, InputLabel, MenuItem, Select, Snackbar, TextField,
    Toolbar,
    Switch
} from "@material-ui/core";
import { Videocam, NoteAdd, Folder, Cloud, Settings } from '@material-ui/icons'
import { createMuiTheme, makeStyles, ThemeProvider, withStyles } from '@material-ui/core/styles';
import './MainPage.css'
import ActionCard from "./ActionCard";
import PropTable from "./PropTable";
import EditorCard from "./EditorCard";
import ConsoleCard from "./ConsoleCard";
import ScreenCard from "./ScreenCard";
import HierarchyContent from "./HierarchyContent";
import {useInterval} from "../Util/Util"
import * as PropTypes from "prop-types";
import TutorialsBoard from "./TutorialsBoard";
import CaseList from "./CasesList";

const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#313131',
        },
        secondary: {
            main: '#424242',
        },
        type: 'dark',
    },
});

const useStyle = makeStyles((style)=>({
    root: {
        height: '100vh',
    },
    grow: {
        flexGrow: 1,
    },
    Input:{
        color:'#f44336 !important',
        width:'200px',
    },
    AppBarON:{
        'background-color':'green'
    },
    AppBarOFF:{
        'background-color':'#313131'
    },

    Button:{
        'border-radius': 0,
        'background-color':'red',
        color: '#fff',
        fontSize: '12px',
        height: 22
    },
    ButtonConnect:{
        'background-color':'green',
        color: '#fff'
    },
    ButtonDisConnect:{

    },
    buttonProgress: {
        color: 'white',
        position: 'absolute',
        top: '50%',
        left: '50%',
        marginTop: -12,
        marginLeft: -12,
    },
    wrapper: {
        margin: theme.spacing(1),
        position: 'relative',
    },
    beginCard:{
        'text-align':'center',
    },
    toolbar: {
        minHeight: 42
    },
    toolbarContainer: {
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    deviceContainer: {
        display: 'flex',
        alignItems: 'center'
    },
    ipInput: {
        padding: 10
    },
    settingBtns: {
        display: 'flex',
        alignItems: 'center'
    },
    mainBtn: {
        fontSize: '12px',
        height: 26
    }
}))

const ToolbarBtn = withStyles({
    root: {
        background: '#424242'
    }
})(Button);

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}


class SimpleDialog extends React.Component {
    render() {
        return null;
    }
}

SimpleDialog.propTypes = {
    onClose: PropTypes.func,
    open: PropTypes.func,
    selectedValue: PropTypes.any
};
export default function MainPage(){
    const classes = useStyle()
    const [okOpen, setOkOpen] = React.useState(false);//底部消息弹窗是否打开
    const [logType,setLogType] = useState('success')//底部消息弹窗类型
    const [isConnected, setIsConnected] = React.useState(false);//是否连接上的设备
    const [loading, setLoading] = React.useState(false);//连接中
    const [message, setMessage] = React.useState('');//提示框的内容
    const [sn, setSN] = useState("");//设备的设备号
    const [ip, setIP] = useState("");//设备的ip
    const [curObjID,setCurObjID] = useState(0)//当前选择的game object的ID
    const [leftP,setLeftP] = useState(40)//左框宽度
    const [rightP,setRightP] = useState(40)//右框宽度
    const [middleTopP,setMiddleTopP] = useState(60)//中框上侧宽度
    const [phoneList,setPhoneList] = useState([])//手机列表
    const [phone,setPhone] = useState('')//当前选择的手机
    const [tutorialsWindowOpen,setTutorialsWindowOpen] = useState(false)//教学模式弹窗
    const [tutorialsMode,setTutorialsMode] = useState(false)//教学模式
    const [isFirst,setIsFirst] = useState(false)//新用户
    let [enableAdvancedMode,setEnableAdvancedMode] = useState(false)//开启高级模式
    const [advancedModeDisable,setAdvancedModeDisable] = useState(true)//高级模式是否可更改
    const [enableHierarchy,setEnableHierarchy] = useState(true)//Hierarchy是否能用
    const [isRecording,setIsRecording] = React.useState(false) //是否正在录制
    const [needSave,setNeedSave] = React.useState(false)
    const [isRunning,setIsRunning] = React.useState(false)
    const [createWindowOpen,setCreateWindowOpen] = useState(false)//创建案例文件弹窗
    const [createCaseName,setCreateCaseName] = useState('')//创建案例文件案例名
    const [createCaseFileName,setCreateCaseFileName] = useState('')//创建案例文件文件名
    const [caseName,setCaseName] = useState('')//当前案例名称
    const [scriptsData,setScriptsData] = React.useState('')
    const [settingWindowOpen,setSettingWindowOpen] = useState(false)//设置弹窗
    const [workSpacePath,setWorkSpacePath] = useState('')//设置案例工作区路径
    const [casesWindowOpen,setCasesWindowOpen] = useState(false)//案例文件弹窗
    const [isPausing,setIsPausing] = React.useState(false)

    let changeSNValue = (e) =>{
        setSN(e.target.value);
    }
    const changeIPValue = (e) =>{
        setIP(e.target.value);
    }

    //连接设备
    let connect = function (d,e = '',name = ''){
        setLoading(true)
        if(e !== ''){
            setSN(e)
            setPhone(name)
        }
        showMsg('连接中，请打开目标程序')
        window.pywebview.api.connect({'sn':e===''?sn:e,'ip':ip}).then((res)=>{
            // setIsConnected(res['ok'])
            if(res['ok']){
                showMsg('连接成功：' + res['msg']['ip'],res['ok'])
                setIP(res['msg']['ip'])
                let version = res['msg']['version']
                let tmp = version.split('.')[0]
                setEnableHierarchy(parseInt(tmp) >= 2)//当版本号大于2.0时可以使用Hierarchy
            }
            else {
                showMsg(res['msg'],res['ok'])
            }
            setLoading(false)

        })
    }
    //断开连接
    const disConnect = function (){
        setLoading(true)
        window.pywebview.api.disConnect().then((res)=>{
            // setIsConnected(false)
            showMsg(res['msg'],false)
            setLoading(false)
            setSN('')
            setPhone('')
            setIP('')
        })
    }
    //教学弹窗关闭事件
    let handleCloseTutorials = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setTutorialsWindowOpen(false);
    };
    //底部消息弹窗关闭事件
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOkOpen(false);
    };
    //底部消息弹窗
    let showMsg = (msg,type = true)=>{
        setMessage(msg)
        setLogType(type?'success':'error')
        setOkOpen(true)
    }
    //设置弹窗关闭事件
    let handleCloseSetting = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setWorkSpacePath('')
        setSettingWindowOpen(false);
    };
    //案例文件弹窗关闭事件
    let handleCloseCases = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCasesWindowOpen(false);
    };

    let upload = function (v){
        window.pywebview.api.loadCase({'caseName':v}).then((res)=>{
            setCaseName(v)
            showMsg(v,res['ok'])
            setIsPausing(false)
            setScriptsData(res['msg'])
            handleCloseCases('','')
        })
    }
    
    const test = function (e){
        // setTutorialsMode(true)
        // setTutorialsWindowOpen(true)
        window.pywebview.api.test().then((res)=>{
            console.log(res['msg'])
        })
        // setCasesWindowOpen(true)

    }
    //检测连接状态
    const checkConnection = function (){
        window.pywebview.api.checkConnection().then((res)=>{
            let status = res['msg']
            if (isConnected !== status['isConnected']) {
                setIsConnected(status['isConnected'])
            }
        })
    }

    // 按钮
    const record = () => {
        setIsRecording(true)
        showMsg('开始录制，长按屏幕5秒结束录制')
        window.pywebview.api.record({'caseName': caseName}).then((res)=>{
            showMsg(res['msg'])
            setIsRecording(false)
            setNeedSave(false)
        })
    }
    const handleChangeRecording = e => {
        setIsRecording(e)
    }
    const handleChangeNeedSave = e => {
        setNeedSave(e)
    }
    const handleChangeRunning = e => {
        setIsRunning(e)
    }
    const handleChangeCaseName = s => {
        setCaseName(s)
    }
    const handleChangeScriptsData = s => {
        setScriptsData(s)
    }
    const handleChangeIsPausing = e => {
        setIsPausing(e)
    }

    //创建案例文件弹窗关闭事件
    let handleCloseCreate = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setCreateWindowOpen(false);
    };

    useInterval(()=>{
        checkConnection()
        if(!isConnected && !loading){
            getCurDevice()
        }
    },1000)

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
                showMsg(res['msg'],res['ok'])
            }
        })
    }

    let setWorkSpace = (v) => {
        if(workSpacePath === '')
            return
        window.pywebview.api.setWorkSpace({'path':workSpacePath}).then((res)=>{
            if(res['ok']){
                setWorkSpacePath('')
                handleCloseSetting('','')
                setCaseName('')
                setScriptsData('')
                showMsg(res['msg'],res['ok'])
            }else{
                showMsg(res['msg'],res['ok'])
            }
        })
    }

    //检测是否为新用户
    const isNewUser = () =>{
        window.pywebview.api.isNewUser().then((res)=>{
            setIsFirst(res['msg'])
        })
    }
    //新用户设置完毕
    const finishNewUser = () =>{
        window.pywebview.api.finishNewUser().then((res)=>{
            setIsFirst(false)
        })
    }

    const beginTutorial = () =>{
        window.pywebview.api.finishNewUser().then((res)=>{
            setIsFirst(false)
            setTutorialsMode(true)
            setTutorialsWindowOpen(true)
        })
    }

    useEffect(()=>{
        setTimeout(isNewUser,2000)
    },[])

    useEffect(()=>{
        if(enableAdvancedMode){
            setLeftP(24.5)
            setRightP(24.5)
        }else{
            setLeftP(70)
            setRightP(30)
        }
    },[enableAdvancedMode])

    //获取连接在电脑的手机列表
    const getCurDevice = () =>{
        window.pywebview.api.getCurDevice().then((res)=>{
            if(res['ok']){
                let list = res['msg']
                setPhoneList(list)
                let s = []
                if(res['msg'].length > 0 && phone === ''){
                    setPhone(res['msg'][0]['name'])
                    setSN(res['msg'][0]['sn'])
                }
            }else{
                showMsg(res['msg'],res['ok'])
            }
        })
    }

    //切换高级模式
    const switchMode = () =>{
        setEnableAdvancedMode(!enableAdvancedMode)
    }
    //选择需要连接的手机
    const handleChange = (e) =>{
        setPhone(e.target.value)
        for (let i in phoneList){
            let p = phoneList[i]
            if(p['name'] === e.target.value){

                setSN(p['sn'])
            }
        }
    }

    const handleMouseMove=(e)=>{
        let content = document.getElementById('content')
        let w = content.offsetWidth
        let h = content.offsetHeight
        let cw = e.pageX
        let ch = e.pageY
        let id = e.target.id
        if(id === 'scroller1'){
            setLeftP(cw/w * 100)
            if(!enableAdvancedMode){
                setRightP(100 - (cw/w * 100))
            }
        }
        else if(id === 'scroller2'){
            setRightP((1 - cw/w) * 100)
        }
        else if(id === 'scroller3'){
            let hh = ch/h * 100 > 90?90:ch/h * 100
            setMiddleTopP(hh)
        }

    }
    const setWidth = (e) =>{
        if(e === 1)
        {
            return {'width':leftP + '%'}
        }
        else if(e === 2)
        {
            return {'width':rightP + '%'}
        }
        else if(e === 3)
        {
            return {'height':(middleTopP) + '%'}
        }
        else if(e === 4)
        {
            return {'height':(100 - middleTopP - 0.5) + '%'}
        }
    }


    let getCurID = (e) =>{
        setCurObjID(e)
    }
    
        return (
            // <div className={classes.root}>
            <ThemeProvider theme={theme}>
                <div className={'container'}>
                    <AppBar position={"static"} className={isConnected?classes.AppBarON:classes.AppBarOFF}>
                        <Toolbar className={classes.toolbar}>
                            {/* <FormControl className={classes.Input} variant="filled">
                                {phoneList.length > 0 ? (
                                    <Select
                                    labelId="demo-simple-select-filled-label"
                                    id="demo-simple-select-filled"
                                    value={phone}
                                    onChange={handleChange}
                                    onOpen={getCurDevice}
                                    disabled={isConnected || loading}
                                >
                                    {phoneList.map((v)=>{
                                        return <MenuItem value={v.name}>{v.name}</MenuItem>
                                    })}
                                    {phoneList.length === 0 && <MenuItem><em>None</em></MenuItem>}
                                </Select>
                                ) : (<Button variant="filled" color="primary" disableElevation>No Devices</Button>)}
                            </FormControl>
                            <TextField
                                id="filled-helperText"
                                label="IP地址"
                                className={classes.Input}
                                value={ip}
                                onChange={changeIPValue}
                            /> */}

                            {/* new UI: ToolBar */}
                            <div className={classes.toolbarContainer}>
                                <div className={classes.deviceContainer}>
                                    <div>
                                        {phoneList.length > 0 ? (
                                            <Select
                                                style={{width: '200px', height: '22px', fontSize: '12px'}}
                                                value={phone}
                                                onChange={handleChange}
                                                onOpen={getCurDevice}
                                                disabled={isConnected || loading}
                                            >
                                                {phoneList.map((v)=>{
                                                    return <MenuItem value={v.name}>{v.name}</MenuItem>
                                                })}
                                            </Select>
                                        ) : (<ToolbarBtn size="small" style={{ width: '200px', height: '22px', fontSize: '12px', lineHeight: '12px' }}>No Devices</ToolbarBtn>)}
                                        <Input placeholder="IP地址" value={ip} onChange={changeIPValue} className={classes.ipInput} style={{ height: '22px', fontSize: '12px' }}/>
                                    </div>
                                    <div className={classes.wrapper}>
                                        {!isConnected && <Button variant="contained" color="primary" size="small" disableElevation className={[classes.Button, classes.mainBtn, classes.ButtonConnect]} onClick={connect} disabled={isConnected || loading}>连接</Button>}
                                        {isConnected && <Button variant="contained" color="primary" size="small" disableElevation className={[classes.Button, classes.mainBtn]} onClick={disConnect} disabled={!isConnected || loading}>断开</Button>}
                                        {loading && <CircularProgress size={24} className={classes.buttonProgress} />}
                                    </div>
                                </div>
                                <ToolbarBtn size="small" style={{padding: '0 15px'}} className={classes.mainBtn} onClick={record} disabled={isRecording || isRunning || !isConnected}><Videocam />开始录制</ToolbarBtn>
                                <div className={classes.settingBtns}>
                                    <ButtonGroup style={{ marginRight: '15px' }}>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'新建脚本'} onClick={()=>{setCreateWindowOpen(true)}} disabled={isRecording || isRunning}><NoteAdd fontSize="small" /></ToolbarBtn>
                                        <ToolbarBtn size="small" className={classes.mainBtn}><Folder fontSize="small" /></ToolbarBtn>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'选择脚本'} onClick={()=>{setCasesWindowOpen(true)}} disabled={isRecording || isRunning}><Cloud fontSize="small" /></ToolbarBtn>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'设置'} onClick={()=>{setSettingWindowOpen(true)}} disabled={isConnected}><Settings fontSize="small" /></ToolbarBtn>
                                    </ButtonGroup>
                                    <ToolbarBtn size="small" className={classes.mainBtn} style={{ marginRight: '15px', padding: '0 15px' }} disableElevation onClick={beginTutorial} disabled={tutorialsMode || isConnected}>新手指引</ToolbarBtn>
                                    <ToolbarBtn size="small" className={classes.mainBtn} style={{padding: '0 15px'}} disabled={!advancedModeDisable} onClick={switchMode}>启用{enableAdvancedMode ? '简易' : '高级'}模式</ToolbarBtn>
                                </div>
                            </div>
                            
                            {/* <div className={classes.wrapper}>
                                {!isConnected && <Button variant="contained" color="primary" size="medium" disableElevation className={[classes.Button,classes.ButtonConnect]} onClick={connect} disabled={isConnected || loading}>连接</Button>}
                                {isConnected && <Button variant="contained" color="secondary" size="medium" disableElevation className={[classes.Button]} onClick={disConnect} disabled={!isConnected || loading}>断开</Button>}
                                {loading && <CircularProgress size={24} className={classes.buttonProgress} />}
                            </div> */}
                            {/* <div>
                                <Button variant="contained" color="primary" size="small" disableElevation onClick={()=>{setIsFirst(true)}} disabled={tutorialsMode || isConnected}>新手指引</Button>
                                <FormControlLabel
                                    control={
                                        <Switch
                                            disabled={!advancedModeDisable}
                                            checked={enableAdvancedMode}
                                            onChange={switchMode}
                                            name="checkedB"
                                            color="secondary"
                                        />
                                    }
                                    label="启用高级模式"
                                />
                                <Button variant="contained" color="primary" size="small" disableElevation disabled={tutorialsMode || isConnected}>启用高级模式</Button>
                            </div> */}
                        </Toolbar>
                    </AppBar>
                    {/* <Dialog open={isFirst} className={classes.beginCard}>
                        <DialogTitle id="simple-dialog-title">新用户？</DialogTitle>
                        <DialogContent>
                            <Button variant="contained" color="primary" size="medium" disableElevation onClick={beginTutorial}>进行教学</Button>
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            <Button variant="contained" color="secondary" size="medium" disableElevation onClick={finishNewUser}>跳过</Button>
                        </DialogContent>
                    </Dialog> */}
                    <TutorialsBoard
                        open={tutorialsWindowOpen}
                        // open={true}
                        onClose={handleCloseTutorials}
                        isConnected={isConnected}
                        loading={loading}
                        connect={connect}
                        changeSNValue={changeSNValue}
                        phoneList={phoneList}
                        showMsg={showMsg}
                    />

                    <div id={'content'}>
                        {enableAdvancedMode && (
                            <div className={'left'} style={setWidth(1)}>
                                <HierarchyContent isConnected={isConnected} getCurID={getCurID} enable={enableHierarchy}/>
                                {/*{!enableAdvancedMode && (*/}
                                {/*    <EditorCard ShowMsg={showMsg} isConnected={isConnected} tutorials={tutorialsMode} setTutorialsMode={setTutorialsMode}  changeADV={(e)=>{setAdvancedModeDisable(e)}}/>*/}
                                {/*)}*/}
                            </div>
                        )}
                        {enableAdvancedMode && (
                            <div className={'scroller'} id={'scroller1'} draggable={"true"} onDragEnd={handleMouseMove}>
                            </div>
                        )}
                        {/*<div className={enableAdvancedMode?'middle':'content'}>*/}
                        {/*        <div className={enableAdvancedMode?'mBlock':'left'}  style={enableAdvancedMode?setWidth(3):setWidth(1)}>*/}
                        {/*            <EditorCard ShowMsg={showMsg} isConnected={isConnected} tutorials={tutorialsMode} setTutorialsMode={setTutorialsMode} changeADV={(e)=>{setAdvancedModeDisable(e)}}/>*/}
                        {/*        </div>*/}
                        {/*        {enableAdvancedMode && (*/}
                        {/*            <div className={'hScroller'} id={'scroller3'} draggable={"true"} onDragEnd={handleMouseMove}>*/}
                        {/*            </div>*/}
                        {/*        )}*/}
                        {/*        {!enableAdvancedMode && (*/}
                        {/*            <div className={'scroller'} id={'scroller1'} draggable={"true"} onDragEnd={handleMouseMove}>*/}
                        {/*            </div>*/}
                        {/*        )}*/}
                        {/*        <div className={enableAdvancedMode?'mBlock':'right'}  style={enableAdvancedMode?setWidth(4):setWidth(2)}>*/}
                        {/*            <ConsoleCard/>*/}
                        {/*        </div>*/}
                        {/*</div>*/}
                        <div className={'middle'}>
                            <div className={'mBlock1'} style={enableAdvancedMode ? setWidth(3) : {height: '100%'}}>
                            <EditorCard 
                                ShowMsg={showMsg} 
                                isConnected={isConnected} 
                                tutorials={tutorialsMode} 
                                setTutorialsMode={setTutorialsMode} 
                                isRecording={isRecording}
                                onChangeRecording={e => handleChangeRecording(e)}
                                needSave={needSave}
                                onChangeNeedSave={e => handleChangeNeedSave(e)}
                                isRunning={isRunning}
                                onChangeRunning={e => handleChangeRunning(e)}
                                changeADV={(e)=>{setAdvancedModeDisable(e)}}
                                caseName={caseName}
                                onChangeCaseName={s => handleChangeCaseName(s)}
                                scriptsData={scriptsData}
                                onChangeScriptsData={s => handleChangeScriptsData(s)}
                                isPausing={isPausing}
                                onChangeIsPausing={e => handleChangeIsPausing(e)}
                            />
                            </div>
                            {enableAdvancedMode && <div className={'hScroller'} id={'scroller3'} draggable={"true"} onDragEnd={handleMouseMove}></div>}
                            {enableAdvancedMode && <div className={'mBlock'}  style={setWidth(4)}>
                                <ConsoleCard/>
                            </div>}
                        </div>
                        {/*<div className={'mBlock'}>*/}
                        {/*    <EditorCard ShowMsg={showMsg} isConnected={isConnected} tutorials={tutorialsMode} setTutorialsMode={setTutorialsMode} changeADV={(e)=>{setAdvancedModeDisable(e)}}/>*/}
                        {/*</div>*/}
                        {/*<div className={'mBlock'}>*/}
                        {/*    <ConsoleCard/>*/}
                        {/*</div>*/}
                        {enableAdvancedMode && (
                            <div className={'scroller'} id={'scroller2'} draggable={"true"} onDragEnd={handleMouseMove}>
                            </div>
                        )}
                        <div className={'right'} style={setWidth(2)}>
                            {enableAdvancedMode && (
                                <div className={'mBlock1'}>
                                    <PropTable curID={curObjID}/>
                                </div>
                            )}
                            {!enableAdvancedMode && <div className={'mBlock'}>
                                <ConsoleCard/>
                            </div>}
                        </div>

                    </div>
                </div>
                <Snackbar open={okOpen} autoHideDuration={3000} onClose={handleClose}>
                    <Alert severity={logType} onClose={handleClose}>
                        {message}
                    </Alert>
                </Snackbar>
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
                <CaseList
                    open={casesWindowOpen}
                    onClose={handleCloseCases}
                    load={upload}
                />
            </ThemeProvider>
            // </div>
        )
}