import React, {useEffect, useRef} from "react";
import {AppBar, Card, CardContent, makeStyles, Paper, Slide, Tab, Tabs} from "@material-ui/core";
import {TreeItem, TreeView} from "@material-ui/lab";
import {ChevronRight, ExpandMore} from "@material-ui/icons";
import {useUpdate} from "../Util/Util";

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
        padding:0,
        'background-color':'#424242',
        border:0,
        color:'white'
    }
}));

function HierarchyContent(){
    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
        </TreeItem>
    );
    const [hierarchyData,setHierarchyData] = React.useState({})
    const [hasData,setHasData] = React.useState(false)
    function getData(){
        window.pywebview.api.showItem().then((res)=>{
            // console.log('res',res)
            setHierarchyData(res['msg']['objs'])
        })
    }
    useEffect(()=>{
        setTimeout(()=>{
            getData()
        },1000)
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

function ConsoleContent(props){
    const {consoleData} = props
    const classes = useStyles()

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

function Content(props){
    console.log(props)
    const {index,consoleData,...others} = props
    // return (
    //     <div>
    //         <Slide direction={"left"} in={index === 0}>
    //             <div>
    //                 <HierarchyContent/>
    //             </div>
    //         </Slide>
    //         <Slide direction={"left"} in={index === 1}  mountOnEnter unmountOnExit>
    //             <div className={classes.textArea}>
    //                 <ConsoleContent consoleData={consoleData}/>
    //             </div>
    //         </Slide>
    //     </div>
    // )
    if(index === 0){
        return(
            <Slide direction={"left"} in={true}>
                <div>
                    <HierarchyContent/>
                </div>
            </Slide>
        )
    }else{
        return(
            <ConsoleContent consoleData={consoleData}/>
        )
    }
}

export default function ConsoleCard (props) {
    let {consoleData} = props
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
                <Content index={page} consoleData={consoleData}/>
                {/*</Paper>*/}

            </CardContent>
        </Card>
    )
}