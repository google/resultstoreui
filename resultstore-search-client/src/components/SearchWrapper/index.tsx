import React, { useState, useEffect, useContext } from 'react';
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
import { AuthContext } from '../../contexts/AuthContext';

const SearchContainer = styled.div`
    display: flex;
    width: 92%;
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
`;

const AppContainer = styled.div`
    height: 98vh;
    width: 98vw;
    margin: 0 auto 0 auto;
`;

export interface State {
    query: string;
    pageToken: string;
    newQuery: boolean;
    isNextPageLoading: boolean;
    error: Error;
}

/*
Wrapper around SearchBar and InvocationTable that passes invocations
returned from SearchBar to the InvocationTable to be rendered
*/
const SearchWrapper: React.FC = () => {
    const authContext = useContext(AuthContext);
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
            authContext.tokenId,
            searchInvocationsCallback
        );
    };

    useEffect(() => {
        if (query !== '') {
            setPageToken('');
            nextRows(true, '');
        }
    }, [query]);

    const searchInvocationsCallback: SearchInvocationCallback = (
        err,
        response,
        newQuery
    ) => {
        if (err) {
            setIsNextPageLoading(false);
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
            setIsNextPageLoading(false);
            const toolsList = response.getToolsListList();
            if (toolsList && toolsList.length !== 0) {
                setToolsList(toolsList);
            }
            if (newQuery) {
                setInvocations(response.getInvocationsList());
            } else {
                setInvocations([
                    ...invocations,
                    ...response.getInvocationsList(),
                ]);
            }
        }
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
                    loading={isNextPageLoading && pageToken === ''}
                />
                <GoogleButton />
            </SearchContainer>
            <ErrorText text={error.errorText} id={'search-error'} />
            <InvocationTable
                invocations={invocations}
                next={nextRows}
                pageToken={pageToken}
                isNextPageLoading={isNextPageLoading}
                tokenID={authContext.tokenId}
            />
        </AppContainer>
    );
};

export default SearchWrapper;
