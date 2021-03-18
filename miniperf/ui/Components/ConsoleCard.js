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
        'overflow-y':'hide',
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
        }
    },
    textArea:{
        width : '100%',
        height: '100%',
        padding:0,
        'background-color':'#2C2828',
        border:0,
        color:'white',
        resize: 'none'
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
        margin: 0
    },
    cardContent: {
        padding: 0,
        '&:last-child': {
            paddingBottom: 0,
        }
    }
}));

const ConsoleBtn = withStyles({
    root: {
        padding: '0 5px',
    }
})(Button);


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
                        <DeleteForever fontSize="small" />
                    </ConsoleBtn>
                </div>
            </div>
            <div className={classes.content}>
                <ConsoleContent ref={clearInfo}/>
            </div>
        </div>
    )
}