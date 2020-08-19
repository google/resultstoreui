// FileModal Component
/**
 * Component that renders the file modal. Files are shown according to the current active
 * invocation or target.
 * @packageDocumentation
 */
import React, { useState, useEffect, useRef } from 'react';
import { makeStyles, createStyles } from '@material-ui/core/styles';
import KeyboardArrowDownIcon from '@material-ui/icons/KeyboardArrowDown';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';
import styled from 'styled-components';
import * as file_pb from '../../../api/file_pb';
import TargetList, { ListRow } from './TargetList';
import FileTable from './FileTable';

const DEFAULT_LIST_WIDTH = 400;
const DEFAULT_ROW_HEIGHT = 30;

const ModalContainer = styled.div`
    background-color: white;
    outline: none;
    border: 2px solid #e0e0e0;
    boxshadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
        0px 5px 8px 0px rgba(0, 0, 0, 0.14),
        0px 1px 14px 0px rgba(0, 0, 0, 0.12);
    width: 80%;
    height: 80%;
    margin: auto;
    display: flex;
    min-width: 1284;
`;

const RowContainer = styled.div`
    width: ${DEFAULT_LIST_WIDTH}px;
    border-right-style: solid;
    border-width: 2px;
    border-color: #e0e0e0;
    height: 100%;
    flex: 0;
`;

const HeaderRow = styled(ListRow)`
    background-color: #fafafa;
    padding-left: 0px;
    font-weight: bold;
    :hover {
        background-color: white;
    }
`;

const ChevronDown = styled(KeyboardArrowDownIcon)`
    padding: 0 5px 0 5px;
`;

const useStyles = makeStyles(() =>
    createStyles({
        modal: {
            display: 'flex',
        },
    })
);

/** FileModal Props */
export interface Props {
    /** FileModal is visible if true */
    isOpen: boolean;
    /** Callback fired when modal is closed */
    close: () => void;
    /** Files to be rendered in the file modal for the parent invocation */
    files: Array<file_pb.File>;
    /** Current invocation whose files and target files are being rendered */
    parent: string;
}

/** FileModal State */
interface State {
    /** Currently selected files to be viewed in the file table */
    selectedFiles: Array<file_pb.File>;
    /** Current resource whose files are viewable */
    selectedName: string;
    /** Type of currently selected resource */
    selectedType: 'target' | 'invocation';
    /** Show spinner if tables rows are being loaded */
    isLoadingTableRows: boolean;
    /** Height of the FileModal */
    height: number;
}

/** FileModal Component */
export const FileModal: React.FC<Props> = ({
    isOpen,
    close,
    files,
    parent,
}) => {
    const classes = useStyles();
    const containerRef = useRef(null);
    const [selectedFiles, setSelectedFiles] = useState<State['selectedFiles']>(
        files
    );
    const [height, setHeight] = useState(1080);
    const [selectedName, setSelectedName] = useState<State['selectedName']>(
        parent.slice(12)
    );
    const [selectedType, setSelectedType] = useState<State['selectedType']>(
        'invocation'
    );
    const [isLoadingTableRows, setIsLoadingTableRows] = useState<
        State['isLoadingTableRows']
    >(false);
    const setDimensions = () => {
        setHeight(
            containerRef.current ? containerRef.current.offsetHeight : 1080
        );
    };

    useEffect(() => {
        setDimensions();
        window.addEventListener('resize', setDimensions);
        return () => window.removeEventListener('resize', setDimensions);
    }, [containerRef.current, isOpen]);

    const invocationName = parent.replace('invocations/', '');

    const handleClose = () => {
        close();
    };

    const onClick = (
        name: string,
        files: Array<file_pb.File>,
        isLoadingTableRows: boolean
    ) => {
        setSelectedName(name);
        setSelectedFiles(files);
        setIsLoadingTableRows(isLoadingTableRows);
    };

    const onTargetClick = (
        name: string,
        files: Array<file_pb.File>,
        isLoadingTableRows: boolean
    ) => {
        setSelectedType('target');
        onClick(name, files, isLoadingTableRows);
    };

    const onInvocationClick = () => {
        setSelectedType('invocation');
        onClick(parent.slice(12), files, false);
    };

    useEffect(() => {
        if (isOpen) {
            onInvocationClick();
        }
    }, [isOpen]);

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
                <ModalContainer id="FileModal" ref={containerRef}>
                    <RowContainer>
                        <HeaderRow>
                            <ChevronDown />
                            {'Invocation'}
                        </HeaderRow>
                        <ListRow
                            onClick={onInvocationClick}
                            id={'InvocationModalRow'}
                        >
                            {invocationName}
                        </ListRow>
                        <HeaderRow>
                            <ChevronDown />
                            {'Targets'}
                        </HeaderRow>
                        <TargetList
                            parent={parent}
                            rowHeight={DEFAULT_ROW_HEIGHT}
                            height={height - 3 * DEFAULT_ROW_HEIGHT - 10}
                            width={DEFAULT_LIST_WIDTH}
                            onClick={onTargetClick}
                        />
                    </RowContainer>
                    <FileTable
                        selectedName={selectedName}
                        selectedType={selectedType}
                        files={selectedFiles}
                        isLoadingTableRows={isLoadingTableRows}
                    />
                </ModalContainer>
            </Fade>
        </Modal>
    );
};

export default FileModal;
