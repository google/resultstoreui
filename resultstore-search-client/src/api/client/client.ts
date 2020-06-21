import * as grpcWeb from 'grpc-web';
import { ResultStoreDownloadClient } from '../Resultstore_downloadServiceClientPb';
import {
    SearchInvocationsRequest,
    SearchInvocationsResponse,
    GetInitialStateRequest,
    GetInitialStateResponse,
} from '../resultstore_download_pb';
import * as invocation_pb from '../invocation_pb';
import { toSentenceCase } from '../../utils/utils';
import config from '../../config/ConfigLoader';
import { ToolSelectProps } from '../../components/ToolSelect';

export type SetInvocations = (
    invocations: Array<invocation_pb.Invocation>
) => void;
export type SetToolsList = (toolsList: Array<string>) => void;
type UpdateError = (error: string, hasError: boolean) => void;

const resultStore = new ResultStoreDownloadClient(
    config.destinationAddress,
    null,
    null
);
const defaultPageSize = 0;
const searchFieldMask =
    'next_page_token,invocations.name,invocations.invocation_attributes,invocations.timing,invocations.workspace_info,invocations.status_attributes';

/*
Search for invocations by query

Args:
    query: The query to search for invocations
    setInvocations: Function called on the returned array of Invocations
    updateError: Function called if the api returned an error message
*/
const searchInvocations = (
    query: string,
    setInvocations: SetInvocations,
    updateError: UpdateError,
    setToolsList: ToolSelectProps['setToolsList'],
    tool: string
) => {
    const request = new SearchInvocationsRequest();
    request.setPageSize(defaultPageSize);
    request.setQuery(query);
    request.setProjectId(config.projectId);
    request.setTool(tool);
    const metadata = {
        'x-goog-fieldmask': searchFieldMask,
    };
    resultStore.searchInvocations(
        request,
        metadata,
        (err: grpcWeb.Error, response: SearchInvocationsResponse) => {
            if (err) {
                updateError(`${toSentenceCase(err.message)}.`, true);
            } else {
                updateError('', false);
                const toolsList = response.getToolsListList();
                if (toolsList && toolsList.length !== 0) {
                    setToolsList(toolsList);
                }
                setInvocations(response.getInvocationsList());
            }
        }
    );
};

const getInitialState = (setToolsList) => {
    const request = new GetInitialStateRequest();
    const metadata = {};
    resultStore.getInitialState(
        request,
        metadata,
        (err: grpcWeb.Error, response: GetInitialStateResponse) => {
            if (!err) {
                setToolsList(response.getToolsListList());
            }
        }
    );
};

export { searchInvocations, getInitialState };
