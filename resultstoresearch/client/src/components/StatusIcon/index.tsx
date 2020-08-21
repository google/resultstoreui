// StatusIcon Component
/**
 * Icon used to signify status of an invocation
 * @packageDocumentation
 */
import React from 'react';
import CheckIcon from '@material-ui/icons/Check';
import BuildIcon from '@material-ui/icons/Build';
import DirectionsRunIcon from '@material-ui/icons/DirectionsRun';
import TimerIcon from '@material-ui/icons/Timer';
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';
import ErrorIcon from '@material-ui/icons/Error';

/** StatusIcon Props */
interface Props {
    /** Type of status to be displayed */
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
    /** Size of display icon svg */
    size?: number;
    /** Display icon style */
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
        case 'FAILED': {
            return (
                <ErrorIcon
                    fontSize={'small'}
                    htmlColor={'#d73f35'}
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
