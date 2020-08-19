// FileTable Component
/**
 * Table to render files and their information.
 * Opens a new page with file contents on row click
 * @packageDocumentation
 */
import React, { useRef } from 'react';
import { ColumnProps, AutoSizer } from 'react-virtualized';
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

/** Data rendered by the file table */
export interface Data {
    name: string;
    type: string;
    size: number;
}

/** FileTable Props */
interface Props {
    /** Currently selected resource's name whose files are viewable*/
    selectedName: string;
    /** Currently selected resource's type whose files are viewable*/
    selectedType: string;
    /** Array of files to be rendered in the table */
    files: Array<file_pb.File>;
    /** Table rows are being loaded if true */
    isLoadingTableRows: boolean;
}

/**
 *
 * @param file File whose information will be parsed into table readable data
 */
const parseFileTableData = (file: file_pb.File): Data => {
    const name = file.getUid();
    const type = file.getContentType();
    const size = file.getLength().getValue();
    return { name, type, size };
};

/** FileTable Component */
export const FileTable: React.FC<Props> = ({
    files,
    selectedName,
    isLoadingTableRows,
}) => {
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
                        isNextPageLoading={isLoadingTableRows}
                    />
                )}
            </AutoSizer>
        </TableContainer>
    );
};

export default FileTable;
