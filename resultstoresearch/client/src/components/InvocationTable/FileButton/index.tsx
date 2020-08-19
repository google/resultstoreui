// FileButton Component
/**
 * Button that opens the file modal
 * @packageDocumentation
 */
import React from 'react';
import styled from 'styled-components';
import Button from '@material-ui/core/Button';

/** FileButton Props  */
interface Props {
    /** Visible if true else hidden */
    isVisible: boolean;
    /** Callback fired on button click */
    onClick: (e: React.MouseEvent) => void;
    /** FileButton id */
    id: string;
}

const FileButtonContainer = styled(Button)<Props>`
    margin-left: auto;
    margin-right: auto;
    visibility: ${({ isVisible }) => (isVisible ? 'visible' : 'hidden')};
`;

/** FileButton Props */
export const FileButton: React.FC<Props> = ({ onClick, isVisible, id }) => {
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
