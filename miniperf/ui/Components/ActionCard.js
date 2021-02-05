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
                <Button variant="contained" color="primary" className={classes.item} endIcon={<TouchApp/>} disabled>
                    Click
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={[<TouchApp/>,<Adjust/>]} disabled>
                    Long Click
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Send/>} disabled>
                    Send Key
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<CancelScheduleSend/>} disabled>
                    Clear Key
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<TrendingFlat/>} disabled>
                    Swipe
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<PanTool/>} disabled>
                    Drag
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<AspectRatio/>} disabled>
                    ScreenShot
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Crop/>} disabled>
                    Crop
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<Search/>} disabled>
                    Match
                </Button>
                <Button variant="contained" color="primary" className={classes.item} endIcon={<GetApp/>} disabled>
                    Install APK
                </Button>
            </CardContent>
        </Card>
    )
}