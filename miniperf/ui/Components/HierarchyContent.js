import {TreeItem, TreeView} from "@material-ui/lab";
import React, {useEffect} from "react";
import {ChevronRight, ExpandMore, RotateLeft} from "@material-ui/icons";
import {Card, CardContent, CardHeader, IconButton, makeStyles} from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    root:{
        height: '100%',
        'overflow-y':'auto'
    },
    content:{
        height: '100%',
        'overflow-y':'auto'
    },
}));


export default function HierarchyContent(props){
    const {ShowMsg} = props
    const classes = useStyles()
    const select = (e,id) =>{
        ShowMsg(id)
    }
    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
        </TreeItem>
    );
    const [hierarchyData,setHierarchyData] = React.useState({})
    function getData(){
        window.pywebview.api.showItem().then((res)=>{
            setHierarchyData(res['msg']['objs'])
        })
    }
    useEffect(()=>{
        setTimeout(()=>{
            getData()
        },1000)
    },[])

    return(
        <Card className={classes.root}>
            <CardHeader title={'Hierarchy'} action={[
                <IconButton aria-label="settings" title={'刷新'} disabled={false} onClick={getData}>
                    <RotateLeft/>
                </IconButton>
            ]}/>
            <CardContent>
                <TreeView
                    defaultCollapseIcon={<ExpandMore />}
                    defaultExpandIcon={<ChevronRight />}
                    defaultExpanded={['root']}
                    onNodeSelect={select}
                >
                    {renderTree(hierarchyData)}
                </TreeView>
            </CardContent>
        </Card>
    )


}