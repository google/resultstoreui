import React from 'react';
import styled from 'styled-components';
import Button from '@material-ui/core/Button';
import DirectionsRunIcon from '@material-ui/icons/DirectionsRun';

const ButtonContainer = styled(Button)`
    height: 56px;
    margin-right: 8px !important;
    margin-top: auto !important;
    margin-bottom: auto !important;
    text-transform: none !important;
    font-size: 17px !important;
`;

const TextContainer = styled.span`
    margin-left: 4px;
`;

interface Props {
    onClick: () => void;
    disabled: boolean;
}

const FlakyTestButton: React.FC<Props> = ({ onClick, disabled }) => {
    return (
        <ButtonContainer
            variant="outlined"
            onClick={onClick}
            title={'Flaky Tests'}
            disabled={disabled}
        >
            <DirectionsRunIcon />
            <TextContainer>{'Flaky '}</TextContainer>
        </ButtonContainer>
    );
};
export default FlakyTestButton;
