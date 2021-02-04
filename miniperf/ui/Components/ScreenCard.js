import React from "react";
import {Button, ButtonGroup, Card, CardContent, makeStyles} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    root: {
        // background:'lightgrey'
        height:'100%',
        display:'flex',
        'flex-direction': 'column',
        'flex-flow': 'row wrap'
    },
    Screen:{
        width:'100%',
        height:'100%',
        display:'flex',
        'align-self': 'flex-start',
        flex: 1
    },
    Group: {
        height:'40px',
        width:'100%',
        display:'flex',
        'align-self': 'flex-end'
    },
    canvas: {
        height:'100%',
        width:'100%'
    }
}));

const Draw = function () {
    let screen = document.getElementById('screen')
    let context = screen.getContext('2d')
    let image = new Image()
    image.src = 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2853553659,1775735885&fm=26&gp=0.jpg'
    image.onload = ()=>{
        context.drawImage(image,0,0,screen.width,screen.height)
    }
    window.pywebview.api.test();
}

export default function ScreenCard () {
    const classes = useStyles()
    return (
        <div className={classes.root}>
            <div  className={classes.Screen}>
                <canvas id={'screen'} className={classes.canvas}/>
            </div>
            <ButtonGroup variant="contained" color="primary" aria-label="contained primary button group" fullWidth className={classes.Group}>
                <Button onClick={Draw}>One</Button>
                <Button>Two</Button>
                <Button>Three</Button>
                <Button>One</Button>
                <Button>Two</Button>
            </ButtonGroup>
        </div>
    )
}