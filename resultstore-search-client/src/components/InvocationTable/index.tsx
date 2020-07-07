import React, { useRef, useState, useEffect } from 'react';
import clsx from 'clsx';
import styled from 'styled-components';
import { makeStyles, Theme, createStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import { InvocationTableProps, ModalState } from './types';
import { parseInvocationTableData } from './utils';
import { ColumnProps } from 'react-virtualized';
import FileModal from './FileModal';
import InfiniteTable from '../InfiniteTable';

const HeaderHeight = 60;
const RowHeight = 48;

const Container = styled(Paper)`
    width: 91.5%;
    height: 90%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    outline: none;
`;

const columns: ColumnProps[] = [
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

/*
Table that displays results of an invocation search
*/
const InvocationTable: React.FC<InvocationTableProps> = ({
    invocations,
    pageToken,
    next,
    isNextPageLoading,
    tokenID,
}) => {
    const classes = useStyles();
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
            return {
                status: 'Loading...',
            };
        }
        return rows[index];
    };

    const onRowClick = ({ index }) => {
        setModalState({
            isOpen: true,
            index: index,
        });
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

    return (
        <Container ref={containerRef} elevation={3}>
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
                gridClass={classes.tableGrid}
            />
            <FileModal
                isOpen={modalState.isOpen}
                close={closeModal}
                files={getFiles()}
                parent={getParent()}
                tokenID={tokenID}
            />
        </Container>
    );
};

export default InvocationTable;
