import React, {useEffect, useRef, useState} from 'react'
import MuiAlert from '@material-ui/lab/Alert';
import {
    AppBar,
    ButtonGroup, Button, IconButton, CircularProgress, Dialog, DialogContent, DialogTitle, DialogActions, FormControl, FormControlLabel,
    Input, InputBase,
    Typography,
    InputAdornment, InputLabel, MenuItem, Select, Snackbar, TextField,
    Toolbar,
    Switch,
} from "@material-ui/core";
import { Videocam, NoteAdd, Folder, Cloud, Close, InsertDriveFile, Settings, BorderColor, Opacity } from '@material-ui/icons'
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
import { borders } from '@material-ui/system'

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
    overrides: {
        MuiInputLabel: {
            root: {
                '&$focused': {
                    color: '#fff'
                }
            },
        },
        MuiInputBase: {
            input: {
                padding: 0
            }
        },
        MuiOutlinedInput:{
            // input: {
            //     padding: '5px 14px'
            // }
        },
        MuiButton: {
            root: {
                lineHeight: 1,
            }
        }
    }
});

const useStyle = makeStyles((style)=>({
    '@global': {
        '.MuiTypography-h6': {
            fontSize: 18,
        },
        '.MuiOutlinedInput-input': {
            fontSize: 14
        },
        '.MuiFormLabel-root': {
            fontSize: 14
        },
        '.MuiInputLabel-outlined.MuiInputLabel-shrink': {
            transform: 'translate(14px, -6px) scale(0.85)'
        }
    },
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
        'background-color':'rgba(82, 196, 26, 0.7)',
    },
    AppBarOFF:{
        'background-color':'#313131'
    },
    settingBtns: {
        display: 'flex',
        alignItems: 'center'
    },
    mainBtn: {
        fontSize: '12px',
        height: 26,
        '&:hover': {
            backgroundColor: '#595959'
        }
    },
    Button:{
        'border-radius': 0,
        'background-color':'red',
        color: '#fff',
        fontSize: '12px',
        borderRadius: 5,
    },
    ButtonConnect:{
        'background-color':'green',
        color: '#fff',
        '&:hover': {
            backgroundColor: '#389e0d'
        }
    },
    ButtonDisConnect:{
        '&:hover': {
            backgroundColor: '#cf1322'
        },
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
        minHeight: 54,
    },
    toolbarContainer: {
        width: '100%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
    },
    deviceContainer: {
        padding: '3px 0',
        display: 'flex',
        alignItems: 'center'
    },
    selectInput: {
        background: '#424242',
        width: '200px', 
        height: '26px', 
        fontSize: '12px',
    },
    ipInput: {
        padding: 10,
        background: '#424242',
        color: '#fff',
        border: '1px solid rgba(255, 255, 255, 0.23)',
        borderRadius: 4
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
    workspaceBtn: {
        backgroundColor: '#1890ff',
        color: '#fff',
        '&:hover': {
            backgroundColor: '#096dd9',
        },
    },
    workspaceActions: {
        padding: 24,
        display: 'flex',
        justifyContent: 'space-around',
        alignContent: 'center'
    },
    dialogContent: {
        overflow: 'hidden',
        display: 'flex',
        flexFlow: 'column',
        justifyContent: 'space-between',
        alignItems: 'center'
    },
    notchedOutline: {},
    focused: {
        "& $notchedOutline": {
            borderColor: "#fff !important"
        }
    },
    recordingDialog: {
        overflow: 'hidden',
        display: 'flex',
        flexFlow: 'column',
        justifyContent: 'ceter',
        alignItems: 'center'
    },
    recordingDialogHeader: {
        display: 'flex',
        alignItems: 'center',
        '& > h2': {
            margin: '0 20px',
        }
    },
    recordingDialogContent: {
        margin: '20px',
        fontSize: '20px'
    },
    recordingDialogBtn: {
        margin: '20px',
        width: '20%',
        backgroundColor: '#666'
    },
    muiDialogTitle: {
        display: 'flex',
        justifyContent: 'flex-end',
        padding: 5,
    },
    closeButton: {
        position: 'absolute',
        right: theme.spacing(1),
        top: theme.spacing(1),
        color: theme.palette.grey[500],
    },
    settingText: {
        fontSize: 14,
        fontWeight: 400
    },
    settingContent: {
        alignItems: 'flex-start',
        padding: '0 80px'
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
    const [isPausing,setIsPausing] = React.useState(false)
    const [consoleData,setConsoleData] = useState('')//console的输出信息
    const [recordWindowOpen,setRecordWindowOpen] = useState(false)//设置录制弹窗


    let changeSNValue = (e) =>{
        setSN(e.target.value);
    }
    const changeIPValue = (e) =>{
        setIP(e.target.value);
    }

    //教学弹窗关闭事件
    let handleCloseTutorials = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setTutorialsWindowOpen(false);
        setTutorialsMode(false);
    };

    //教学弹窗关闭事件
    let userOnClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setTutorialsWindowOpen(false);
        setTutorialsMode(false);
        if(isConnected){
            disConnect();
        }     
        showMsg('新手指引已关闭');
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
    //设置弹窗关闭事件
    let handleCloseSetting = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setWorkSpacePath('')
        setSettingWindowOpen(false);
    };

    
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
    function record(){
        setIsRecording(true)
        // showMsg('开始录制，长按屏幕5秒结束录制')
        window.pywebview.api.record({'caseName': caseName}).then((res)=>{
            setRecordWindowOpen(true);
            showMsg(res['msg'])
            setIsRecording(true)
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
    const handleChangeConsoleData = e => {
        setConsoleData(e)
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
        if(isRecording) {
            window.pywebview.api.is_debug_mode_record().then((res)=>{
                console.log(res)
                if(!res['ok']){
                    showMsg('已停止录制')
                    setRecordWindowOpen(false)
                    setIsRecording(false)
                    setNeedSave(false)
                }
            })
        }
    },1000)

    // 添加脚本
    const addFile = () =>{
        window.pywebview.api.addFile().then((res)=>{
            if(res){
                showMsg(res['msg'],res['ok'])
            }else{
                // showMsg("已取消添加脚本")
            }
        })
    }

    // 暂停录制
    const recordPause = () => {
        window.pywebview.api.recordPause().then(res => {
            showMsg(res['msg'])
            setIsRecording(false)
        })
    }
    // 停止录制
    const recordStop = () => {
        window.pywebview.api.recordStop().then(res => {
            showMsg(res['msg'])
            setRecordWindowOpen(false)
            setIsRecording(false)
            setNeedSave(false)
        })
    }
    // 继续录制
    const recordResume = () => {
        window.pywebview.api.recordResume().then(res => {
            showMsg(res['msg'])
            setIsRecording(true)
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
                showMsg(res['msg'],res['ok'])
            }
        })
    }

    // let setWorkSpace = (v) => {
    //     if(workSpacePath === '')
    //         return
    //     window.pywebview.api.setWorkSpace({'path':workSpacePath}).then((res)=>{
    //         if(res['ok']){
    //             setWorkSpacePath('')
    //             handleCloseSetting('','')
    //             setCaseName('')
    //             setScriptsData('')
    //             showMsg(res['msg'],res['ok'])
    //         }else{
    //             showMsg(res['msg'],res['ok'])
    //         }
    //     })
    // }

    let setWorkSpace = () => {
        window.pywebview.api.openUAUTOFile().then((res)=>{
            if(res){
                showMsg(res['msg'],res['ok'])
            }else{
                // showMsg("已取消工作区打开")
            }
            handleCloseSetting('','')
        })
    }

    let createuserWorkSpace = (e) => {
        window.pywebview.api.createuserWorkSpace().then((res)=>{
            if(res){
                showMsg(res['msg'],res['ok'])
            }else{
                // showMsg("已取消工作区创建")
            }
            handleCloseSetting('','')
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

    const isDevicesChange = () =>{
        window.pywebview.api.isDevicesChange().then((res)=>{
            if(!isConnected && !loading)
            {
                getCurDevice()
            }
            isDevicesChange()
        })
    }

    useEffect(()=>{
        setTimeout(isNewUser,2000)
        setTimeout(isDevicesChange,2000)
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
                    setIP(res['msg'][0]['ip'])
                }
                else
                {
                    setPhone('')
                    setSN('')
                    setIP('')
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
                console.log(p['sn']);
                setIP(p['ip'])
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
                    <AppBar position={"static"}>
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
                                        <ButtonGroup>
                                            {phoneList.length > 0 ? (
                                                <Select
                                                    className={classes.selectInput}
                                                    value={phone}
                                                    onChange={handleChange}
                                                    onOpen={getCurDevice}
                                                    disabled={isConnected || loading}
                                                >
                                                    {phoneList.map((v)=>{
                                                        return <MenuItem value={v.name} key={v.name}>{v.name}</MenuItem>
                                                    })}
                                                </Select>
                                            ) : (<ToolbarBtn onClick={() => showMsg('请保证电脑连接到手机', false)} className={classes.mainBtn} size="small" style={{ width: '200px', height: '26px', fontSize: '12px', lineHeight: '12px' }}>No Devices</ToolbarBtn>)}
                                                <InputBase placeholder="IP地址" value={ip} onChange={changeIPValue} className={classes.ipInput} style={{height: '26px', fontSize: '12px' }}/>
                                            
                                        </ButtonGroup>
                                    </div>
                                    <div className={classes.wrapper}>
                                        {!isConnected && <Button variant="contained" color="primary" size="small" disableElevation className={[classes.Button, classes.mainBtn, classes.ButtonConnect]} onClick={connect} disabled={isConnected || loading}>连接</Button>}
                                        {isConnected && <Button variant="contained" color="primary" size="small" disableElevation className={[classes.Button, classes.mainBtn, classes.ButtonDisConnect]} onClick={disConnect} disabled={!isConnected || loading}>断开</Button>}
                                        {loading && <CircularProgress size={24} className={classes.buttonProgress} />}
                                    </div>
                                </div>
                                <ToolbarBtn size="small" style={{padding: '0 30px'}} className={classes.mainBtn} onClick={record} disabled={isRecording || isRunning || !isConnected}><i className="iconfont" style={{marginRight: 10}}>&#xe68d;</i>开始录制</ToolbarBtn>
                                <div className={classes.settingBtns}>
                                    <ButtonGroup style={{ marginRight: '20px' }}>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'新建脚本'} onClick={()=>{setCreateWindowOpen(true)}} disabled={isRecording || isRunning}>
                                            {/* <NoteAdd fontSize="small" style={{fontSize: '16px'}} /> */}
                                            <i className="iconfont">&#xe61d;</i>
                                        </ToolbarBtn>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'添加脚本'} onClick={addFile} disabled={isRecording || isRunning}>
                                            {/* <InsertDriveFile fontSize="small" style={{fontSize: '16px'}} /> */}
                                            <i className="iconfont">&#xe662;</i>
                                        </ToolbarBtn>
                                        <ToolbarBtn size="small" className={classes.mainBtn} title={'设置'} onClick={()=>{setSettingWindowOpen(true)}}>
                                            {/* <Folder fontSize="small" style={{fontSize: '16px'}}/> */}
                                            <i className="iconfont">&#xe726;</i>
                                        </ToolbarBtn>
                                    </ButtonGroup>
                                    <ToolbarBtn size="small" className={classes.mainBtn} style={{ marginRight: '20px', padding: '0 15px' }} disableElevation onClick={beginTutorial} disabled={isConnected}>新手指引</ToolbarBtn>
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
                        userOnClose={userOnClose}
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
                                <ConsoleCard consoleData={consoleData} onChangeConsoleData={e => handleChangeConsoleData(e)}/>
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
                                <ConsoleCard consoleData={consoleData} onChangeConsoleData={e => handleChangeConsoleData(e)}/>
                            </div>}
                        </div>

                    </div>
                </div>
                <Snackbar anchorOrigin={{ vertical: 'top', horizontal: 'center' }} open={okOpen} autoHideDuration={3000} onClose={handleClose}>
                    <Alert severity={logType} onClose={handleClose}>
                        {message}
                    </Alert>
                </Snackbar>
                <Dialog open={createWindowOpen} fullWidth={true} maxWidth="sm">
                    <DialogTitle>新建案例</DialogTitle>
                    <DialogContent className={classes.dialogContent}>
                            <TextField 
                                style={{width: '80%', marginBottom: '20px'}} 
                                id="outlined-basic" 
                                label="案例名称" 
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
                                style={{width: '80%'}}
                                id="outlined-basic" 
                                label="案例文件名" 
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
                <Dialog open={settingWindowOpen} onClose={handleCloseSetting} fullWidth={true} maxWidth="sm">
                    <DialogTitle>设置工作区</DialogTitle>
                    <DialogContent className={[classes.dialogContent, classes.settingContent]}>
                        {/* <TextField 
                            style={{width: '100%'}} 
                            id="outlined-basic" 
                            label="设置工作区" 
                            variant="outlined" 
                            value={workSpacePath}
                            InputProps={{
                                classes: {
                                    notchedOutline: classes.notchedOutline,
                                    focused: classes.focused
                                }
                            }}
                            onChange={(e)=>{setWorkSpacePath(e.target.value)}}
                        /> */}
                        <p className={classes.settingText}>创建：请选择一个空文件夹</p>
                        <p className={classes.settingText}>设置：请选择已创建工作区的setting.UAUTO</p>
                        
                    </DialogContent>
                    <DialogActions classes={{root: classes.workspaceActions}}>
                        <Button variant="contained" classes={{root: classes.workspaceBtn}} onClick={(e)=>{createuserWorkSpace(e)}}>
                            创建
                        </Button>
                        <Button variant="contained" classes={{root: classes.workspaceBtn}} onClick={(e)=>{setWorkSpace(e)}}>
                            设置
                        </Button>
                        <Button variant="contained" color="primary" onClick={(e)=>{handleCloseSetting('','')}}>
                            取消
                        </Button>
                    </DialogActions>
                </Dialog>
                <Dialog open={recordWindowOpen} fullWidth={true} maxWidth="sm" className={classes.muiDialog}>
                    <DialogTitle id="simple-dialog-title">
                    <IconButton aria-label="close" className={classes.closeButton} onClick={() => recordStop()}>
                        <Close />
                    </IconButton>
                    </DialogTitle>
                    <DialogContent className={classes.recordingDialog}>
                        <div className={classes.recordingDialogHeader}>
                            <h2>录制中</h2><CircularProgress style={{color: '#fff'}}/>
                        </div>
                        <div className={classes.recordingDialogContent}>可长按手机屏幕5秒结束录制</div>
                        {isRecording && <Button className={classes.recordingDialogBtn} onClick={() => recordPause()}>暂停录制</Button>}
                        {!isRecording && <Button className={classes.recordingDialogBtn} onClick={() => recordResume()}>继续录制</Button>}
                    </DialogContent>
                </Dialog>
            </ThemeProvider>
            // </div>
        )
}