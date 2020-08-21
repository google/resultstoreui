import React from 'react';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import {
    Column,
    Table,
    TableCellRenderer,
    TableHeaderProps,
    InfiniteLoaderChildProps,
    TableProps,
} from 'react-virtualized';
import TableCell from '@material-ui/core/TableCell';
import LoadingRow from './LoadingRow';

const FirstLoadingRow = styled(LoadingRow)`
    margin-top: 15px;
`;

export interface SelfProps {
    rowHeight: number;
    headerClass?: string;
    cellClass?: string;
    gridClass?: string;
    isNextPageLoading?: boolean;
}

export type Props = SelfProps &
    Pick<
        TableProps,
        | 'columns'
        | 'width'
        | 'height'
        | 'headerHeight'
        | 'rowCount'
        | 'rowGetter'
        | 'rowClassName'
        | 'onRowClick'
        | 'onRowMouseOver'
        | 'onRowMouseOut'
        | 'rowRenderer'
    > &
    InfiniteLoaderChildProps;

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        flexContainer: {
            display: 'flex',
            alignItems: 'center',
            boxSizing: 'border-box',
        },
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
    headerClass,
    cellClass,
    gridClass,
    onRowMouseOut,
    onRowMouseOver,
    isNextPageLoading = false,
    rowRenderer,
}) => {
    const classes = useStyles();

    const cellRenderer: TableCellRenderer = ({ cellData }) => {
        return (
            <TableCell
                component="div"
                className={cellClass}
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
                className={headerClass}
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
            gridClassName={gridClass}
            headerHeight={headerHeight}
            ref={registerChild}
            rowClassName={rowClassName}
            onRowsRendered={onRowsRendered}
            headerStyle={{ display: 'flex', flexGrow: 1 }}
            rowGetter={rowGetter}
            rowCount={rowCount}
            onRowClick={onRowClick}
            onRowMouseOut={onRowMouseOut}
            onRowMouseOver={onRowMouseOver}
            noRowsRenderer={() =>
                isNextPageLoading && <FirstLoadingRow width={width} size={35} />
            }
            rowRenderer={rowRenderer}
        >
            {columns.map(({ dataKey, width, ...other }) => {
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
                        width={width}
                        {...other}
                    />
                );
            })}
        </Table>
    );
};

export default BaseTable;
