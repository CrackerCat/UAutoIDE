import {TreeItem, TreeView} from "@material-ui/lab";
import React, {useEffect} from "react";
import {ChevronRight, ExpandMore, RotateLeft} from "@material-ui/icons";
import {Card, CardContent, CardHeader, IconButton, makeStyles} from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    root:{
        'overflow-y':'auto'
    },
    content:{
        height: '100%',
        'overflow-y':'auto'
    },
}));


export default function HierarchyContent(){
    const classes = useStyles()
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
                    >
                        {renderTree(hierarchyData)}
                    </TreeView>
            </CardContent>
        </Card>
    )


}