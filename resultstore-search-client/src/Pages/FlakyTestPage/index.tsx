import React, { useState } from 'react';
import styled from 'styled-components';
import { RouteComponentProps } from 'react-router-dom';
import { StaticContext } from 'react-router';
import BackButton from '../../components/BackButton';
import { GetTestCasesResponse } from '../../api/resultstore_download_pb';
import FlakyTestTable from '../../components/FlakyTestTable';
import TestResults, {
    Props as TestResultsProps,
} from '../../components/TestResults';

const AppContainer = styled.div`
    height: 98vh;
    width: 98vw;
    margin: 0 auto 0 auto;
`;

const HeaderContainer = styled.div`
    display: flex;
    width: 91.5%;
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
`;

interface RouterState {
    invocationsTestList: Uint8Array;
}

type FlakyTestState = TestResultsProps;

const FlakyTest = ({
    history,
    location,
}: RouteComponentProps<{}, StaticContext, RouterState>) => {
    const { state } = location;
    const [aggregateTestData, setAggregateTestData] = useState<FlakyTestState>({
        totalTests: 0,
        failedTests: 0,
        passedTests: 0,
    });
    const { totalTests, failedTests, passedTests } = aggregateTestData;
    const backButtonOnClick = () => {
        history.push('/');
    };
    const list = GetTestCasesResponse.deserializeBinary(
        state.invocationsTestList
    );
    return (
        <AppContainer>
            <HeaderContainer>
                <BackButton onClick={backButtonOnClick} />
                <TestResults
                    totalTests={totalTests}
                    failedTests={failedTests}
                    passedTests={passedTests}
                />
            </HeaderContainer>
            <FlakyTestTable
                invocationsTestList={list.getInvocationTestsList()}
                setAggregateTestData={setAggregateTestData}
            />
        </AppContainer>
    );
};

export default FlakyTest;
