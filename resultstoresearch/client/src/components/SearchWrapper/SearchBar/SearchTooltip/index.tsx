import React from 'react';
import Tooltip from '@material-ui/core/Tooltip';
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';
import Typography from '@material-ui/core/Typography';

const SearchTooltip: React.FC = () => {
    return (
        <Tooltip
            title={
                <Typography style={{ fontSize: 14 }}>
                    {'Fields that support equals ("=") restrictions:'} <br />
                    {'name'} <br />
                    {'status_attributes.status'} <br />
                    {'workspace_info.hostname'} <br /> <br />
                    {'Fields that support contains (":") restrictions:'} <br />
                    {'invocation_attributes.users'} <br />
                    {'invocation_attributes.labels'} <br /> <br />
                    {
                        'Fields that support comparison ("<", "<=", ">", ">=") restrictions:'
                    }
                    <br />
                    {'timing.start_time'} <br /> <br />
                    {'Supported custom function global restrictions:'} <br />
                    {'propertyEquals("key", "value")'}
                </Typography>
            }
            aria-label="SearchHelp"
        >
            <HelpOutlineIcon />
        </Tooltip>
    );
};

export default SearchTooltip;
