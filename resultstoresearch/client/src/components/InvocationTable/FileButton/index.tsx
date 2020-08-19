import React from 'react';
import styled from 'styled-components';
import Button from '@material-ui/core/Button';

interface Props {
    isVisible: boolean;
    onClick: (e: React.MouseEvent) => void;
    id: string;
}

const FileButtonContainer = styled(Button)<Props>`
    margin-left: auto;
    margin-right: auto;
    visibility: ${({ isVisible }) => (isVisible ? 'visible' : 'hidden')};
`;

const FileButton: React.FC<Props> = ({ onClick, isVisible, id }) => {
    return (
        <FileButtonContainer
            onClick={onClick}
            variant="contained"
            isVisible={isVisible}
            id={id}
        >
            Files
        </FileButtonContainer>
    );
};

export default FileButton;
