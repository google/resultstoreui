import React, { useRef, useState, useEffect } from 'react';
import { ColumnProps, TableProps } from 'react-virtualized';
import clsx from 'clsx';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import BaseTable from '../../../InfiniteTable/BaseTable';
import * as file_pb from '../../../../api/file_pb';
import { getFile } from '../../../../api/client/client';

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
        },
        tableRowHover: {
            '&:hover': {
                backgroundColor: theme.palette.grey[200],
            },
        },
        tableCell: {
            flex: 1,
        },
        tableGrid: {
            outline: 'none',
        },
        tableHeader: {
            fontWeight: 550,
            fontSize: 16,
        },
    })
);

const columns: ColumnProps[] = [
    { dataKey: 'name', label: 'Artifact Name', width: 120 },
    { dataKey: 'type', label: 'Type', width: 50 },
    { dataKey: 'size', label: 'File Size', width: 20 },
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
    tokenID: string;
}

type Dimensions = Pick<TableProps, 'width' | 'height'>;

const parseFileTableData = (file: file_pb.File): Data => {
    const name = file.getUid();
    const type = file.getContentType();
    const size = file.getLength().getValue();
    return { name, type, size };
};

const FileTable: React.FC<Props> = ({ files, tokenID }) => {
    const classes = useStyles();
    const [dimensions, setDimensions] = useState<Dimensions>({
        width: 1920,
        height: 1080,
    });
    const { width, height } = dimensions;
    const rows = files
        .filter((file) => !file.getHidden())
        .map((file) => parseFileTableData(file));
    const ref = useRef<HTMLDivElement>();

    const setRefDimensions = () => {
        console.log(ref.current ? ref.current.offsetWidth : 0);
        setDimensions({
            width: ref.current ? ref.current.offsetWidth : 1920,
            height: ref.current ? ref.current.offsetHeight : 1080,
        });
    };

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

    useEffect(() => {
        setRefDimensions();
    }, [ref]);

    useEffect(() => {
        setRefDimensions();
        window.addEventListener('resize', setRefDimensions);
        return () => window.removeEventListener('resize', setRefDimensions);
    }, []);

    const onRowClickCallback = (file: file_pb.File, fileData: string) => {};

    return (
        <TableContainer ref={ref}>
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
                    console.log(index);
                    getFile(files[index], tokenID, onRowClickCallback);
                }}
                headerClass={headerClass}
                cellClass={cellClass}
                rowClassName={getRowClassName}
                gridClass={classes.tableGrid}
            />
        </TableContainer>
    );
};

export default FileTable;
