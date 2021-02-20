import React, {useImperativeHandle, useRef, useState} from "react";
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
        height: '40%',
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
        height: '90%',
        padding:0,
        'background-color':'#424242',
        border:0,
        color:'white',
        resize: 'none'
    }
}));

// function HierarchyContent(){
//     const renderTree = (nodes) => (
//         <TreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
//             {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
//         </TreeItem>
//     );
//     const [hierarchyData,setHierarchyData] = React.useState({})
//     const [hasData,setHasData] = React.useState(false)
//     function getData(){
//         window.pywebview.api.showItem().then((res)=>{
//             // console.log('res',res)
//             setHierarchyData(res['msg']['objs'])
//         })
//     }
//     useEffect(()=>{
//         setTimeout(()=>{
//             getData()
//         },1000)
//     },[])
//
//         return(
//             <TreeView
//                 defaultCollapseIcon={<ExpandMore />}
//                 defaultExpandIcon={<ChevronRight />}
//                 defaultExpanded={['root']}
//             >
//                 {renderTree(hierarchyData)}
//             </TreeView>
//         )
//
//
// }

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

    useUpdate(()=>{
        setHeight()
    },consoleData)

    const setHeight = () =>{
        console.log('change')
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