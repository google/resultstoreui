import React from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormHelperText from '@material-ui/core/FormHelperText';
import Search from '@material-ui/icons/Search';
import FormControl from '@material-ui/core/FormControl';
import { State as PageWrapperState } from '..';
import * as invocation_pb from '../../../api/invocation_pb';

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

export interface State {
    query: string;
    invocations: Array<invocation_pb.Invocation>;
    errorText: string;
    hasError: boolean;
}

export interface SearchBarProps {
    setQueryParent: (query: PageWrapperState['query']) => void;
    errorText: string;
    hasError: boolean;
}

/*
SearchBar component to search for invocations by query string
*/
const SearchBar: React.FC<SearchBarProps> = ({
    setQueryParent,
    errorText,
    hasError,
}) => {
    const [query, setQuery] = React.useState<State['query']>('');
    const classes = useStyles();

    const updateQuery = (query: string) => {
        setQuery(query);
        setQueryParent(query);
    };

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
