import {TreeItem, TreeView} from "@material-ui/lab";
import React, {useEffect} from "react";
import {ChevronRight, ExpandMore, RotateLeft} from "@material-ui/icons";
import {Card, CardContent, CardHeader, IconButton, Typography, Button, makeStyles, withStyles} from "@material-ui/core";


const useStyles = makeStyles((theme) => ({
    '@global': {
        '.MuiTreeItem-group': {
            marginLeft: 7,
            paddingLeft: 8,
            paddingTop: 5,
            // borderLeft: '1px dashed rgba(255, 255, 255, 0.5)',
        },
        '.MuiTypography-body1': {
            fontSize: '0.9rem'
        }
    },
    root:{
        height: '100%',
        'overflow-y':'auto',
        color: '#fff'
    },
    content:{
        height: '100%',
        'overflow-y':'auto'
    },
    cardHeader: {
        maxHeight: 22,
        padding: '5px 5px 5px 24px',
        background: '#424242',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        boxShadow: '0px 1px 1px rgb(0 0 0 / 50%)'
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

const HierarchyBtn = withStyles({
    root: {
        padding: '0 5px',
    }
})(Button);

export default function HierarchyContent(props){
    const {isConnected,getCurID,enable} = props
    const classes = useStyles()
    const select = (e,id) =>{
        getCurID(id)
    }
    const renderTree = (nodes) => (
        <TreeItem key={nodes.id} nodeId={nodes.id} label={nodes.name}>
            {Array.isArray(nodes.children) ? nodes.children.map((node) => renderTree(node)) : null}
        </TreeItem>
    );
    const [hierarchyData,setHierarchyData] = React.useState({})
    function getData(){
        window.pywebview.api.showItem().then((res)=>{
            if(res['ok']){
                setHierarchyData(res['msg']['objs'])
            }
        })
    }
    useEffect(()=>{
        if(!isConnected){
            setHierarchyData({})
            getCurID(0)
        }
        if(isConnected) {
            getData()
        }
    },[isConnected])

    return(
        <div className={classes.root}>
            {/* <CardHeader title={'Hierarchy'} action={[
                <IconButton aria-label="settings" title={'刷新'} disabled={!enable || !isConnected} onClick={getData}>
                    <RotateLeft/>
                </IconButton>
            ]}/> */}
            <div className={classes.cardHeader}>
                <div className={classes.cardHeaderTitle}>Hierarchy</div>
                {/* <Typography variant="h6" gutterBottom component="div">Hierarchy</Typography> */}
                <div className={classes.cardHeaderAction}>
                    <HierarchyBtn aria-label="settings" title={'刷新'} disabled={!enable || !isConnected} onClick={getData}>
                        <RotateLeft fontSize="small"/>
                    </HierarchyBtn>
                </div>
            </div>
            <div>
                <TreeView
                    defaultCollapseIcon={<ExpandMore />}
                    defaultExpandIcon={<ChevronRight />}
                    defaultExpanded={['root']}
                    onNodeSelect={select}
                >
                    {renderTree(hierarchyData)}
                </TreeView>
            </div>
        </div>
    )


}