import React from "react";
import {makeStyles, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow} from "@material-ui/core";
function createData(name, value) {
    return { name, value };
}

const RowData = [
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23'),
    createData('2313','23')
]

const useStyle = makeStyles((style)=>({
    root:{
        // background:'lightgrey'
    }
}))

export default function PropTable() {
    const classes = useStyle()
    return (
        <TableContainer component={Paper} className={classes.root}>
            <Table>
                <TableHead>
                    <TableRow>
                        <TableCell>Prop</TableCell>
                        <TableCell align="right">Value</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {RowData.map((row) => (
                        <TableRow key={row.name}>
                            <TableCell component="th" scope="row">
                                {row.name}
                            </TableCell>
                            <TableCell align="right">{row.value}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    )
}