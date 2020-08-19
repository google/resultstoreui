// LoadingRow Component
/**
 * Component that adds a place holder row with a loading spinner
 * while data is currently being loaded in a table
 * @packageDocumentation
 */
import React from 'react';
import styled from 'styled-components';
import CircularProgress from '@material-ui/core/CircularProgress';

const TableSpinner = styled(CircularProgress)`
    color: #6e6e6e !important;
`;

const SpinnerContainer = styled.div<Props>`
    margin-top: 5px;
    width: ${({ width }) => width}px;
    display: flex;
    align-items: center;
    justify-content: center;
`;

/** LoadingRow Props */
interface Props {
    /** width of the row */
    width: number;
    /** Size of the spinner svg */
    size?: number;
}

/** LoadingRow Component */
export const LoadingRow: React.FC<Props> = ({ width, size = 25 }) => {
    return (
        <SpinnerContainer width={width}>
            <TableSpinner size={size} />
        </SpinnerContainer>
    );
};

export default LoadingRow;
