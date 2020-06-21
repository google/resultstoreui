import React from 'react';
import InfiniteScroll from 'react-infinite-scroll-component';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import { Column, InvocationTableProps } from './types';
import { parseInvocationTableData } from './utils';
import Spinner from '../Spinner';

const columns: Column[] = [
    { id: 'status', label: 'Status' },
    { id: 'name', label: 'Name' },
    { id: 'labels', label: 'Labels' },
    { id: 'date', label: 'Run Date' },
    { id: 'duration', label: 'Duration' },
    { id: 'user', label: 'User' },
];

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        margin: {
            margin: theme.spacing(2),
        },
        container: {
            display: 'flex',
            flexWrap: 'wrap',
        },
    })
);

/*
Table that displays results of an invocation search
*/
const InvocationTable: React.FC<InvocationTableProps> = ({
    invocations,
    pageToken,
    next,
}) => {
    const classes = useStyles();

    const rows = invocations.map((invocation) =>
        parseInvocationTableData(invocation)
    );

    return (
        <React.Fragment>
            <InfiniteScroll
                dataLength={invocations.length}
                loader={<Spinner />}
                hasMore={pageToken !== ''}
                next={() => next(false, pageToken)}
            >
                <TableContainer className={classes.container}>
                    <Table
                        stickyHeader
                        aria-label="sticky table"
                        className={classes.margin}
                    >
                        <TableHead>
                            <TableRow>
                                {columns.map((column) => (
                                    <TableCell
                                        key={column.id}
                                        align={column.align}
                                        style={{ minWidth: column.minWidth }}
                                    >
                                        {column.label}
                                    </TableCell>
                                ))}
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row) => {
                                return (
                                    <TableRow
                                        hover
                                        role="checkbox"
                                        tabIndex={-1}
                                        key={row.name}
                                    >
                                        {columns.map((column) => {
                                            return (
                                                <TableCell
                                                    key={column.id}
                                                    align={column.align}
                                                >
                                                    {row[column.id]}
                                                </TableCell>
                                            );
                                        })}
                                    </TableRow>
                                );
                            })}
                        </TableBody>
                    </Table>
                </TableContainer>
            </InfiniteScroll>
        </React.Fragment>
    );
};

export default InvocationTable;
