import React, {useEffect, useRef, useState} from "react";
import {AppBar, Card, CardContent, makeStyles, Paper, Slide, Tab, Tabs} from "@material-ui/core";
import {TreeItem, TreeView} from "@material-ui/lab";
import {ChevronRight, ExpandMore} from "@material-ui/icons";
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

function ConsoleContent(props){
    const classes = useStyles()
    const [consoleData,setConsoleData] = useState('')//console的输出信息

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
}

// function Content(props){
//     console.log(props)
//     const {index,consoleData,...others} = props
//     if(index === 0){
//         return(
//             <Slide direction={"left"} in={true}>
//                 <div>
//                     <HierarchyContent/>
//                 </div>
//             </Slide>
//         )
//     }else{
//         return(
//             <ConsoleContent consoleData={consoleData}/>
//         )
//     }
// }

export default function ConsoleCard (props) {
    const classes = useStyles()
    const [page,setPage] = React.useState(0)

    const ChangePage = (e,v)=>{
        setPage(v)
    }

    return (
        <Card variant={'outlined'} className={classes.root}>
            <CardContent className={classes.content}>
                {/*<Paper square>*/}
                <Tabs
                    value={page}
                    indicatorColor="primary"
                    textColor="primary"
                    onChange={ChangePage}
                    aria-label="disabled tabs example"
                >
                    {/*<Tab label={'Hierarchy'}/>*/}
                    <Tab label={'Console'}/>
                </Tabs>
                {/*<Content index={page} consoleData={consoleData}/>*/}
                {/*</Paper>*/}
                <ConsoleContent/>

            </CardContent>
        </Card>
    )
}