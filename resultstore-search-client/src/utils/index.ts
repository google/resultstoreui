import moment from 'moment';
import common_pb from '../api/common_pb';

/*
Converts inputted string to sentence case

Args:
    theString: Inputted string to be converted
*/
const toSentenceCase = (theString) => {
    const newString = theString.toLowerCase().replace(
        // eslint-disable-next-line
        /(^\s*\w|[\.\!\?]\s*\w)/g,
        (c) => {
            return c.toUpperCase();
        }
    );
    return newString;
};

const getDate = (timing: common_pb.Timing | undefined) => {
    const startTiming =
        (timing &&
            timing.getStartTime() &&
            timing.getStartTime().getSeconds()) ||
        0;
    const startTime = moment.unix(startTiming);
    return startTime.format(`YYYY-MM-DD, hh:mm A`);
};

const flakyTestHeaderDate = (timing: common_pb.Timing | undefined) => {
    const startTiming =
        (timing &&
            timing.getStartTime() &&
            timing.getStartTime().getSeconds()) ||
        0;
    const startTime = moment.unix(startTiming);
    return startTime.format(`MM/DD hh:mm`);
};

export { toSentenceCase, getDate, flakyTestHeaderDate };
