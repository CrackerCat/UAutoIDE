import React, {useEffect, useState} from "react";
import {
    Box,
    Collapse,
    IconButton,
    makeStyles,
    Paper,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow, Typography
} from "@material-ui/core";
import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import KeyboardArrowUpIcon from '@material-ui/icons/KeyboardArrowUp';
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
    root:{
        // background:'lightgrey'
    }
}))
const useRowStyles = makeStyles({
    root: {
        '& > *': {
            borderBottom: 'unset',
        },
    },
});

function Row(props) {
    const { row } = props;
    const [open, setOpen] = React.useState(false);
    const classes = useRowStyles();

    return (
        <React.Fragment>
            <TableRow className={classes.root}>
                <TableCell>
                    <IconButton aria-label="expand row" size="small" onClick={() => setOpen(!open)}>
                        {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
                    </IconButton>
                </TableCell>
                <TableCell component="th" scope="row">
                    {row.type}
                </TableCell>
                {/*<TableCell align="right">{row.calories}</TableCell>*/}
            </TableRow>
            <TableRow>
                <TableCell style={{ paddingBottom: 0, paddingTop: 0 }} colSpan={6}>
                    <Collapse in={open} timeout="auto" unmountOnExit>
                        <Box margin={1}>
                            <Typography variant="h6" gutterBottom component="div">
                                Properties
                            </Typography>
                            <Table size="small" aria-label="purchases">
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
    const [componentsInfo,setComponents] = useState(components)


    useEffect(()=>{
        if(curID !== 0)
        {
            window.pywebview.api.get_inspector({'ID':curID}).then((res)=>{
                setComponents(res['msg']['components'])
            })
        }
    },[curID])

    return (
        <TableContainer component={Paper} className={classes.root}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell align={"left"}>Components</TableCell>
                        {/*<TableCell align="right">Value</TableCell>*/}
                    </TableRow>
                </TableHead>
                <TableBody>
                    {componentsInfo.map((row) => (
                        <Row key={row.id} row={row} />
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}