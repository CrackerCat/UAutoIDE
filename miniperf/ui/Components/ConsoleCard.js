import React, {useEffect, useImperativeHandle, useRef, useState} from "react";
import {
    Card,
    CardContent,
    CardHeader,
    IconButton,
    makeStyles,
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
        'overflow-y':'hide',
        // background:'lightgrey'
    },
    content:{
        width : '100%',
        height: '100%',
        padding:0,
        display:'flex',
        'flex-direction':'column'
    },
    textArea:{
        width : '100%',
        height: '100%',
        padding:0,
        'background-color':'#2C2828',
        border:0,
        color:'white',
        resize: 'none'
    }
}));


const ConsoleContent = React.forwardRef((props,ref)=>{
    const classes = useStyles()
    const [consoleData,setConsoleData] = useState('')//console的输出信息
    const inputRef = useRef();
    useImperativeHandle(ref, () => ({
        clear: () => {
            setConsoleData('')
        }
    }));

    //获取console的输出信息
    const getNewLog =  function(){
        window.pywebview.api.PythonOutput().then((res)=>{
            if(res !== "405null") {
                let l = consoleData
                l+=(res + '\n')
                setConsoleData(l)
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
    return(
            <div  className={classes.textArea}>
                <textarea value={consoleData}  className={classes.textArea} onChange={setHeight} id={'consoleArea'}/>
            </div>

    )
})

export default function ConsoleCard (props) {
    const classes = useStyles()
    const [page,setPage] = React.useState(0)
    const clearInfo = useRef()
    const ChangePage = (e,v)=>{
        setPage(v)
    }

    return (
        <Card variant={'outlined'} className={classes.root}>
            <CardHeader
                title={'Console'}
                action={[
                    <IconButton aria-label="settings" title={'清空'} onClick={()=>{clearInfo.current.clear()}}>
                        <DeleteForever/>
                    </IconButton>
                ]}
            />
            <CardContent className={classes.content}>
                <ConsoleContent ref={clearInfo}/>
            </CardContent>
        </Card>
    )
}