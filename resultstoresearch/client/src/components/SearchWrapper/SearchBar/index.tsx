// SearchBar Component
/**
 * SearchBar that queries a list of invocations to be rendered in the invocation table
 * @packageDocumentation
 */
import React from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormControl from '@material-ui/core/FormControl';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import * as invocation_pb from '../../../api/invocation_pb';
import SearchTooltip from './SearchTooltip';
import SearchButton from './SearchButton';
import FlakyTestButton from './FlakyTestButton';
import { State as PageWrapperState } from '../';

interface QueryPrefix {
    value: string;
    label: string;
}

const searchPlaceholder = 'Search Invocations';
const queryPrefixes: Array<QueryPrefix> = [
    {
        value: 'invocation_attributes.users:',
        label: 'invocation_attributes.users',
    },
    {
        value: 'invocation_attributes.labels:',
        label: 'invocation_attributes.labels',
    },
    { value: 'name=', label: 'name' },
    { value: 'status_attributes.status=', label: 'status_attributes.status' },
    { value: 'workspace_info.hostname=', label: 'workspace_info.hostname' },
    {
        value: 'timing.start_time',
        label: 'timing.start_time',
    },
];

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

/** SearchBar State */
export interface State {
    /** Current query in the search bar */
    query: string;
}

/** SearchBar Props */
export interface SearchBarProps {
    /** Set the current search bar query in the search wrapper */
    setQueryParent: (query: PageWrapperState['query']) => void;
    /** Currently selected query in the search wrapper */
    queryParent: PageWrapperState['query'];
    /** Current query has an error if true */
    hasError: boolean;
    /** True if current search query is in process */
    loading: boolean;
    /** Callback fired when the flaky test button is clicked */
    onFlakyTestClick?: () => void;
    /** Show the search button if true */
    showSearchButton?: boolean;
    /** Show flaky test button if true */
    showFlakyTestButton?: boolean;
    /** Flaky button click is disabled if true */
    flakyDisabled: boolean;
    /** Search is disabled if true */
    searchDisabled: boolean;
}

/*
SearchBar component to search for invocations by query string
*/
export const SearchBar: React.FC<SearchBarProps> = ({
    setQueryParent,
    queryParent,
    hasError,
    loading,
    showSearchButton = true,
    showFlakyTestButton = true,
    onFlakyTestClick,
    flakyDisabled,
    searchDisabled,
}) => {
    const [query, setQuery] = React.useState<State['query']>('');
    const classes = useStyles();

    const onChange = (_, value: QueryPrefix, reason) => {
        if (reason === 'select-option') {
            const splitQuery = query.split(' ');
            splitQuery[splitQuery.length - 1] = value.value;
            const newQuery = splitQuery.join(' ');
            setQuery(newQuery);
            return newQuery;
        }
    };

    const updateQuery = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter') {
            setQueryParent(query);
        }
    };

    const filterOptions = (options: Array<QueryPrefix>) => {
        const splitQuery = query.split(' ');
        const latestQuery = splitQuery[splitQuery.length - 1];
        const filteredOptions = options.filter((option) => {
            return option.label.includes(latestQuery);
        });
        return filteredOptions;
    };

    return (
        <>
            <div className={classes.root}>
                <FormControl
                    fullWidth
                    className={classes.margin}
                    variant="outlined"
                    error={hasError}
                >
                    <Autocomplete
                        id="search-bar"
                        options={queryPrefixes}
                        getOptionLabel={(option: QueryPrefix) => option.label}
                        selectOnFocus={false}
                        inputValue={query}
                        value={''}
                        clearOnBlur={false}
                        onChange={onChange}
                        onKeyDown={(e) => updateQuery(e)}
                        onInputChange={(_, value: string) => setQuery(value)}
                        renderInput={(params) => (
                            <TextField
                                {...params}
                                variant="outlined"
                                InputProps={{
                                    ...params.InputProps,
                                    startAdornment: (
                                        <InputAdornment position="end">
                                            <SearchTooltip />
                                        </InputAdornment>
                                    ),
                                }}
                                placeholder={searchPlaceholder}
                            ></TextField>
                        )}
                        filterOptions={filterOptions}
                    ></Autocomplete>
                </FormControl>
            </div>
            {showSearchButton && (
                <SearchButton
                    showSpinner={loading}
                    onClick={() => setQueryParent(query)}
                    disabled={searchDisabled || flakyDisabled}
                />
            )}
            {showFlakyTestButton && (
                <FlakyTestButton
                    showSpinner={flakyDisabled}
                    onClick={onFlakyTestClick}
                    disabled={
                        flakyDisabled || searchDisabled || queryParent === ''
                    }
                />
            )}
        </>
    );
};

export default SearchBar;
