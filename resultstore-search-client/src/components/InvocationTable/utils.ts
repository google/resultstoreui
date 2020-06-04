import moment from 'moment';
import invocation_pb, { InvocationAttributes } from '../../api/invocation_pb';
import common_pb from '../../api/common_pb';
import { Data } from './types';

/*
Parses invocation returned from search into invocation table consumable data

Args:
    Invocation: An invocation to be parsed

Returns:
    Table consumable object
*/
function parseInvocationTableData(invocation: invocation_pb.Invocation): Data {
    const statusAttributes = invocation.getStatusAttributes();
    const invocationAttributes = invocation.getInvocationAttributes();
    const workspaceInfo = invocation.getWorkspaceInfo();
    const timing = invocation.getTiming();

    const status = getStatus(statusAttributes);
    const name = invocation.getName();
    const labels = getLabels(invocationAttributes)
    const date = getDate(timing);
    const duration = getDuration(timing);
    const user = getUser(invocationAttributes, workspaceInfo);

    return { status, name, labels, date, duration, user };
}


/*
Helper functions to format invocation table data
*/

const getDate = (timing: common_pb.Timing | undefined) => {
    const startTiming =
        (timing &&
            timing.getStartTime() &&
            timing.getStartTime().getSeconds()) ||
        0;
    const startTime = moment.unix(startTiming);
    return startTime.format('YYYY-MM-DD, hh:mm A');
};

const getUser = (
    invocationAttributes: invocation_pb.InvocationAttributes | undefined,
    workspaceInfo: invocation_pb.WorkspaceInfo | undefined
) => {
    const hostname = (workspaceInfo && workspaceInfo.getHostname()) || '';
    const usersList = (invocationAttributes &&
        invocationAttributes.getUsersList()) || ['None'];
    const userPrefix = (usersList.length > 0 && usersList[0]) || 'None';
    return `${userPrefix}@${hostname}`;
};

const getStatus = (
    statusAttributes: common_pb.StatusAttributes | undefined
) => {
    return (statusAttributes && statusAttributes.getDescription()) || 'UNKNOWN';
}

const getLabels = (
    invocationAttributes: invocation_pb.InvocationAttributes
) => {
    const labelsList =
        (invocationAttributes && invocationAttributes.getLabelsList()) || [];
    return labelsList.join(',');
}

const getDuration = (
    timing: common_pb.Timing | undefined
) => {
    const timingDuration = timing.getDuration();
    const durationSeconds =
        (timingDuration && timingDuration.getSeconds()) || 0;
    return moment
    .utc(moment.duration(durationSeconds, 's').asMilliseconds())
    .format('mm:ss');
}

export { parseInvocationTableData };
