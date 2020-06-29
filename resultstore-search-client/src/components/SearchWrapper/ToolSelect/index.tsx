import React, { useEffect } from 'react';
import { createStyles, makeStyles, Theme } from '@material-ui/core/styles';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import Select from '@material-ui/core/Select';
import MenuItem from '@material-ui/core/MenuItem';
import { getInitialState } from '../../../api/client/client';

export interface ToolSelectProps {
    toolsList: Array<string>;
    setToolsList: (toolsList: Array<string>) => void;
    selectedTool: string;
    setSelectedTool: (selectedTool: string) => void;
}

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        formControl: {
            margin: theme.spacing(1),
            minWidth: 120,
        },
    })
);

const createToolItems = (toolsList: ToolSelectProps['toolsList']) => {
    return toolsList.map((tool) => (
        <MenuItem value={tool}>
            <em>{tool}</em>
        </MenuItem>
    ));
};

/*
Tool select dropdown
*/
const ToolSelect: React.FC<ToolSelectProps> = ({
    selectedTool,
    setSelectedTool,
    toolsList,
    setToolsList,
}) => {
    const classes = useStyles();
    useEffect(() => {
        getInitialState(setToolsList);
    }, [setToolsList]);

    return (
        <FormControl variant="outlined" className={classes.formControl}>
            <InputLabel id="demo-simple-select-outlined-label">
                Tool Type
            </InputLabel>
            <Select
                labelId="demo-simple-select-outlined-label"
                id="demo-simple-select-outlined"
                value={selectedTool}
                onChange={(event) =>
                    setSelectedTool(event.target.value as string)
                }
                label="Tool Type"
            >
                <MenuItem value="">
                    <em>None</em>
                </MenuItem>
                {createToolItems(toolsList)}
            </Select>
        </FormControl>
    );
};

export default ToolSelect;
