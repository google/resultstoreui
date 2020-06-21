import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import InvocationTable from '../InvocationTable';
import SearchBar, {
    State as SearchBarState,
    SearchBarProps,
} from './SearchBar';
import { InvocationTableProps } from '../InvocationTable/types';
import ToolSelect, { ToolSelectProps } from './ToolSelect';
import {
    searchInvocations,
    SearchInvocationCallback,
} from '../../api/client/client';
import { toSentenceCase } from '../../utils/utils';

const SearchContainer = styled.div`
    display: flex;
`;

export interface State {
    query: string;
    pageToken: string;
    newQuery: boolean;
}

/*
Wrapper around SearchBar and InvocationTable that passes invocations
returned from SearchBar to the InvocationTable to be rendered
*/
const PageWrapper: React.FC = () => {
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
    const [errorText, setErrorText] = React.useState<
        SearchBarProps['errorText']
    >('');
    const [hasError, setHasError] = React.useState<SearchBarProps['hasError']>(
        false
    );

    const updateError = (error: string, hasError: boolean) => {
        setHasError(hasError);
        setErrorText(error);
    };

    const nextRows = (newQuery: boolean, pageToken: string) => {
        searchInvocations(
            query,
            newQuery,
            selectedTool,
            pageToken,
            searchInvocationsCallback
        );
    };

    useEffect(() => {
        if (query !== '') {
            setNewQuery(true);
            setPageToken('');
            nextRows(true, '');
        }
    }, [selectedTool, query]);

    const searchInvocationsCallback: SearchInvocationCallback = (
        err,
        response
    ) => {
        if (err) {
            updateError(`${toSentenceCase(err.message)}.`, true);
        } else {
            updateError('', false);
            setPageToken(response.getNextPageToken());
            const toolsList = response.getToolsListList();
            if (toolsList && toolsList.length !== 0) {
                setToolsList(toolsList);
            }
            if (newQuery) {
                setInvocations(response.getInvocationsList());
                setNewQuery(false);
            } else {
                setInvocations([
                    ...invocations,
                    ...response.getInvocationsList(),
                ]);
            }
        }
    };

    return (
        <div>
            <SearchContainer>
                <ToolSelect
                    toolsList={toolsList}
                    setToolsList={setToolsList}
                    selectedTool={selectedTool}
                    setSelectedTool={setSelectedTool}
                />
                <SearchBar
                    setQueryParent={setQuery}
                    errorText={errorText}
                    hasError={hasError}
                />
            </SearchContainer>
            <InvocationTable
                invocations={invocations}
                next={nextRows}
                pageToken={pageToken}
            />
        </div>
    );
};

export default PageWrapper;
