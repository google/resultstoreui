import React, { useRef, useState, useEffect } from 'react';
import { ColumnProps, TableProps, AutoSizer } from 'react-virtualized';
import clsx from 'clsx';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import BaseTable from '../../../InfiniteTable/BaseTable';
import * as file_pb from '../../../../api/file_pb';

const TableContainer = styled.div`
    width: 100%;
    height: 100%;
    flex: 1;
`;

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        flexContainer: {
            display: 'flex',
            alignItems: 'center',
            boxSizing: 'border-box',
        },
        tableRow: {
            cursor: 'pointer',
            outline: 'none',
            minWidth: '0px',
            flexGrow: 1,
        },
        tableRowHover: {
            '&:hover': {
                backgroundColor: theme.palette.grey[200],
            },
        },
        tableCell: {
            flexGrow: 1,
        },
        tableHeader: {
            fontWeight: 550,
            fontSize: 16,
        },
    })
);

const columns: ColumnProps[] = [
    { dataKey: 'name', label: 'Artifact Name', width: 400 },
    { dataKey: 'type', label: 'Type', width: 100 },
    { dataKey: 'size', label: 'File Size', width: 100 },
];

export interface Data {
    name: string;
    type: string;
    size: number;
}

interface Props {
    selectedName: string;
    selectedType: string;
    files: Array<file_pb.File>;
}

const parseFileTableData = (file: file_pb.File): Data => {
    const name = file.getUid();
    const type = file.getContentType();
    const size = file.getLength().getValue();
    return { name, type, size };
};

const FileTable: React.FC<Props> = ({ files, selectedName }) => {
    const classes = useStyles();
    const rows = files
        .filter((file) => !file.getHidden())
        .map((file) => parseFileTableData(file));
    const ref = useRef<HTMLDivElement>();

    const cellClass = clsx(classes.tableCell, classes.flexContainer);
    const headerClass = clsx(
        classes.tableCell,
        classes.flexContainer,
        classes.tableHeader
    );
    const getRowClassName = ({ index }) => {
        return clsx(classes.tableRow, classes.flexContainer, {
            [classes.tableRowHover]: index !== -1,
        });
    };

    const getFileURL = (fileUid: string) => {
        return (
            window.location.origin +
            `/file?prefix=${selectedName}&fileName=${fileUid}`
        );
    };

    return (
        <TableContainer ref={ref} id={'FileTable'}>
            <AutoSizer>
                {({ height, width }) => (
                    <BaseTable
                        columns={columns}
                        width={width}
                        height={height}
                        rowHeight={48}
                        headerHeight={48}
                        rowCount={files.length}
                        onRowsRendered={() => {}}
                        registerChild={null}
                        rowGetter={({ index }) => rows[index]}
                        onRowClick={({ index }) => {
                            window.open(
                                getFileURL(files[index].getUid()),
                                '_blank'
                            );
                        }}
                        headerClass={headerClass}
                        cellClass={cellClass}
                        rowClassName={getRowClassName}
                    />
                )}
            </AutoSizer>
        </TableContainer>
    );
};

export default FileTable;
