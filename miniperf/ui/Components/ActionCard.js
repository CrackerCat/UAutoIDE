import React from "react";
import {Button, Card, CardContent, Icon, makeStyles} from "@material-ui/core";
import {
    TouchApp,
    Adjust,
    Send,
    CancelScheduleSend,
    PanTool,
    TrendingFlat,
    AspectRatio,
    Crop,
    Search, GetApp
} from '@material-ui/icons';
const useStyles = makeStyles((theme) => ({
    root: {
        width : '100%',
        height: '40%',
        'overflow-y':'auto',
        // background:'lightgrey'
    },
    itemContent: {
        display: 'flex',
        'flex-direction': 'column',
        flex:1
    },
    item:{
        'margin-top':'5px'
    }
}));

export default function ActionCard () {
    const classes = useStyles();
    return(
        <Card variant={'outlined'} className={classes.root}>
            <CardContent className={classes.itemContent}>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<TouchApp/>}>
                    Click
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={[<TouchApp/>,<Adjust/>]}>
                    Long Click
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Send/>}>
                    Send Key
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<CancelScheduleSend/>}>
                    Clear Key
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<TrendingFlat/>}>
                    Swipe
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<PanTool/>}>
                    Drag
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<AspectRatio/>}>
                    ScreenShot
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Crop/>}>
                    Crop
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Search/>}>
                    Match
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<GetApp/>}>
                    Install APK
                </Button>
            </CardContent>
        </Card>
    )
}