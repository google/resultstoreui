// package: resultstoresearch.v1
// file: resultstore_download.proto

/* tslint:disable */
/* eslint-disable */

import * as grpc from "grpc";
import * as resultstore_download_pb from "./resultstore_download_pb";
import * as invocation_pb from "./invocation_pb";

interface IResultStoreDownloadService extends grpc.ServiceDefinition<grpc.UntypedServiceImplementation> {
    searchInvocations: IResultStoreDownloadService_ISearchInvocations;
    getInvocation: IResultStoreDownloadService_IGetInvocation;
}

interface IResultStoreDownloadService_ISearchInvocations extends grpc.MethodDefinition<resultstore_download_pb.SearchInvocationsRequest, resultstore_download_pb.SearchInvocationsResponse> {
    path: string; // "/resultstoresearch.v1.ResultStoreDownload/SearchInvocations"
    requestStream: boolean; // false
    responseStream: boolean; // false
    requestSerialize: grpc.serialize<resultstore_download_pb.SearchInvocationsRequest>;
    requestDeserialize: grpc.deserialize<resultstore_download_pb.SearchInvocationsRequest>;
    responseSerialize: grpc.serialize<resultstore_download_pb.SearchInvocationsResponse>;
    responseDeserialize: grpc.deserialize<resultstore_download_pb.SearchInvocationsResponse>;
}
interface IResultStoreDownloadService_IGetInvocation extends grpc.MethodDefinition<resultstore_download_pb.GetInvocationRequest, invocation_pb.Invocation> {
    path: string; // "/resultstoresearch.v1.ResultStoreDownload/GetInvocation"
    requestStream: boolean; // false
    responseStream: boolean; // false
    requestSerialize: grpc.serialize<resultstore_download_pb.GetInvocationRequest>;
    requestDeserialize: grpc.deserialize<resultstore_download_pb.GetInvocationRequest>;
    responseSerialize: grpc.serialize<invocation_pb.Invocation>;
    responseDeserialize: grpc.deserialize<invocation_pb.Invocation>;
}

export const ResultStoreDownloadService: IResultStoreDownloadService;

export interface IResultStoreDownloadServer {
    searchInvocations: grpc.handleUnaryCall<resultstore_download_pb.SearchInvocationsRequest, resultstore_download_pb.SearchInvocationsResponse>;
    getInvocation: grpc.handleUnaryCall<resultstore_download_pb.GetInvocationRequest, invocation_pb.Invocation>;
}

export interface IResultStoreDownloadClient {
    searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    getInvocation(request: resultstore_download_pb.GetInvocationRequest, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
    getInvocation(request: resultstore_download_pb.GetInvocationRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
    getInvocation(request: resultstore_download_pb.GetInvocationRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
}

export class ResultStoreDownloadClient extends grpc.Client implements IResultStoreDownloadClient {
    constructor(address: string, credentials: grpc.ChannelCredentials, options?: object);
    public searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    public searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    public searchInvocations(request: resultstore_download_pb.SearchInvocationsRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: resultstore_download_pb.SearchInvocationsResponse) => void): grpc.ClientUnaryCall;
    public getInvocation(request: resultstore_download_pb.GetInvocationRequest, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
    public getInvocation(request: resultstore_download_pb.GetInvocationRequest, metadata: grpc.Metadata, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
    public getInvocation(request: resultstore_download_pb.GetInvocationRequest, metadata: grpc.Metadata, options: Partial<grpc.CallOptions>, callback: (error: grpc.ServiceError | null, response: invocation_pb.Invocation) => void): grpc.ClientUnaryCall;
}
