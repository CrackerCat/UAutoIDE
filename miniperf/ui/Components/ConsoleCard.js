import React, {useEffect, useRef} from "react";
import {AppBar, Card, CardContent, makeStyles, Paper, Tab, Tabs} from "@material-ui/core";
import {TreeItem, TreeView} from "@material-ui/lab";
import {ChevronRight, ExpandMore} from "@material-ui/icons";

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
        padding:0
    }
}));

function HierarchyContent(){
    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
        </TreeItem>
    );
    const [hierarchyData,setHierarchyData] = React.useState({})

    function getData(){
        window.pywebview.api.showItem().then((res)=>{
            console.log(res)
            setHierarchyData(res['msg']['objs'])
        })
    }
    useEffect(()=>{
        // console.log("第一次渲染");
        getData()
    },[])
    return(
        <TreeView
            defaultCollapseIcon={<ExpandMore />}
            defaultExpandIcon={<ChevronRight />}
            defaultExpanded={['root']}
        >
            {renderTree(hierarchyData)}
        </TreeView>
    )
}

function ConsoleContent(){
    const classes = useStyles()
    const [consoleData,setConsoleData] = React.useState([])
    const getNewLog =  function(){
        window.pywebview.api.PythonOutput().then((res)=>{
            if(res === "405null")
            {

            }
            else{
                let l = consoleData
                l.push(res)
                setConsoleData([...l])
                setHeight()
            }
        })
    }
    useInterval(()=>{
        getNewLog()
    },500)
    const setHeight = () =>{
        console.log('change')
        const textarea = document.getElementById('consoleArea');
        textarea.scrollTop = textarea.scrollHeight;
    }
    return(
        <div  className={classes.textArea}>{
            // consoleData.map((item)=>{
            //     return <div>{item}</div>
            // })
            <textarea value={consoleData}  className={classes.textArea} onChange={setHeight} id={'consoleArea'}/>
        }</div>
    )
}

function Content(props){
    console.log(props)
    const {index,...others} = props
    if(index === 0){
        return(
            <HierarchyContent/>
        )
    }else{
        return(
            <ConsoleContent/>
        )
    }
}

export default function ConsoleCard () {
    const classes = useStyles()
    const [page,setPage] = React.useState(1)

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
                    <Tab label={'Hierarchy'}/>
                    <Tab label={'Console'}/>
                </Tabs>
                <Content index={page}/>
                {/*</Paper>*/}

            </CardContent>
        </Card>
    )
}