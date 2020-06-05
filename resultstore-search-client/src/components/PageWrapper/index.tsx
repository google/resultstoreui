import React from 'react';
import InvocationTable from '../InvocationTable';
import SearchBar from '../SearchBar';
import { InvocationTableProps } from '../InvocationTable/types';

/*
Wrapper around SearchBar and InvocationTable that passes invocations
returned from SearchBar to the InvocationTable to be rendered
*/
const PageWrapper: React.FC = () => {
    const [invocations, setInvocations] = React.useState<
        InvocationTableProps['invocations']
    >([]);
    return (
        <div>
            <SearchBar setInvocations={setInvocations} />
            <InvocationTable invocations={invocations} />
        </div>
    );
};

export default PageWrapper;
