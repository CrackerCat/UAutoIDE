import React, {useEffect, useState} from "react";
import {
    Box, CardHeader,
    Collapse,
    createMuiTheme,
    IconButton,
    makeStyles,
    ThemeProvider,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow, Typography
} from "@material-ui/core";
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
import KeyboardArrowRightIcon from '@material-ui/icons/KeyboardArrowRight';
import * as PropTypes from "prop-types";

const components = [{
    "id": 16936,
    "type": "UnityEngine.Transform",
    "properties": [{
        "name": "m_LocalRotation",
        "type": "Quaternion",
        "value": "(0.7064338, 0.4777144, 0.03084357, 0.5213338)"
    }, {
        "name": "m_LocalPosition",
        "type": "Vector3",
        "value": "(0.24, 3, 4.18)"
    }, {
        "name": "m_LocalScale",
        "type": "Vector3",
        "value": "(1, 1, 1)"
    }]
}, {
    "id": 16934,
    "type": "UnityEngine.Light",
    "enabled": true,
    "properties": [{
        "name": "m_Type",
        "type": "Enum",
        "value": "Directional"
    }, {
        "name": "m_Shape",
        "type": "Enum",
        "value": "Cone"
    }, {
        "name": "m_Color",
        "type": "Color",
        "value": "RGBA(1, 0.9568627, 0.8392157, 1)"
    }, {
        "name": "m_Intensity",
        "type": "Float",
        "value": "2"
    }, {
        "name": "m_Range",
        "type": "Float",
        "value": "10"
    }, {
        "name": "m_SpotAngle",
        "type": "Float",
        "value": "30"
    }, {
        "name": "m_InnerSpotAngle",
        "type": "Float",
        "value": "21.80208"
    }, {
        "name": "m_CookieSize",
        "type": "Float",
        "value": "10"
    }]
}]
const useStyle = makeStyles((style)=>({
    '@global': {
        '.MuiTableCell-root': {
            padding: '5px 16px'
        },
        '.MuiCollapse-container .MuiTableCell-root': {
            border: '1px solid rgba(81, 81, 81, 1)',
        },
        '.MuiCollapse-container td, .MuiCollapse-container th': {
            wordBreak: 'break-all'
        },
        '.MuiTableContainer-root': {
            maxHeight: 'calc(100% - 32px - 54px)',
            minWidth: '100%',
            maxWidth: '100%',
            overflow: 'auto'
        },
    },
    root:{
        // background:'lightgrey'
        width: '100%',
        '& > .MuiTableCell-root': {
            borderBottom: '1px solid rgba(81, 81, 81, 1)',
        }
    },
    cardHeader: {
        height: 22,
        padding: '5px 5px 5px 24px',
        background: '#424242',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        fontSize: 14,
        color: '#fff',
        boxShadow: '0px 1px 1px rgb(0 0 0 / 50%)'
    },
}))
const useRowStyles = makeStyles({
    root: {
        // '& > *': {
        //     borderBottom: 'unset',
        // },
        width: '100%',
    },
    cellContainer: {
        display: 'block',
        width: '100%',
        whiteSpace: 'nowrap',
        overflow: 'hidden',
        textOverflow: 'ellipsis',
    }
});

function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);
    const classes = useRowStyles();

    return (
        <React.Fragment>
            <TableRow className={classes.root}>
                <TableCell style={{maxWidth: '30px', width: '10%', padding: '5px', textAlign: 'center'}}>
                    <div>
                        <IconButton aria-label="expand row" size="small" onClick={() => setOpen(!open)}>
                            {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowRightIcon />}
                        </IconButton>
                        {/* {row.type} */}
                    </div>
                </TableCell>
                <TableCell style={{width: '90%', padding: '5px'}}>
                    <div className={classes.cellContainer} title={row.type}>
                        {row.type}
                    </div>
                </TableCell>
                {/*<TableCell component="th" scope="row" align={'left'}>*/}
                {/*    {row.type}*/}
                {/*</TableCell>*/}
                {/*<TableCell align="right">{row.calories}</TableCell>*/}
            </TableRow>
            <TableRow>
                <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={8}>
                    <Collapse in={open} timeout="auto" unmountOnExit>
                        <Box margin={1}>
                            {/* <Typography variant="h6" gutterBottom component="div">
                                Properties
                            </Typography> */}
                            <Table size="small" style={{tableLayout: 'fixed'}} aria-label="purchases">
                                <TableHead>
                                    <TableRow>
                                        <TableCell>name</TableCell>
                                        <TableCell>value</TableCell>
                                    </TableRow>
                                </TableHead>
                                <TableBody>
                                    {row.properties.map((propertiesRow) => (
                                        <TableRow key={propertiesRow.name}>
                                            <TableCell component="th" scope="row">
                                                {propertiesRow.name}
                                            </TableCell>
                                            <TableCell>{propertiesRow.value}</TableCell>
                                        </TableRow>
                                    ))}
                                </TableBody>
                            </Table>
                        </Box>
                    </Collapse>
                </TableCell>
            </TableRow>
        </React.Fragment>
    );
}
Row.propTypes = {
    row: PropTypes.shape({
        calories: PropTypes.number.isRequired,
        carbs: PropTypes.number.isRequired,
        fat: PropTypes.number.isRequired,
        history: PropTypes.arrayOf(
            PropTypes.shape({
                amount: PropTypes.number.isRequired,
                customerId: PropTypes.string.isRequired,
                date: PropTypes.string.isRequired,
            }),
        ).isRequired,
        name: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        protein: PropTypes.number.isRequired,
    }).isRequired,
};

export default function PropTable(props) {
    const {curID} = props
    const classes = useStyle()
    const [componentsInfo,setComponents] = useState([])


    useEffect(()=>{
        if(curID !== 0)
        {
            window.pywebview.api.get_inspector({'ID':curID}).then((res)=>{
                setComponents(res['msg']['components'])
            })
        }else{
            setComponents([])
        }
    },[curID])

    return (
        <div className={classes.root}>
            <div className={classes.cardHeader}>Components</div>
            <TableContainer>
                <Table size="small" style={{tableLayout: 'fixed'}}>
                    {/* <TableHead> */}
                        {/* <TableRow> */}
                            {/* <TableCell align={"left"}></TableCell> */}
                            {/* <div className={classes.cardHeader}>Components</div> */}
                            {/* <TableCell align="right">Value</TableCell> */}
                        {/* </TableRow> */}
                    {/* </TableHead> */}
                    <TableBody>
                        {componentsInfo.map((row) => (
                            <Row key={row.id} row={row} />
                        ))}
                    </TableBody>
                </Table>
            </TableContainer>
        </div>
    )
}