// TargetList Component
/**
 * List of targets whose files can be viewed in the FileTable
 * @packageDocumentation
 */
import React, { useState, useEffect, useContext, useRef } from 'react';
import { List, InfiniteLoader } from 'react-virtualized';
import styled from 'styled-components';
import {
    listTargetsRequest,
    ListTargetsCallback,
    listTargetSubFiles,
    ListTargetSubFilesCallback,
} from '../../../../api/client/client';
import * as target_pb from '../../../../api/target_pb';
import * as file_pb from '../../../../api/file_pb';
import { AuthContext } from '../../../../contexts/AuthContext';
import LoadingRow from '../../../InfiniteTable/BaseTable/LoadingRow';

const StyledTargetList = styled(List)`
    outline: none;
`;

export const ListRow = styled.div<{ rowHeight: number }>`
    display: flex;
    padding: 2px 0px 2px 20px;
    box-sizing: border-box;
    cursor: pointer;
    text-overflow: ellipsis;
    height: ${({ rowHeight }) => rowHeight || 30}px;
    width: 100%;
    border-bottom-style: solid;
    border-color: #e0e0e0;
    border-width: 1px;
    :hover {
        background-color: #eeeeee;
    }
`;

/** TargetList State */
interface State {
    targets: Array<target_pb.Target>;
    pageToken: string;
    newQuery: boolean;
    isNextPageLoading: boolean;
}

/** TargetList Props */
interface Props {
    /** Parent invocation name for targets */
    parent: string;
    /** Width of the target list */
    width: number;
    /** Height of the target list */
    height: number;
    /** Height of each row in the target list */
    rowHeight: number;
    /** Callback called on each row click */
    onClick: (
        name: string,
        files: Array<file_pb.File>,
        isLoadingTableRows: boolean
    ) => void;
}

/** TargetList Component */
export const TargetList: React.FC<Props> = ({
    parent,
    width,
    height,
    rowHeight,
    onClick,
}) => {
    const authContext = useContext(AuthContext);
    const listRef = useRef(null);
    const bindListRef = (ref) => {
        listRef.current = ref;
    };
    const [targets, setTargets] = useState<State['targets']>([]);
    const [pageToken, setPageToken] = useState<State['pageToken']>('');
    const [isNextPageLoading, setIsNextPageLoading] = React.useState<
        State['isNextPageLoading']
    >(false);
    const hasNextPage = pageToken !== '';
    const rowCount = hasNextPage ? targets.length + 1 : targets.length;
    const isRowLoaded = ({ index }) => {
        return !!targets[index];
    };

    const rowRenderer = ({ key, index, style }) => {
        if (!isRowLoaded({ index })) {
            return (
                <div key={key} style={style}>
                    <LoadingRow width={width} size={20} />
                </div>
            );
        }
        const targetName = targets[index].getId().getTargetId();
        const filesCallback: ListTargetSubFilesCallback = (err, response) => {
            if (err) {
                console.error(err);
            } else {
                onClick(
                    `${parent.slice(12)}/${targetName}`,
                    targets[index]
                        .getFilesList()
                        .concat(response.getFilesList()),
                    false
                );
            }
        };

        return (
            <ListRow
                key={key}
                rowHeight={rowHeight}
                style={style}
                onClick={() => {
                    onClick(
                        `${parent.slice(12)}/${targetName}`,
                        targets[index].getFilesList(),
                        true
                    );
                    listTargetSubFiles(
                        targets[index].getName(),
                        authContext.tokenId,
                        filesCallback
                    );
                }}
            >
                {targetName}
            </ListRow>
        );
    };

    const targetsCallback: ListTargetsCallback = (err, response, newQuery) => {
        if (err) {
            setIsNextPageLoading(false);
            console.error(err);
        } else {
            setPageToken(response.getNextPageToken());
            setIsNextPageLoading(false);
            if (newQuery) {
                setTargets(response.getTargetsList());
            } else {
                setTargets([...targets, ...response.getTargetsList()]);
            }
        }
        console.log(rowCount);
    };

    const loadMoreRows: any = isNextPageLoading ? () => {} : () => nextRows();

    const nextRows = () => {
        setIsNextPageLoading(true);
        listTargetsRequest(
            targets.length === 0 || targets.length === 1,
            parent,
            pageToken,
            authContext.tokenId,
            targetsCallback
        );
    };

    useEffect(() => nextRows(), []);
    useEffect(() => {
        if (listRef.current) {
            listRef.current.forceUpdateGrid();
        }
    }, [listRef.current, targets]);

    return (
        <InfiniteLoader
            isRowLoaded={isRowLoaded}
            loadMoreRows={loadMoreRows}
            rowCount={rowCount}
            threshold={1}
        >
            {({ onRowsRendered, registerChild }) => (
                <StyledTargetList
                    ref={bindListRef}
                    rowCount={rowCount}
                    width={width}
                    height={height}
                    rowHeight={rowHeight}
                    rowRenderer={rowRenderer}
                    onRowsRendered={onRowsRendered}
                    registerChild={registerChild}
                />
            )}
        </InfiniteLoader>
    );
};

export default TargetList;
