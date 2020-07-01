import React from 'react';
import { makeStyles, createStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';
import styled from 'styled-components';
import * as file_pb from '../../../api/file_pb';
import { ModalState } from '../types';

const ModalContainer = styled.div`
    background-color: white;
    border: 2px solid #000;
    boxshadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
        0px 5px 8px 0px rgba(0, 0, 0, 0.14),
        0px 1px 14px 0px rgba(0, 0, 0, 0.12);
    width: 80%;
    height: 80%;
`;

const useStyles = makeStyles(() =>
    createStyles({
        modal: {
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
        },
    })
);

export interface Props {
    isOpen: boolean;
    close: () => void;
    files: Array<file_pb.File>;
}

const FileModal: React.FC<Props> = ({ isOpen, close, files }) => {
    const classes = useStyles();

    const handleClose = () => {
        close();
    };

    return (
        <Modal
            aria-labelledby="transition-modal-title"
            aria-describedby="transition-modal-description"
            className={classes.modal}
            open={isOpen}
            onClose={handleClose}
            closeAfterTransition
            BackdropComponent={Backdrop}
            BackdropProps={{
                timeout: 500,
            }}
        >
            <Fade in={isOpen}>
                <ModalContainer>
                    <h2 id="transition-modal-title">Transition modal</h2>
                    <p id="transition-modal-description">
                        react-transition-group animates me.
                    </p>
                </ModalContainer>
            </Fade>
        </Modal>
    );
};

export default FileModal;
