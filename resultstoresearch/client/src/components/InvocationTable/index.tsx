// InvocationTable Component
/**
 * Component that renders invocations data and information in a table
 * @packageDocumentation
 */
import React, { useRef, useState, useEffect } from 'react';
import clsx from 'clsx';
import {
    ColumnProps,
    TableCellRenderer,
    RowMouseEventHandlerParams,
    defaultTableRowRenderer,
    TableRowProps,
} from 'react-virtualized';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import { InvocationTableProps, ModalState, HoverState } from './types';
import { parseInvocationTableData } from './utils';
import FileModal from './FileModal';
import InfiniteTable from '../InfiniteTable';
import LoadingRow from '../InfiniteTable/BaseTable/LoadingRow';
import FileButton from './FileButton';
import StatusIcon from '../StatusIcon';

const HeaderHeight = 60;
const RowHeight = 48;

const Container = styled(Paper)`
    width: 91.5%;
    height: calc(98vh - 120px);
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    outline: none;
`;

const FileCell = styled.div`
    height: ${RowHeight - 1}px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 1px solid rgba(224, 224, 224, 1);
`;

const StatusCell = styled.div`
    height: ${RowHeight - 1}px;
    width: 100%;
    border-bottom: 1px solid rgba(224, 224, 224, 1);
    margin-left: 5px;
`;

const StatusContainer = styled.div`
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
`;

const IconStyle: React.CSSProperties = { marginRight: '3px' };

/**
 *
 * @param fileRenderer function to open file modal button
 * @param statusCellRenderer function to render status cell button
 */
export const createColumns = (
    fileRenderer: TableCellRenderer,
    statusCellRenderer: TableCellRenderer
) => {
    const columns: ColumnProps[] = [
        {
            dataKey: 'status',
            label: 'Status',
            width: 150,
            cellRenderer: statusCellRenderer,
        },
        { dataKey: 'name', label: 'Name', width: 400 },
        { dataKey: 'labels', label: 'Labels', width: 120 },
        { dataKey: 'date', label: 'Run Date', width: 200 },
        { dataKey: 'duration', label: 'Duration', width: 120 },
        { dataKey: 'user', label: 'User', width: 400 },
        {
            dataKey: 'files',
            label: '',
            width: 100,
            cellRenderer: fileRenderer,
            flexGrow: 0,
        },
    ];
    return columns;
};

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

/** InvocationTable Component */
export const InvocationTable: React.FC<InvocationTableProps> = ({
    invocations,
    pageToken,
    next,
    isNextPageLoading,
}) => {
    const classes = useStyles();
    const [hoverState, setHoverState] = useState<HoverState>({
        isHovered: false,
        rowIndex: -1,
    });
    const containerRef = useRef<HTMLDivElement>(null);
    const [modalState, setModalState] = useState<ModalState>({
        isOpen: false,
        index: 0,
    });
    const closeModal = () => {
        setModalState({
            isOpen: false,
            index: 0,
        });
    };
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

    const cellClass = clsx(classes.tableCell, classes.flexContainer);
    const headerClass = clsx(
        classes.tableCell,
        classes.flexContainer,
        classes.tableHeader
    );

    const rowGetter = ({ index }) => {
        if (!isRowLoaded({ index })) {
            return {};
        }
        return rows[index];
    };

    const onRowClick = ({ index }: RowMouseEventHandlerParams) => {
        window.open(
            `https://source.cloud.google.com/results/${invocations[
                index
            ].getName()}`
        );
        return false;
    };

    const getFiles = () => {
        if (invocations.length > 0) {
            return invocations[modalState.index].getFilesList();
        }
        return [];
    };

    const getParent = () => {
        if (invocations.length > 0) {
            return invocations[modalState.index].getName();
        }
        return '';
    };

    const fileCellRenderer: TableCellRenderer = ({ rowIndex }) => {
        const openFileModal = (index: number, event: React.MouseEvent) => {
            event.stopPropagation();
            setModalState({
                isOpen: true,
                index: index,
            });
        };

        const showFileButton = () => {
            return hoverState.isHovered && rowIndex === hoverState.rowIndex;
        };

        return (
            <FileCell>
                <FileButton
                    isVisible={showFileButton()}
                    id={`FileButton-${rowIndex}`}
                    onClick={(e) => openFileModal(rowIndex, e)}
                />
            </FileCell>
        );
    };

    const statusCellRenderer: TableCellRenderer = ({ rowData }) => {
        return (
            <StatusCell>
                <StatusContainer>
                    <StatusIcon name={rowData.status} style={IconStyle} />
                    {rowData.status}
                </StatusContainer>
            </StatusCell>
        );
    };

    const onRowMouseOver = ({ index }: RowMouseEventHandlerParams) => {
        setHoverState({
            isHovered: true,
            rowIndex: index,
        });
    };

    const onRowMouseOut = ({ index }: RowMouseEventHandlerParams) => {
        setHoverState({
            isHovered: false,
            rowIndex: index,
        });
    };

    const columns = createColumns(fileCellRenderer, statusCellRenderer);

    const rowRenderer = (props: TableRowProps) => {
        const { index, key, style } = props;
        if (!isRowLoaded({ index })) {
            return (
                <div key={key} style={style}>
                    <LoadingRow width={width} size={20} />
                </div>
            );
        }
        return defaultTableRowRenderer(props);
    };

    return (
        <Container ref={containerRef} elevation={3} id={'InvocationTable'}>
            <InfiniteTable
                columns={columns}
                width={width}
                height={height}
                rowHeight={RowHeight}
                headerHeight={HeaderHeight}
                rowCount={rowCount}
                rowGetter={rowGetter}
                rowClassName={getRowClassName}
                onRowClick={onRowClick}
                isRowLoaded={isRowLoaded}
                loadMoreRows={loadMoreRows}
                cellClass={cellClass}
                headerClass={headerClass}
                onRowMouseOver={onRowMouseOver}
                onRowMouseOut={onRowMouseOut}
                gridClass={classes.tableGrid}
                isNextPageLoading={isNextPageLoading}
                rowRenderer={rowRenderer}
            />
            <FileModal
                isOpen={modalState.isOpen}
                close={closeModal}
                files={getFiles()}
                parent={getParent()}
            />
        </Container>
    );
};

export default InvocationTable;
