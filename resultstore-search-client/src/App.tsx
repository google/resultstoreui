import React from 'react';
import SearchBar from './components/SearchBar';
import InvocationTable from './components/InvocationTable'
import * as invocation_pb from './api/invocation_pb';

interface State {
    invocations: Array<invocation_pb.Invocation>;
}

function App() {
    const [invocations, setInvocations] = React.useState<State['invocations']>([]);
    return (
        <React.Fragment>
            <SearchBar setInvocations={setInvocations}/>
            <InvocationTable invocations={invocations}/>
        </React.Fragment>
    )
}

export default App;
