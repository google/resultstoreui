import React, { useEffect } from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormHelperText from '@material-ui/core/FormHelperText';
import Search from '@material-ui/icons/Search';
import FormControl from '@material-ui/core/FormControl';
import { SetInvocations, searchInvocations } from '../../api/client/client';
import { ToolSelectProps } from '../ToolSelect';
import * as invocation_pb from '../../api/invocation_pb';

const searchPlaceholder = 'Search Invocations';

const useStyles = makeStyles((theme: Theme) =>
    createStyles({
        margin: {
            margin: theme.spacing(1),
        },
        root: {
            display: 'flex',
            flexWrap: 'wrap',
            flexGrow: 2,
        },
    })
);

interface State {
    query: string;
    invocations: Array<invocation_pb.Invocation>;
    errorText: string;
    hasError: boolean;
}

export interface InvocationTableProps {
    setInvocations: SetInvocations;
    tool: ToolSelectProps['selectedTool'];
    setToolsList: ToolSelectProps['setToolsList'];
}

/*
SearchBar component to search for invocations by query string
*/
const SearchBar: React.FC<InvocationTableProps> = ({
    setInvocations,
    setToolsList,
    tool,
}) => {
    const [query, setQuery] = React.useState<State['query']>('');
    const [errorText, setErrorText] = React.useState<State['errorText']>('');
    const [hasError, setHasError] = React.useState<State['hasError']>(false);
    const classes = useStyles();

    const updateError = (error: string, hasError: boolean) => {
        setHasError(hasError);
        setErrorText(error);
    };

    const updateQuery = (query: string) => {
        setQuery(query);
        searchInvocations(
            query,
            setInvocations,
            updateError,
            setToolsList,
            tool
        );
    };

    useEffect(() => {
        if (query !== '') {
            searchInvocations(
                query,
                setInvocations,
                updateError,
                setToolsList,
                tool
            );
        }
    }, [tool]);

    return (
        <div className={classes.root}>
            <FormControl
                fullWidth
                className={classes.margin}
                variant="outlined"
                error={hasError}
            >
                <OutlinedInput
                    id="outlined-adornment-amount"
                    startAdornment={
                        <InputAdornment position="start">
                            <Search />
                        </InputAdornment>
                    }
                    value={query}
                    onChange={(e) => updateQuery(e.target.value)}
                    placeholder={searchPlaceholder}
                />
                {hasError && (
                    <FormHelperText id="component-error-text">
                        {errorText}
                    </FormHelperText>
                )}
            </FormControl>
        </div>
    );
};

export default SearchBar;
