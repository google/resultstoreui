// ErrorText Component
/**
 * Component that displays error messages
 * @packageDocumentation
 */
import React from 'react';
import { Typography } from '@material-ui/core';
import styled from 'styled-components';

const Error = styled(Typography)`
    color: #ed3224;
`;

/** ErrorText Props */
interface Props {
    /** Button display text */
    text: string;
    /** Button id */
    id: string;
}

/** Component to display error text */
export const ErrorText: React.FC<Props> = ({ text, id }) => {
    return (
        <Error id={id} align="center">
            {text}
        </Error>
    );
};

export default ErrorText;
