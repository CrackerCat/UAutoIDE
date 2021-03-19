import React, {useEffect, useRef, useState} from 'react'
import MuiAlert from '@material-ui/lab/Alert';
import {
    AppBar,
    Button, CircularProgress, Dialog, DialogContent, DialogTitle, FormControl, FormControlLabel,
    Input,
    InputAdornment, InputLabel, MenuItem, Select, Snackbar, TextField,
    Toolbar,
    Switch
} from "@material-ui/core";
import { createMuiTheme, makeStyles, ThemeProvider } from '@material-ui/core/styles';
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

const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#11698e',
        },
        secondary: {
            main: '#f44336',
        },
        type: 'dark',
    },
});

const useStyle = makeStyles((style)=>({
    grow: {
        flexGrow: 1,
    },
    Input:{
        color:'#f44336 !important',
        width:'200px'
    },
    AppBarON:{
        'background-color':'green'
    },
    AppBarOFF:{
        'background-color':'#11698e'
    },

    Button:{
        'border-radius': 0
    },
    ButtonConnect:{
        'background-color':'green'
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
    }
}))

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

    useInterval(()=>{
        checkConnection()
        // if(!isConnected && !loading){
        //     getCurDevice()
        // }
    },1000)

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
    const switchMode = (e) =>{
        setEnableAdvancedMode(e.target.checked)
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
                    <AppBar position={"static"} className={isConnected?classes.AppBarON:classes.AppBarOFF}>
                        <Toolbar>
                            <FormControl variant="filled" className={classes.Input}>
                                <InputLabel id="demo-simple-select-filled-label">手机设备</InputLabel>
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
                            </FormControl>
                            <TextField
                                id="filled-helperText"
                                label="IP地址"
                                variant="filled"
                                className={classes.Input}
                                value={ip}
                                onChange={changeIPValue}
                            />
                            <div className={classes.wrapper}>
                                {!isConnected && <Button variant="contained" color="primary" size="medium" disableElevation className={[classes.Button,classes.ButtonConnect]} onClick={connect} disabled={isConnected || loading}>连接</Button>}
                                {isConnected && <Button variant="contained" color="secondary" size="medium" disableElevation className={[classes.Button]} onClick={disConnect} disabled={!isConnected || loading}>断开</Button>}
                                {loading && <CircularProgress size={24} className={classes.buttonProgress} />}
                            </div>
                            {/*<Button variant="contained" color="primary" size="medium" disableElevation onClick={test}>Test</Button>*/}
                            <div className={classes.grow} />
                            <div>
                                <Button variant="contained" color="primary" size="small" disableElevation onClick={()=>{setIsFirst(true)}} disabled={tutorialsMode || isConnected}>新手指导</Button>
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
                            </div>
                        </Toolbar>
                    </AppBar>
                    <Dialog open={isFirst} className={classes.beginCard}>
                        <DialogTitle id="simple-dialog-title">新用户？</DialogTitle>
                        <DialogContent>
                            <Button variant="contained" color="primary" size="medium" disableElevation onClick={beginTutorial}>进行教学</Button>
                            &nbsp;&nbsp;&nbsp;&nbsp;
                            <Button variant="contained" color="secondary" size="medium" disableElevation onClick={finishNewUser}>跳过</Button>
                        </DialogContent>
                    </Dialog>
                    <TutorialsBoard
                        open={tutorialsWindowOpen}
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
                            <EditorCard ShowMsg={showMsg} isConnected={isConnected} tutorials={tutorialsMode} setTutorialsMode={setTutorialsMode} changeADV={(e)=>{setAdvancedModeDisable(e)}}/>
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
                                <div className={'mBlock1'}  style={setWidth(3)}>
                                    <PropTable curID={curObjID}/>
                                </div>
                            )}
                            {enableAdvancedMode && <div className={'hScroller'} id={'scroller3'} draggable={"true"} onDragEnd={handleMouseMove}></div>}
                            <div className={'mBlock'}  style={setWidth(4)}>
                                <ConsoleCard/>
                            </div>

                        </div>

                    </div>
                </div>
                <Snackbar open={okOpen} autoHideDuration={3000} onClose={handleClose}>
                    <Alert severity={logType} onClose={handleClose}>
                        {message}
                    </Alert>
                </Snackbar>
            </ThemeProvider>
            // </div>
        )
}