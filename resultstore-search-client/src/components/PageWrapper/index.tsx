import React, { useState } from 'react';
import styled from 'styled-components';
import InvocationTable from '../InvocationTable';
import SearchBar from '../SearchBar';
import { InvocationTableProps } from '../InvocationTable/types';
import ToolSelect, { ToolSelectProps } from '../ToolSelect';

const SearchContainer = styled.div`
    display: flex;
`;

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
                    setInvocations={setInvocations}
                    tool={selectedTool}
                    setToolsList={setToolsList}
                />
            </SearchContainer>
            <InvocationTable invocations={invocations} />
        </div>
    );
};

export default PageWrapper;
