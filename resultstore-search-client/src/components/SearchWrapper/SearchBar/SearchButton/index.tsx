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
`;

interface Props {
    showSpinner: boolean;
    size?: number;
    onClick?: () => void;
}

const SearchButton: React.FC<Props> = ({ showSpinner, size = 25, onClick }) => {
    return (
        <SearchButtonContainer variant="outlined" onClick={onClick}>
            {showSpinner && <TableSpinner size={size} />}
            {!showSpinner && <SearchIcon />}
        </SearchButtonContainer>
    );
};

export default SearchButton;
