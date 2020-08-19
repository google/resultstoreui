// BackButton Component
/**
 * Component that allows users to navigte to previous page on click
 * @packageDocumentation
 */
import React from 'react';
import styled from 'styled-components';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';
import Button from '@material-ui/core/Button';

const ButtonContainer = styled(Button)`
    height: 55px !important;
    width: 55px !important;
    margin-right: 8px !important;
    margin-top: auto !important;
    margin-bottom: auto !important;
    text-transform: none !important;
    font-size: 17px !important;
`;

/** BackButton Props */
interface Props {
    /** Callback fired on button click */
    onClick: () => void;
}

/** BackButton Component */
export const BackButton: React.FC<Props> = ({ onClick }) => {
    return (
        <ButtonContainer variant="outlined" onClick={onClick}>
            <ArrowBackIcon />
        </ButtonContainer>
    );
};

export default BackButton;
