import React from 'react';
import styled from 'styled-components';
import Typography from '@material-ui/core/Typography';
import TestCard from './TestCard';
import StatusIcon from '../StatusIcon';

const TestResultsContainer = styled.div`
    display: flex;
    margin: 0 auto 0 auto;
`;

const TextContainer = styled(Typography)`
    font-weight: bold !important;
    margin-right: 6px !important;
    font-size: 19px !important;
`;

export interface Props {
    totalTests: number;
    failedTests: number;
    passedTests: number;
}

const TestResults: React.FC<Props> = ({
    totalTests,
    failedTests,
    passedTests,
}) => {
    return (
        <TestResultsContainer>
            <TestCard numberTests={totalTests}>
                <TextContainer>Total</TextContainer>
                <StatusIcon name={'BUILDING'} />
            </TestCard>
            <TestCard numberTests={passedTests}>
                <TextContainer>Passed</TextContainer>
                <StatusIcon name={'PASS'} />
            </TestCard>
            <TestCard numberTests={failedTests}>
                <TextContainer>Failed</TextContainer>
                <StatusIcon name={'FAILED'} />
            </TestCard>
        </TestResultsContainer>
    );
};

export default TestResults;
