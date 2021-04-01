import React, {useEffect, useState} from "react";
import {
    CircularProgress,
    Dialog,
    DialogContent,
    DialogTitle, IconButton,
    LinearProgress,
    List, ListItem, ListItemSecondaryAction,
    ListItemText
} from "@material-ui/core";
import {makeStyles} from "@material-ui/core/styles";
import {useInterval} from "../Util/Util";
import {PlayCircleFilled, Publish} from "@material-ui/icons";

const useStyle = makeStyles((theme)=>({
    root: {
        width: '100%',
    },
    listContent:{
        width:'360px',
        maxHeight: 480,
    }
}))

export default function CaseList(props){
    const classes = useStyle()
    const { onClose, open,load} = props;
    const [casesList,setCasesList] = useState([])

    const getCases = () =>{
        window.pywebview.api.loadCasesList().then((res)=>{
            if(res['ok']){
                setCasesList(res['msg'])
            }
        })
    }

    useEffect(()=>{
        if(open){
            getCases()
        }
    },[open])

    return(
        <Dialog open={open} onClose={onClose} className={classes.root}>
            <DialogTitle id="simple-dialog-title">案例列表</DialogTitle>
            <DialogContent className={classes.listContent}>
                <List component="nav" aria-label="secondary mailbox folders">

                    {casesList.map((v,i)=>(

                    <ListItem button>
                        <ListItemText primary={v.tag + '(' + v.run_case + '.py)'} />
                        <ListItemSecondaryAction>
                            <IconButton edge="end" aria-label="Publish" title={'加载'} onClick={(e)=>{load(v.run_case)}} id={v.run_case}>
                                <Publish/>
                            </IconButton>
                        </ListItemSecondaryAction>
                    </ListItem>

                    ))}

                    {/*<ListItem button>*/}
                    {/*    <ListItemText primary="Trash" />*/}
                    {/*    <ListItemSecondaryAction>*/}
                    {/*        <IconButton edge="end" aria-label="delete">*/}
                    {/*            <PlayCircleFilled/>*/}
                    {/*        </IconButton>*/}
                    {/*    </ListItemSecondaryAction>*/}
                    {/*</ListItem>*/}

                </List>
            </DialogContent>
        </Dialog>
    )
}