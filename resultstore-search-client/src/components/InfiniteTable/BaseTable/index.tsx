import React from 'react';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import {
    ColumnProps,
    Column,
    Table,
    TableCellRenderer,
    TableHeaderProps,
    InfiniteLoaderChildProps,
    TableProps,
} from 'react-virtualized';
import clsx from 'clsx';
import TableCell from '@material-ui/core/TableCell';

export interface SelfProps {
    columns: Array<ColumnProps>;
    rowHeight: number;
    headerHeight: number;
}

export type Props = SelfProps & InfiniteLoaderChildProps & TableProps;

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

const BaseTable: React.FC<Props> = ({
    columns,
    width,
    height,
    rowHeight,
    headerHeight,
    onRowsRendered,
    registerChild,
    rowCount,
    rowGetter,
    rowClassName,
    onRowClick,
}) => {
    const classes = useStyles();

    const cellRenderer: TableCellRenderer = ({ cellData }) => {
        return (
            <TableCell
                component="div"
                className={clsx(classes.tableCell, classes.flexContainer)}
                variant="body"
                style={{ height: rowHeight }}
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
                style={{ height: headerHeight }}
                align={'center'}
            >
                <span>{label}</span>
            </TableCell>
        );
    };
    return (
        <Table
            height={height}
            width={width}
            rowHeight={48}
            gridStyle={{
                direction: 'inherit',
            }}
            className={classes.table}
            headerHeight={headerHeight}
            ref={registerChild}
            rowClassName={rowClassName}
            onRowsRendered={onRowsRendered}
            headerStyle={{ display: 'flex', flexGrow: 1 }}
            rowGetter={rowGetter}
            rowCount={rowCount}
            onRowClick={onRowClick}
        >
            {columns.map(({ dataKey, ...other }) => {
                return (
                    <Column
                        key={dataKey}
                        headerRenderer={(headerProps) =>
                            headerRenderer({
                                ...headerProps,
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
    );
};

export default BaseTable;
