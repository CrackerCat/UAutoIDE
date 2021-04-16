import React, {useEffect, useImperativeHandle, useRef, useState} from "react";
import {
    Card,
    CardContent,
    CardHeader,
    IconButton,
    Button,
    makeStyles,
    withStyles,
} from "@material-ui/core";
import {DeleteForever} from "@material-ui/icons";
import {useInterval, useUpdate} from "../Util/Util";

const testData = {
    id : 'root',
    name : 'root',
    children:[
        {
            id : '2',
            name : '2'
        }
    ]
}
const useStyles = makeStyles((theme) => ({
    root: {
        width : '100%',
        height: '100%',
        'overflow-y':'hidden',
        // background:'lightgrey'
    },
    content:{
        width : '100%',
        height: 'calc(100% - 72px)',
        padding:0,
        display:'flex',
        'flex-direction':'column',
        '&:last-child': {
            paddingBottom: 0,
        },
    },
    logContainer: {
        height: 'calc(100% - 32px)',
    },
    textArea:{
        boxSizing: 'border-box',
        width : '100%',
        height: '100%',
        padding:'5px 12px',
        backgroundColor:'#2C2828',
        border:0,
        color:'white',
        // resize: 'none',
        overflow: 'auto',
        '&:focus': {
            outline: '0px solid transparent',
        }
    },
    cardHeader: {
        maxHeight: 22,
        padding: '5px 5px 5px 12px',
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
        margin: 0
    },
    cardContent: {
        padding: 0,
        '&:last-child': {
            paddingBottom: 0,
        }
    },
    infoLog: {
        color: '#52C41A'
    },
    errorLog: {
        color: '#FF4D4F'
    }
}));

const ConsoleBtn = withStyles({
    root: {
        padding: '0 5px',
    }
})(Button);


const ConsoleContent = React.forwardRef((props,ref)=>{
    const { consoleData, onChangeConsoleData } = props
    const classes = useStyles()
    const inputRef = useRef();
    useImperativeHandle(ref, () => ({
        clear: () => {
            onChangeConsoleData('')
        }
    }));

    //获取console的输出信息
    const getNewLog =  function(){
        const testInfo = new RegExp(/^(\[INFO\]).*/)
        const testError = new RegExp(/^(\[ERROR\]).*/)
        window.pywebview.api.PythonOutput().then((res)=>{
            if(res !== "405null") {
                // const ret = res.split('\n')
                // const list = ret.map(r => {
                //     if(testInfo.test(r.trim())) return (`<p style="margin: 3px 0; padding: 0; color: #fff; font-size: 12px; font-weight: 400;">${r}</p>`)
                //     if(testError.test(r.trim())) return (`<p style="margin: 3px 0; padding: 0; color: #FF4D4F;  font-size: 12px; font-weight: 400;">${r}</p>`)
                //     return `<p style="margin: 3px 0; padding: 0; color: #fff; font-size: 12px; font-weight: 400;">${r}</p>`
                // })
                if(testInfo.test(res)) {
                    res = `<pre style="margin: 0; padding: 0; color: #fff; font-size: 12px; font-weight: 400; line-height: 16px;">${res}</pre>`
                } else if(testError.test(res)) {
                    res = `<pre style="margin: 0; padding: 0; color: #FF4D4F;  font-size: 12px; font-weight: 400; line-height: 16px;">${res}</pre>`
                } else {
                    res = `<pre style="margin: 0; padding: 0; color: #fff; font-size: 12px; font-weight: 400; line-height: 16px;">${res}</pre>`
                }
                let l = consoleData
                l+=(res + '\n')
                // for(let item of list) {
                //     l += item
                // }
                onChangeConsoleData(l)
            }
        })
    }
    useInterval(()=>{
        getNewLog()
    },500)

    // useUpdate(()=>{
    //     setHeight()
    // },consoleData)

    useEffect(()=>{
        setHeight()
    },[consoleData])

    const setHeight = () =>{
        const textarea = document.getElementById('consoleArea');
        textarea.scrollTop = textarea.scrollHeight;
    }
    const noop = e => {
        e.preventDefault()
        return false
    }
    return(
        <div className={classes.logContainer}>
            <div
                className={classes.textArea} 
                id={'consoleArea'} 
                contentEditable={true}
                draggable={false}
                spellcheck="false"
                onCut={noop}
                onCopy={noop}
                onPaste={noop}
                onKeyDown={noop}
                onDragStart={noop}
                dangerouslySetInnerHTML={{__html: consoleData}}>
            </div>
        </div>
        // <div  className={classes.textArea}>
        //     <textarea value={consoleData}  className={classes.textArea} onChange={setHeight} id={'consoleArea'}/>
        // </div>
    )
})

export default function ConsoleCard (props) {
    const { consoleData, onChangeConsoleData } = props
    const classes = useStyles()
    const [page,setPage] = React.useState(0)
    const clearInfo = useRef()
    const ChangePage = (e,v)=>{
        setPage(v)
    }

    const handleChangeConsoleData = e => {
        onChangeConsoleData(e)
    }
    return (
        <div className={classes.root}>
            {/* <CardHeader
                className={classes.cardHeader}
                classes={{title: classes.cardHeaderTitle, action: classes.cardHeaderAction}} 
                title={'Log Window'}
                action={[
                    <ConsoleBtn aria-label="settings" title={'清空'} onClick={()=>{clearInfo.current.clear()}}>
                        <DeleteForever fontSize="small" />
                    </ConsoleBtn>
                ]}
            /> */}
            <div className={classes.cardHeader}>
                <div className={classes.cardHeaderTitle}>Log Window</div>
                <div className={classes.cardHeaderAction}>
                    <ConsoleBtn aria-label="settings" title={'清空'} onClick={()=>{clearInfo.current.clear()}}>
                        <i className="iconfont">&#xe610;</i>
                    </ConsoleBtn>
                </div>
            </div>
            {/* <div className={classes.content}> */}
                <ConsoleContent ref={clearInfo} style={{overflowY: 'scroll'}} consoleData={consoleData} onChangeConsoleData={e => handleChangeConsoleData(e)}/>
            {/* </div> */}
        </div>
    )
}