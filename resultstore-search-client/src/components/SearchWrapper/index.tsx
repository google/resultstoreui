import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import InvocationTable from '../InvocationTable';
import SearchBar, { State as SearchBarState } from './SearchBar';
import { InvocationTableProps } from '../InvocationTable/types';
import ToolSelect, { ToolSelectProps } from './ToolSelect';
import {
    searchInvocations,
    SearchInvocationCallback,
} from '../../api/client/client';
import { toSentenceCase } from '../../utils/utils';
import ErrorText from '../ErrorText';
import GoogleButton from '../GoogleButton';
import { Error } from '../ErrorText';

const SearchContainer = styled.div`
    display: flex;
    width: 92%;
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
`;

const AppContainer = styled.div`
    height: 100vh;
    width: 100vw;
`;

export interface State {
    query: string;
    pageToken: string;
    newQuery: boolean;
    isNextPageLoading: boolean;
    error: Error;
}

export interface Auth {
    tokenID: string;
}

/*
Wrapper around SearchBar and InvocationTable that passes invocations
returned from SearchBar to the InvocationTable to be rendered
*/
const SearchWrapper: React.FC = () => {
    const [tokenID, setTokenID] = useState<Auth['tokenID']>('');
    const [invocations, setInvocations] = useState<
        InvocationTableProps['invocations']
    >([]);
    const [toolsList, setToolsList] = useState<ToolSelectProps['toolsList']>(
        []
    );
    const [selectedTool, setSelectedTool] = useState<
        ToolSelectProps['selectedTool']
    >('');
    const [query, setQuery] = useState<SearchBarState['query']>('');
    const [pageToken, setPageToken] = useState<State['pageToken']>('');
    const [newQuery, setNewQuery] = useState<State['newQuery']>(true);
    const [error, setError] = React.useState<State['error']>({
        errorText: '',
        hasError: false,
    });
    const [isNextPageLoading, setIsNextPageLoading] = React.useState<
        State['isNextPageLoading']
    >(false);

    const nextRows = (newQuery: boolean, pageToken: string) => {
        setIsNextPageLoading(true);
        searchInvocations(
            query,
            newQuery,
            selectedTool,
            pageToken,
            tokenID,
            searchInvocationsCallback
        );
    };

    useEffect(() => {
        if (query !== '') {
            setNewQuery(true);
            setPageToken('');
            nextRows(true, '');
        }
    }, [query]);

    const searchInvocationsCallback: SearchInvocationCallback = (
        err,
        response
    ) => {
        if (err) {
            setError({
                errorText: `${toSentenceCase(err.message)}`,
                hasError: true,
            });
        } else {
            setError({
                errorText: '',
                hasError: false,
            });
            setPageToken(response.getNextPageToken());
            const toolsList = response.getToolsListList();
            if (toolsList && toolsList.length !== 0) {
                setToolsList(toolsList);
            }
            if (newQuery) {
                setNewQuery(false);
                setInvocations(response.getInvocationsList());
            } else {
                setInvocations([
                    ...invocations,
                    ...response.getInvocationsList(),
                ]);
            }
        }
        setIsNextPageLoading(false);
    };

    return (
        <AppContainer>
            <SearchContainer>
                <ToolSelect
                    toolsList={toolsList}
                    setToolsList={setToolsList}
                    selectedTool={selectedTool}
                    setSelectedTool={setSelectedTool}
                />
                <SearchBar
                    setQueryParent={setQuery}
                    hasError={error.hasError}
                />
                <GoogleButton setTokenID={setTokenID} />
            </SearchContainer>
            <ErrorText text={error.errorText} id={'search-error'} />
            <InvocationTable
                invocations={invocations}
                next={nextRows}
                pageToken={pageToken}
                isNextPageLoading={isNextPageLoading}
                tokenID={tokenID}
            />
        </AppContainer>
    );
};

export default SearchWrapper;
