import React from 'react';
import CheckIcon from '@material-ui/icons/Check';
import BuildIcon from '@material-ui/icons/Build';
import DirectionsRunIcon from '@material-ui/icons/DirectionsRun';
import TimerIcon from '@material-ui/icons/Timer';
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';

interface Props {
    name:
        | 'PASS'
        | 'BUILDING'
        | 'BUILT'
        | 'FAILED_TO_BUILD'
        | 'TESTING'
        | 'FAILED'
        | 'TIMED_OUT'
        | 'CANCELLED'
        | 'TOOL_FAILED'
        | 'UNKNOWN'
        | 'SKIPPED';
    size?: number;
    style?: React.CSSProperties;
}

const StatusIcon: React.FC<Props> = ({ name, style }) => {
    switch (name) {
        case 'PASS': {
            return (
                <CheckIcon
                    fontSize={'small'}
                    htmlColor={'#34a853'}
                    style={style}
                />
            );
        }
        case 'BUILDING': {
            return (
                <BuildIcon
                    fontSize={'small'}
                    htmlColor={'#90caf9'}
                    style={style}
                />
            );
        }
        case 'TESTING': {
            return (
                <DirectionsRunIcon
                    fontSize={'small'}
                    htmlColor={'#fca311'}
                    style={style}
                />
            );
        }
        case 'TIMED_OUT': {
            return (
                <TimerIcon
                    fontSize={'small'}
                    htmlColor={'#370617'}
                    style={style}
                />
            );
        }
        case 'UNKNOWN': {
            return (
                <HelpOutlineIcon
                    fontSize={'small'}
                    htmlColor={'#252422'}
                    style={style}
                />
            );
        }
        default: {
            return (
                <HelpOutlineIcon
                    fontSize={'small'}
                    htmlColor={'#252422'}
                    style={style}
                />
            );
        }
    }
};

export default StatusIcon;
