import React, {useEffect, useRef, useState} from 'react'
import MuiAlert from '@material-ui/lab/Alert';
import {
    AppBar,
    Button,
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
import {purple,blue} from "@material-ui/core/colors";


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

    },
    Button:{
        'border-radius': 0
    }
}))

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}


export default function MainPage(){
    const classes = useStyle()
    const [okOpen, setOkOpen] = React.useState(false);
    const [isConnected, setIsConnected] = React.useState(false);
    const [message, setMessage] = React.useState('');
    const [sn, setSN] = useState("");
    const [ip, setIP] = useState("");

    const changeSNValue = (e) =>{
        setSN(e.target.value);
    }
    const changeIPValue = (e) =>{
        setIP(e.target.value);
    }
    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }
        setOkOpen(false);
    };

    let showMsg = (msg)=>{
        setMessage(msg)
        setOkOpen(true)
    }

    const connect = function (){
        window.pywebview.api.connect({'sn':sn,'ip':ip}).then((res)=>{
            setIsConnected(res['ok'])
            showMsg(res['msg'])
        })
    }
    const disConnect = function (){
        window.pywebview.api.disConnect().then((res)=>{
            setIsConnected(false)
            showMsg(res['msg'])
        })
    }
    const test = function (){
        window.pywebview.api.test().then((res)=>{
            showMsg(res['msg'])
        })
    }

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
        return (
            // <div className={classes.root}>
            <ThemeProvider theme={theme}>
                <div className={'container'}>
                    <AppBar position={"static"}>
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
                            <Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button} onClick={connect} disabled={isConnected}>连接</Button>
                            <Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button} onClick={disConnect} disabled={!isConnected}>断开</Button>
                            <Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button} onClick={test}>test</Button>
                        </Toolbar>
                    </AppBar>
                    <div id={'content'}>
                        <div className={'left'}>
                            <ActionCard/>
                            <PropTable/>
                        </div>
                        <div className={'middle'}>
                            <EditorCard ShowMsg={showMsg}/>
                            <ConsoleCard/>
                        </div>
                        <div className={'right'}>
                            <ScreenCard/>
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