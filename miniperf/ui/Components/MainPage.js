import React, {useEffect, useRef, useState} from 'react'
import MuiAlert from '@material-ui/lab/Alert';
import {
    AppBar,
    Button, CircularProgress,
    Input,
    InputAdornment, Snackbar, TextField,
    Toolbar
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
    Input:{
        color:'#f44336 !important'
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
    }
}))

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}


export default function MainPage(){
    const classes = useStyle()
    const [okOpen, setOkOpen] = React.useState(false);
    const [isConnected, setIsConnected] = React.useState(false);
    const [loading, setLoading] = React.useState(false);
    const [message, setMessage] = React.useState('');
    const [sn, setSN] = useState("");
    const [ip, setIP] = useState("");
    const [curObjID,setCurObjID] = useState(0)
    const [leftP,setLeftP] = useState(24.5)
    const [rightP,setRightP] = useState(24.5)
    const [mouseMoving,setMouseMoving] = useState(false)
    const changeSNValue = (e) =>{
        setSN(e.target.value);
    }
    const changeIPValue = (e) =>{
        setIP(e.target.value);
    }



    //底部消息弹窗关闭事件
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOkOpen(false);
    };
    //底部消息弹窗
    let showMsg = (msg)=>{
        setMessage(msg)
        setOkOpen(true)
    }
    //连接设备
    const connect = function (){
        setLoading(true)
        window.pywebview.api.connect({'sn':sn,'ip':ip}).then((res)=>{
            // setIsConnected(res['ok'])
            showMsg(res['msg'])
            setLoading(false)
        })
    }
    //断开连接
    const disConnect = function (){
        setLoading(true)
        window.pywebview.api.disConnect().then((res)=>{
            // setIsConnected(false)
            showMsg(res['msg'])
            setLoading(false)
        })
    }
    const test = function (e){
        const reader = new FileReader();
        reader.readAsText(e.target.files[0])
        reader.onload = function (e){
            showMsg(e.target.result)
        }
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
    },1000)

    useEffect(()=>{
        setTimeout(()=>{
            getCurDevice()
        },2000)
    },[])

    const getCurDevice = () =>{
        window.pywebview.api.getCurDevice().then((res)=>{
            setSN(res['msg'])
        })
    }

    const handleMouseDown=(e)=>{
        setMouseMoving(true)
    }
    const handleMouseMove=(e)=>{
        let content = document.getElementById('content')
        let w = content.offsetWidth
        let cw = e.pageX
        let id = e.target.id
        if(id === 'scroller1'){
            setLeftP(cw/w * 100)
        }
        else{
            setRightP((1 - cw/w) * 100)
        }

    }
    const handleMouseUp=(e)=>{

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
                            <TextField
                                id="filled-helperText"
                                label="设备号"
                                variant="filled"
                                className={classes.Input}
                                value={sn}
                                onChange={changeSNValue}
                            />
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
                            {/*<input*/}
                            {/*    id="contained-button-file"*/}
                            {/*    className={classes.upload}*/}
                            {/*    multiple*/}
                            {/*    type="file"*/}
                            {/*    onChange={test}*/}
                            {/*/>*/}
                            {/*<label htmlFor="contained-button-file">*/}
                            {/*    <Button variant="contained" color="primary" component="span">*/}
                            {/*        Upload*/}
                            {/*    </Button>*/}
                            {/*/!*<Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button}>test</Button>*!/*/}
                            {/*</label>*/}
                        </Toolbar>
                    </AppBar>
                    <div id={'content'}>
                        <div className={'left'} style={setWidth(1)}>
                            {/*<ActionCard/>*/}
                            {/*<PropTable/>*/}
                            <HierarchyContent ShowMsg={showMsg} getCurID={getCurID}/>
                        </div>
                        <div className={'scroller'} id={'scroller1'} draggable={"true"} onDragEnd={handleMouseMove}>

                        </div>
                        <div className={'middle'}>
                            <EditorCard ShowMsg={showMsg} isConnected={isConnected}/>
                            <ConsoleCard/>
                        </div>
                        <div className={'scroller'} id={'scroller2'} draggable={"true"} onDragEnd={handleMouseMove}>

                        </div>
                        <div className={'right'} style={setWidth(2)}>
                            {/*<ScreenCard/>*/}
                            <PropTable curID={curObjID}/>
                        </div>
                    </div>
                </div>
                <Snackbar open={okOpen} autoHideDuration={6000} onClose={handleClose}>
                    <Alert severity="success" onClose={handleClose}>
                        {message}
                    </Alert>
                </Snackbar>
            </ThemeProvider>
            // </div>
        )
}