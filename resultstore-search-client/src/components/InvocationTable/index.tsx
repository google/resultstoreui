import React, { useRef, useState, useEffect } from 'react';
import clsx from 'clsx';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import TableCell from '@material-ui/core/TableCell';
import { InvocationTableProps } from './types';
import { parseInvocationTableData } from './utils';
import {
    Column,
    Table,
    InfiniteLoader,
    TableCellRenderer,
    TableHeaderProps,
} from 'react-virtualized';

const HeaderHeight = 60;
const RowHeight = 48;

const Container = styled(Paper)`
    width: 91.5%;
    height: 90%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
`;

const columns: Column[] = [
    { dataKey: 'status', label: 'Status', width: 120 },
    { dataKey: 'name', label: 'Name', width: 400 },
    { dataKey: 'labels', label: 'Labels', width: 120 },
    { dataKey: 'date', label: 'Run Date', width: 200 },
    { dataKey: 'duration', label: 'Duration', width: 120 },
    { dataKey: 'user', label: 'User', width: 400 },
];

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        flexContainer: {
            display: 'flex',
            alignItems: 'center',
            boxSizing: 'border-box',
        },
        tableRow: {
            cursor: 'pointer',
        },
        tableRowHover: {
            '&:hover': {
                backgroundColor: theme.palette.grey[200],
            },
        },
        tableCell: {
            flex: 1,
        },
        table: {},
    })
);

/*
Table that displays results of an invocation search
*/
const InvocationTable: React.FC<InvocationTableProps> = ({
    invocations,
    pageToken,
    next,
    isNextPageLoading,
}) => {
    const classes = useStyles();
    const containerRef = useRef<HTMLDivElement>(null);
    const [width, setWidth] = useState(1920);
    const [height, setHeight] = useState(1080);
    const rows = invocations.map((invocation) =>
        parseInvocationTableData(invocation)
    );
    const hasNextPage = pageToken !== '';
    const isRowLoaded = ({ index }) => !hasNextPage || index < rows.length;
    const rowCount = hasNextPage ? rows.length + 1 : rows.length;
    const loadMoreRows = isNextPageLoading
        ? () => {}
        : () => next(false, pageToken);

    const setDimensions = () => {
        setWidth(
            containerRef.current ? containerRef.current.offsetWidth : 1920
        );
        setHeight(
            containerRef.current ? containerRef.current.offsetHeight : 1080
        );
    };

    useEffect(() => {
        setDimensions();
    }, [containerRef]);

    useEffect(() => {
        window.addEventListener('resize', setDimensions);
        return () => window.removeEventListener('resize', setDimensions);
    }, []);

    const getRowClassName = ({ index }) => {
        return clsx(classes.tableRow, classes.flexContainer, {
            [classes.tableRowHover]: index !== -1,
        });
    };

    const rowGetter = ({ index }) => {
        if (!isRowLoaded({ index })) {
            return {
                status: 'Loading...',
            };
        }
        return rows[index];
    };

    const cellRenderer: TableCellRenderer = ({ cellData }) => {
        return (
            <TableCell
                component="div"
                className={clsx(classes.tableCell, classes.flexContainer)}
                variant="body"
                style={{ height: RowHeight }}
                align={'left'}
            >
                {cellData}
            </TableCell>
        );
    };

    const headerRenderer = ({ label }: TableHeaderProps) => {
        return (
            <TableCell
                component="div"
                className={clsx(classes.tableCell, classes.flexContainer)}
                variant="head"
                style={{ height: HeaderHeight }}
                align={'center'}
            >
                <span>{label}</span>
            </TableCell>
        );
    };

    return (
        <Container ref={containerRef} elevation={3}>
            <InfiniteLoader
                isRowLoaded={isRowLoaded}
                loadMoreRows={loadMoreRows}
                rowCount={rowCount}
                threshold={15}
            >
                {({ onRowsRendered, registerChild }) => (
                    <Table
                        height={height}
                        width={width}
                        rowHeight={48}
                        gridStyle={{
                            direction: 'inherit',
                        }}
                        className={classes.table}
                        headerHeight={HeaderHeight}
                        ref={registerChild}
                        rowClassName={getRowClassName}
                        onRowsRendered={onRowsRendered}
                        headerStyle={{ display: 'flex', flexGrow: 1 }}
                        rowGetter={rowGetter}
                        rowCount={rowCount}
                    >
                        {columns.map(({ dataKey, ...other }, index) => {
                            return (
                                <Column
                                    key={dataKey}
                                    headerRenderer={(headerProps) =>
                                        headerRenderer({
                                            ...headerProps,
                                            columnIndex: index,
                                        })
                                    }
                                    className={classes.flexContainer}
                                    cellRenderer={cellRenderer}
                                    dataKey={dataKey}
                                    flexGrow={1}
                                    {...other}
                                />
                            );
                        })}
                    </Table>
                )}
            </InfiniteLoader>
        </Container>
    );
};

export default InvocationTable;
