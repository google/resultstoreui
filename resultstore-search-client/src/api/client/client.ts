import * as grpcWeb from 'grpc-web';
import { ResultStoreDownloadClient } from '../Resultstore_downloadServiceClientPb';
import {
    SearchInvocationsRequest,
    SearchInvocationsResponse,
    GetInitialStateRequest,
    GetInitialStateResponse,
    ListTargetsRequest,
    ListTargetsResponse,
    ListTargetSubFilesRequest,
    ListTargetSubFilesResponse,
    DownloadFileRequest,
    DownloadFileResponse,
    GetTestCasesRequest,
    GetTestCasesResponse,
} from '../resultstore_download_pb';
import * as invocation_pb from '../invocation_pb';
import config from '../../config/ConfigLoader';
import { TokenId } from '../../contexts/AuthContext';

export type SetInvocations = (
    invocations: Array<invocation_pb.Invocation>
) => void;
export type SetToolsList = (toolsList: Array<string>) => void;
export type SearchInvocationCallback = (
    err: grpcWeb.Error,
    response: SearchInvocationsResponse,
    newQuery: boolean
) => void;
export type DownloadFileCallback = (
    err: grpcWeb.Error,
    response: DownloadFileResponse
) => void;
export type ListTargetsCallback = (
    err: grpcWeb.Error,
    response: ListTargetsResponse
) => void;
export type ListTargetSubFilesCallback = (
    err: grpcWeb.Error,
    response: ListTargetSubFilesResponse
) => void;
export type GetTestCasesCallback = (
    err: grpcWeb.Error,
    response: GetTestCasesResponse
) => void;

const resultStore = new ResultStoreDownloadClient(
    config.destinationAddress,
    null,
    null
);
const defaultPageSize = 25;
const searchFieldMask =
    'next_page_token,invocations.name,invocations.invocation_attributes,invocations.timing,invocations.workspace_info,invocations.status_attributes,invocations.files';
const searchTargetFieldMask =
    'next_page_token,targets.name,targets.files,targets.properties,targets.id';

/*
Search for invocations by query

Args:
    query: The query to search for invocations
    setInvocations: Function called on the returned array of Invocations
    updateError: Function called if the api returned an error message
*/
const searchInvocations = (
    query: string,
    newQuery: boolean,
    tool: string,
    pageToken: string,
    tokenID: TokenId,
    callback: SearchInvocationCallback
) => {
    const request = new SearchInvocationsRequest();
    request.setPageSize(defaultPageSize);
    request.setQuery(query);
    request.setProjectId(config.projectId);
    request.setTool(tool);

    if (!newQuery) {
        request.setPageToken(pageToken);
    }

    const metadata = {
        'x-goog-fieldmask': searchFieldMask,
        id_token: tokenID,
    };
    resultStore.searchInvocations(request, metadata, (err, response) => {
        callback(err, response, newQuery);
    });
};

const listTargetsRequest = (
    newQuery: boolean,
    parent: string,
    pageToken: string,
    tokenID: TokenId,
    callback: ListTargetsCallback
) => {
    const request = new ListTargetsRequest();
    request.setPageToken(pageToken);
    request.setPageSize(defaultPageSize);
    request.setParent(parent);

    const metadata = {
        'x-goog-fieldmask': searchTargetFieldMask,
        id_token: tokenID,
    };

    if (!newQuery) {
        request.setPageToken(pageToken);
    }

    resultStore.listTargets(request, metadata, callback);
};

const listTargetSubFiles = (
    parent: string,
    tokenID: TokenId,
    callback: ListTargetSubFilesCallback
) => {
    const request = new ListTargetSubFilesRequest();
    request.setParent(parent);

    const metadata = {
        id_token: tokenID,
    };

    resultStore.listTargetSubFiles(request, metadata, callback);
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

const downloadFile = (
    fileName: string,
    tokenID: TokenId,
    callback: DownloadFileCallback
) => {
    const request = new DownloadFileRequest();
    request.setFileName(fileName);
    const metadata = {
        id_token: tokenID,
    };
    resultStore.downloadFile(request, metadata, callback);
};

const getTestCases = (
    query: string,
    tool: string,
    pageToken: string,
    tokenID: TokenId,
    invocations: Array<invocation_pb.Invocation>,
    callback: GetTestCasesCallback
) => {
    const metadata = {
        'x-goog-fieldmask': searchFieldMask,
        id_token: tokenID,
    };

    const request = new GetTestCasesRequest();
    request.setPageSize(defaultPageSize);
    request.setPageToken(pageToken);
    request.setProjectId(config.projectId);
    request.setQuery(query);
    request.setTool(tool);
    request.setInvocationsList(invocations);

    resultStore.getTestCases(request, metadata, callback);
};

export {
    searchInvocations,
    getInitialState,
    downloadFile,
    listTargetsRequest,
    listTargetSubFiles,
    getTestCases,
};
