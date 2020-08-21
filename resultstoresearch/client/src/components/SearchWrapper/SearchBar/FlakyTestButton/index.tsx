// FlakyTestButton Component
/**
 * Button that initiates query and redirects to a flaky test page
 * @packageDocumentation
 */
import React from 'react';
import styled from 'styled-components';
import Button from '@material-ui/core/Button';
import DirectionsRunIcon from '@material-ui/icons/DirectionsRun';
import CircularProgress from '@material-ui/core/CircularProgress';

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

const TableSpinner = styled(CircularProgress)`
    color: #6e6e6e !important;
`;

/** FlakyTestButton Props */
interface Props {
    /** Callback fired on click*/
    onClick: () => void;
    /** Disabled if true */
    disabled: boolean;
    /** Show spinner if true */
    showSpinner: boolean;
}

/** FlakyTestButton Component */
export const FlakyTestButton: React.FC<Props> = ({
    onClick,
    disabled,
    showSpinner,
}) => {
    return (
        <ButtonContainer
            variant="outlined"
            onClick={onClick}
            title={'Flaky Tests'}
            disabled={disabled}
        >
            {showSpinner && <TableSpinner size={25} />}
            {!showSpinner && <DirectionsRunIcon />}
            <TextContainer>{'Flaky '}</TextContainer>
        </ButtonContainer>
    );
};
export default FlakyTestButton;
