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

import {
  GetFileRequest,
  GetFileResponse,
  GetInitialStateRequest,
  GetInitialStateResponse,
  GetInvocationRequest,
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

