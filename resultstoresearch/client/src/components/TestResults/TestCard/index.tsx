// TestCard Component
/**
 * Card to display individual aggregate test results
 * @packageDocumentation
 */
import React from 'react';
import Card from '@material-ui/core/Card';
import styled from 'styled-components';

const CardContainer = styled(Card)`
    display: flex;
    flex: 1;
    margin: auto 5px auto 5px;
    height: 55px;
    width: 175px;
    align-items: center;
    justify-content: center;
    font-weight: bold;
`;

const TextContainer = styled.div<{ flex: number }>`
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: left;
    font-weight: bold;
    margin: auto 15px auto 10px;
`;

const NumberContainer = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 19px;
    margin: auto 15px auto 0px;
`;

/** TestCard Props */
interface Props {
    /** Total number of tests */
    numberTests: number;
}

/** TestCard Component */
const TestCard: React.FC<Props> = ({ children, numberTests }) => {
    return (
        <CardContainer>
            <TextContainer>{children}</TextContainer>
            <NumberContainer>{numberTests}</NumberContainer>
        </CardContainer>
    );
};

export default TestCard;
