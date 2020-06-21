import React from 'react';
import ScaleLoader from 'react-spinners/ScaleLoader';
import styled from 'styled-components';

const SpinnerContainer = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
`;

const Spinner = () => {
    return (
        <SpinnerContainer>
            <ScaleLoader />
        </SpinnerContainer>
    );
};

export default Spinner;
