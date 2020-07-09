import React, { useState, useEffect } from 'react';
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

const StyledTargetList = styled(List)`
    outline: none;
`;

export const ListRow = styled.div`
    display: flex;
    padding: 2px 0px 2px 20px;
    box-sizing: border-box;
    cursor: pointer;
    text-overflow: ellipsis;
    height: 30px;
    width: 100%;
    border-bottom-style: solid;
    border-color: #e0e0e0;
    border-width: 1px;
    :hover {
        background-color: #eeeeee;
    }
`;

interface State {
    targets: Array<target_pb.Target>;
    pageToken: string;
    newQuery: boolean;
}

interface SelfProps {
    parent: string;
    tokenID: string;
    width: number;
    height: number;
    rowHeight: number;
    onClick: (name: string, files: Array<file_pb.File>) => void;
}

type Props = SelfProps;

const TargetList: React.FC<Props> = ({
    parent,
    tokenID,
    width,
    height,
    rowHeight,
    onClick,
}) => {
    const [targets, setTargets] = useState<State['targets']>([]);
    const [pageToken, setPageToken] = useState<State['pageToken']>('');
    const [newQuery, setNewQuery] = useState<State['newQuery']>(true);

    const isRowLoaded = ({ index }) => {
        return !!targets[index];
    };

    const rowRenderer = ({ key, index }) => {
        const targetName = targets[index].getName().split('targets/')[1];

        const filesCallback: ListTargetSubFilesCallback = (err, response) => {
            if (err) {
                console.log(err);
            } else {
                onClick(
                    targetName,
                    targets[index]
                        .getFilesList()
                        .concat(response.getFilesList())
                );
            }
        };

        return (
            <ListRow
                key={key}
                onClick={() => {
                    onClick(targetName, targets[index].getFilesList());
                    listTargetSubFiles(
                        targets[index].getName(),
                        tokenID,
                        filesCallback
                    );
                }}
            >
                {targetName}
            </ListRow>
        );
    };

    const targetsCallback: ListTargetsCallback = (err, response) => {
        if (err) {
            console.log(err);
        } else {
            setPageToken(response.getNextPageToken());
            if (newQuery) {
                setTargets(response.getTargetsList());
                setNewQuery(false);
            } else {
                setTargets([...targets, ...response.getTargetsList()]);
            }
        }
    };

    const loadMoreRows: any = () => {
        listTargetsRequest(
            newQuery,
            parent,
            pageToken,
            tokenID,
            targetsCallback
        );
    };

    useEffect(() => {
        listTargetsRequest(
            newQuery,
            parent,
            pageToken,
            tokenID,
            targetsCallback
        );
    }, []);

    return (
        <InfiniteLoader
            isRowLoaded={isRowLoaded}
            loadMoreRows={loadMoreRows}
            rowCount={targets.length}
        >
            {({ onRowsRendered, registerChild }) => (
                <StyledTargetList
                    rowCount={targets.length}
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
