import React from 'react'
import {UnControlled as CodeMirror} from "react-codemirror2";

import {
    AppBar,
    Button,
    Input,
    InputAdornment,
    Toolbar
} from "@material-ui/core";
import { createMuiTheme, makeStyles, ThemeProvider } from '@material-ui/core/styles';
import './MainPage.css'
import ActionCard from "./ActionCard";
import PropTable from "./PropTable";
import EditorCard from "./EditorCard";
import ConsoleCard from "./ConsoleCard";
import ScreenCard from "./ScreenCard";
import {purple,blue} from "@material-ui/core/colors";


const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#11698e',
        },
        secondary: {
            main: '#f44336',
        },
        type: 'dark',
    },
});

const useStyle = makeStyles((style)=>({
    Input:{

    },
    Button:{
        'border-radius': 0
    }
}))


export default function MainPage(){
    const classes = useStyle()
        return (
            // <div className={classes.root}>
            <ThemeProvider theme={theme}>
                <div className={'container'}>
                    <AppBar position={"static"}>
                        <Toolbar>
                            <Input
                                id="standard-adornment-password"
                                type={'text'}
                                label="Standard"
                                className={classes.Input}
                                endAdornment={
                                    <InputAdornment position="end">
                                        <Button variant="contained" color="primary" size="medium" disableElevation className={classes.Button}>连接</Button>
                                    </InputAdornment>
                                }
                            />
                        </Toolbar>
                    </AppBar>
                    <div id={'content'}>
                        <div className={'left'}>
                            <ActionCard/>
                            <PropTable/>
                        </div>
                        <div className={'middle'}>
                            <EditorCard/>
                            <ConsoleCard/>
                        </div>
                        <div className={'right'}>
                            <ScreenCard/>
                        </div>
                    </div>
                </div>
            </ThemeProvider>
            // </div>
        )
}