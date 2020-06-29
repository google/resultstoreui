import React from 'react';
import { Typography } from '@material-ui/core';
import styled from 'styled-components';

const Error = styled(Typography)`
    color: #ed3224;
`;

interface Props {
    text: string;
    id: string;
}

export interface Error {
    errorText: string;
    hasError: boolean;
}

/*
Component to display error text
*/
const ErrorText: React.FC<Props> = ({ text, id }) => {
    return (
        <Error id={id} align="center">
            {text}
        </Error>
    );
};

export default ErrorText;
