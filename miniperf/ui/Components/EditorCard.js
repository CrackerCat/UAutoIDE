import React, {useEffect, useRef} from "react";
import {UnControlled as CodeMirror} from "react-codemirror2";
import 'codemirror/lib/codemirror.css'
import 'codemirror/lib/codemirror'

import 'codemirror/theme/ayu-mirage.css'
import 'codemirror/mode/clike/clike'
import 'codemirror/mode/python/python'
import {Card, CardContent, CardHeader, IconButton, makeStyles, TextareaAutosize} from "@material-ui/core";
import {Adb, GetApp, MissedVideoCall, RotateLeft, SendOutlined, Stop} from "@material-ui/icons";
import AceEditor from "react-ace";

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
    textArea:{
        height: '100% !important',
        width: '100% !important',
        position:'absolute',
        left:0,
        right:0,
        bottom:0,
        top:0
    }
}));

function useInterval(callback, delay) {
    const savedCallback = useRef();

    // Remember the latest callback.
    useEffect(() => {
        savedCallback.current = callback;
    });

    // Set up the interval.
    useEffect(() => {
        function tick() {
            savedCallback.current();
        }
        if (delay !== null) {
            let id = setInterval(tick, delay);
            return () => clearInterval(id);
        }
    }, [delay]);
}



export default function EditorCard () {
    const [scriptsData,setScriptsData] = React.useState('')
    const classes = useStyles()
    useInterval(()=>{
        window.pywebview.api.test().then((res)=>{
            setScriptsData(res['msg'])
        })
    },1000)

    function record(){
        window.pywebview.api.record().then((res)=>{
            setScriptsData(res['msg'])
        })
    }


    return (
        <Card variant={'outlined'} className={classes.root}>
            <CardHeader title={'Coding'} action={[
                <IconButton aria-label="settings" title={'录制'} onClick={record}>
                    <MissedVideoCall/>
                </IconButton>,
                <IconButton aria-label="settings" title={'重置'}>
                    <RotateLeft/>
                </IconButton>,
                <IconButton aria-label="settings" title={'下载'}>
                    <GetApp/>
                </IconButton>,
                <IconButton aria-label="settings" title={'运行'}>
                    <SendOutlined/>
                </IconButton>,
                <IconButton aria-label="settings" title={'调试'}>
                    <Adb/>
                </IconButton>,
                <IconButton aria-label="settings" title={'停止'}>
                    <Stop/>
                </IconButton>
            ]}/>
            <CardContent className={classes.content}>
                {/*<CodeMirror*/}
                {/*    value='re'*/}
                {/*    options={{*/}
                {/*        lineNumbers: true,*/}
                {/*        theme:'ayu-mirage',*/}
                {/*        mode:'python'*/}
                {/*    }}*/}
                {/*    */}
                {/*>*/}
                {/*</CodeMirror>*/}
                <AceEditor
                    mode="java"
                    theme="github"
                    name="UNIQUE_ID_OF_DIV"
                    editorProps={{ $blockScrolling: true }}
                    className={classes.textArea}
                    value={scriptsData}
                />
            </CardContent>
        </Card>

    )
}