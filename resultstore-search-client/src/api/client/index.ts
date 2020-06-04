import * as grpcWeb from 'grpc-web';
import { ResultStoreDownloadClient } from '../Resultstore_downloadServiceClientPb';
import {
    SearchInvocationsRequest,
    SearchInvocationsResponse,
} from '../resultstore_download_pb';
import * as invocation_pb from '../invocation_pb';
import { toSentenceCase } from '../../utils/index';

export type SetInvocations = (invocations: Array<invocation_pb.Invocation>) => void;
type UpdateError = (error: string, hasError: boolean) => void;

const destinationAddress = 'http://localhost:8080';
const resultStore = new ResultStoreDownloadClient(
    destinationAddress,
    null,
    null
);
const projectId = 'google.com:gchips-productivity';
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
    updateError: UpdateError
) => {
    const request = new SearchInvocationsRequest();
    request.setPageSize(defaultPageSize);
    request.setQuery(query);
    request.setProjectId(projectId);
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
                setInvocations(response.getInvocationsList());
            }
        }
    );
};

export { searchInvocations };
