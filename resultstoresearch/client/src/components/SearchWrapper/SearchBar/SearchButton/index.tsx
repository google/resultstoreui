// SearchButton Component
/**
 * Button that initiates invocation search
 * @packageDocumentation
 */
import React from 'react';
import styled from 'styled-components';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import Search from '@material-ui/icons/Search';

const SearchButtonContainer = styled(Button)`
    height: 56px;
    margin-right: 8px !important;
    margin-top: auto !important;
    margin-bottom: auto !important;
    text-transform: none !important;
    font-size: 17px !important;
`;

const TableSpinner = styled(CircularProgress)`
    color: #6e6e6e !important;
`;

const SearchIcon = styled(Search)`
    color: #6e6e6e !important;
    font-size: 25px !important;
`;

const TextContainer = styled.span`
    margin-left: 4px;
`;

/** SearchButton Props */
interface Props {
    /** Show spinner if true */
    showSpinner: boolean;
    /** Size of spinner svg */
    size?: number;
    /** Callback fired on click */
    onClick?: () => void;
    /** Disabled if true */
    disabled?: boolean;
}

/** SearchButton Components */
export const SearchButton: React.FC<Props> = ({
    showSpinner,
    size = 25,
    onClick,
    disabled,
}) => {
    return (
        <SearchButtonContainer
            variant="outlined"
            onClick={onClick}
            title={'Search'}
            disabled={disabled}
        >
            {showSpinner && <TableSpinner size={size} />}
            {!showSpinner && <SearchIcon />}
            <TextContainer>{'Search'}</TextContainer>
        </SearchButtonContainer>
    );
};

export default SearchButton;
