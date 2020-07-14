import React from 'react';
import { createStyles, Theme, makeStyles } from '@material-ui/core/styles';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormControl from '@material-ui/core/FormControl';
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import * as invocation_pb from '../../../api/invocation_pb';
import SearchTooltip from './SearchTooltip';
import SearchButton from './SearchButton';
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

export interface State {
    query: string;
    invocations: Array<invocation_pb.Invocation>;
}

export interface SearchBarProps {
    setQueryParent: (query: PageWrapperState['query']) => void;
    hasError: boolean;
    loading: boolean;
}

/*
SearchBar component to search for invocations by query string
*/
const SearchBar: React.FC<SearchBarProps> = ({
    setQueryParent,
    hasError,
    loading,
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
            return option.label.startsWith(latestQuery);
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
                        id="combo-box-demo"
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
            <SearchButton
                showSpinner={loading}
                onClick={() => setQueryParent(query)}
            />
        </>
    );
};

export default SearchBar;
