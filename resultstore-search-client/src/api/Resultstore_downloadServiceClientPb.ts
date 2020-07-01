/**
 * @fileoverview gRPC-Web generated client stub for resultstoresearch.v1
 * @enhanceable
 * @public
 */

// GENERATED CODE -- DO NOT EDIT!


/* eslint-disable */
// @ts-nocheck


import * as grpcWeb from 'grpc-web';

import * as invocation_pb from './invocation_pb';
import * as target_pb from './target_pb';
import * as file_pb from './file_pb';

import {
  DownloadFileRequest,
  DownloadFileResponse,
  GetFileRequest,
  GetFileResponse,
  GetInitialStateRequest,
  GetInitialStateResponse,
  GetInvocationRequest,
  ListTargetSubFilesRequest,
  ListTargetSubFilesResponse,
  ListTargetsRequest,
  ListTargetsResponse,
  SearchInvocationsRequest,
  SearchInvocationsResponse} from './resultstore_download_pb';

export class ResultStoreDownloadClient {
  client_: grpcWeb.AbstractClientBase;
  hostname_: string;
  credentials_: null | { [index: string]: string; };
  options_: null | { [index: string]: string; };

  constructor (hostname: string,
               credentials?: null | { [index: string]: string; },
               options?: null | { [index: string]: string; }) {
    if (!options) options = {};
    if (!credentials) credentials = {};
    options['format'] = 'text';

    this.client_ = new grpcWeb.GrpcWebClientBase(options);
    this.hostname_ = hostname;
    this.credentials_ = credentials;
    this.options_ = options;
  }

  methodInfoSearchInvocations = new grpcWeb.AbstractClientBase.MethodInfo(
    SearchInvocationsResponse,
    (request: SearchInvocationsRequest) => {
      return request.serializeBinary();
    },
    SearchInvocationsResponse.deserializeBinary
  );

  searchInvocations(
    request: SearchInvocationsRequest,
    metadata: grpcWeb.Metadata | null): Promise<SearchInvocationsResponse>;

  searchInvocations(
    request: SearchInvocationsRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: SearchInvocationsResponse) => void): grpcWeb.ClientReadableStream<SearchInvocationsResponse>;

  searchInvocations(
    request: SearchInvocationsRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: SearchInvocationsResponse) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/SearchInvocations', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoSearchInvocations,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/SearchInvocations',
    request,
    metadata || {},
    this.methodInfoSearchInvocations);
  }

  methodInfoGetInvocation = new grpcWeb.AbstractClientBase.MethodInfo(
    invocation_pb.Invocation,
    (request: GetInvocationRequest) => {
      return request.serializeBinary();
    },
    invocation_pb.Invocation.deserializeBinary
  );

  getInvocation(
    request: GetInvocationRequest,
    metadata: grpcWeb.Metadata | null): Promise<invocation_pb.Invocation>;

  getInvocation(
    request: GetInvocationRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: invocation_pb.Invocation) => void): grpcWeb.ClientReadableStream<invocation_pb.Invocation>;

  getInvocation(
    request: GetInvocationRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: invocation_pb.Invocation) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/GetInvocation', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoGetInvocation,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/GetInvocation',
    request,
    metadata || {},
    this.methodInfoGetInvocation);
  }

  methodInfoListTargets = new grpcWeb.AbstractClientBase.MethodInfo(
    ListTargetsResponse,
    (request: ListTargetsRequest) => {
      return request.serializeBinary();
    },
    ListTargetsResponse.deserializeBinary
  );

  listTargets(
    request: ListTargetsRequest,
    metadata: grpcWeb.Metadata | null): Promise<ListTargetsResponse>;

  listTargets(
    request: ListTargetsRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: ListTargetsResponse) => void): grpcWeb.ClientReadableStream<ListTargetsResponse>;

  listTargets(
    request: ListTargetsRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: ListTargetsResponse) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/ListTargets', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoListTargets,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/ListTargets',
    request,
    metadata || {},
    this.methodInfoListTargets);
  }

  methodInfoListTargetSubFiles = new grpcWeb.AbstractClientBase.MethodInfo(
    ListTargetSubFilesResponse,
    (request: ListTargetSubFilesRequest) => {
      return request.serializeBinary();
    },
    ListTargetSubFilesResponse.deserializeBinary
  );

  listTargetSubFiles(
    request: ListTargetSubFilesRequest,
    metadata: grpcWeb.Metadata | null): Promise<ListTargetSubFilesResponse>;

  listTargetSubFiles(
    request: ListTargetSubFilesRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: ListTargetSubFilesResponse) => void): grpcWeb.ClientReadableStream<ListTargetSubFilesResponse>;

  listTargetSubFiles(
    request: ListTargetSubFilesRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: ListTargetSubFilesResponse) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/ListTargetSubFiles', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoListTargetSubFiles,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/ListTargetSubFiles',
    request,
    metadata || {},
    this.methodInfoListTargetSubFiles);
  }

  methodInfoGetFile = new grpcWeb.AbstractClientBase.MethodInfo(
    GetFileResponse,
    (request: GetFileRequest) => {
      return request.serializeBinary();
    },
    GetFileResponse.deserializeBinary
  );

  getFile(
    request: GetFileRequest,
    metadata?: grpcWeb.Metadata) {
    return this.client_.serverStreaming(
      new URL('/resultstoresearch.v1.ResultStoreDownload/GetFile', this.hostname_).toString(),
      request,
      metadata || {},
      this.methodInfoGetFile);
  }

  methodInfoDownloadFile = new grpcWeb.AbstractClientBase.MethodInfo(
    DownloadFileResponse,
    (request: DownloadFileRequest) => {
      return request.serializeBinary();
    },
    DownloadFileResponse.deserializeBinary
  );

  downloadFile(
    request: DownloadFileRequest,
    metadata: grpcWeb.Metadata | null): Promise<DownloadFileResponse>;

  downloadFile(
    request: DownloadFileRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: DownloadFileResponse) => void): grpcWeb.ClientReadableStream<DownloadFileResponse>;

  downloadFile(
    request: DownloadFileRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: DownloadFileResponse) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/DownloadFile', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoDownloadFile,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/DownloadFile',
    request,
    metadata || {},
    this.methodInfoDownloadFile);
  }

  methodInfoGetInitialState = new grpcWeb.AbstractClientBase.MethodInfo(
    GetInitialStateResponse,
    (request: GetInitialStateRequest) => {
      return request.serializeBinary();
    },
    GetInitialStateResponse.deserializeBinary
  );

  getInitialState(
    request: GetInitialStateRequest,
    metadata: grpcWeb.Metadata | null): Promise<GetInitialStateResponse>;

  getInitialState(
    request: GetInitialStateRequest,
    metadata: grpcWeb.Metadata | null,
    callback: (err: grpcWeb.Error,
               response: GetInitialStateResponse) => void): grpcWeb.ClientReadableStream<GetInitialStateResponse>;

  getInitialState(
    request: GetInitialStateRequest,
    metadata: grpcWeb.Metadata | null,
    callback?: (err: grpcWeb.Error,
               response: GetInitialStateResponse) => void) {
    if (callback !== undefined) {
      return this.client_.rpcCall(
        new URL('/resultstoresearch.v1.ResultStoreDownload/GetInitialState', this.hostname_).toString(),
        request,
        metadata || {},
        this.methodInfoGetInitialState,
        callback);
    }
    return this.client_.unaryCall(
    this.hostname_ +
      '/resultstoresearch.v1.ResultStoreDownload/GetInitialState',
    request,
    metadata || {},
    this.methodInfoGetInitialState);
  }

}

