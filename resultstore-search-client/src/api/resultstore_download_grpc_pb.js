// GENERATED CODE -- DO NOT EDIT!
/* tslint:disable */
/* eslint-disable */

'use strict';
var grpc = require('grpc');
var resultstore_download_pb = require('./resultstore_download_pb.js');
var invocation_pb = require('./invocation_pb.js');

function serialize_resultstoresearch_v1_GetInvocationRequest(arg) {
  if (!(arg instanceof resultstore_download_pb.GetInvocationRequest)) {
    throw new Error('Expected argument of type resultstoresearch.v1.GetInvocationRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_resultstoresearch_v1_GetInvocationRequest(buffer_arg) {
  return resultstore_download_pb.GetInvocationRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_resultstoresearch_v1_Invocation(arg) {
  if (!(arg instanceof invocation_pb.Invocation)) {
    throw new Error('Expected argument of type resultstoresearch.v1.Invocation');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_resultstoresearch_v1_Invocation(buffer_arg) {
  return invocation_pb.Invocation.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_resultstoresearch_v1_SearchInvocationsRequest(arg) {
  if (!(arg instanceof resultstore_download_pb.SearchInvocationsRequest)) {
    throw new Error('Expected argument of type resultstoresearch.v1.SearchInvocationsRequest');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_resultstoresearch_v1_SearchInvocationsRequest(buffer_arg) {
  return resultstore_download_pb.SearchInvocationsRequest.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_resultstoresearch_v1_SearchInvocationsResponse(arg) {
  if (!(arg instanceof resultstore_download_pb.SearchInvocationsResponse)) {
    throw new Error('Expected argument of type resultstoresearch.v1.SearchInvocationsResponse');
  }
  return Buffer.from(arg.serializeBinary());
}

function deserialize_resultstoresearch_v1_SearchInvocationsResponse(buffer_arg) {
  return resultstore_download_pb.SearchInvocationsResponse.deserializeBinary(new Uint8Array(buffer_arg));
}


// This is the interface used to download information from the ResultStore
// database.
//
// Most APIs require setting a response FieldMask via the 'fields' URL query
// parameter or the X-Goog-FieldMask HTTP/gRPC header.
var ResultStoreDownloadService = exports.ResultStoreDownloadService = {
  // Searches for invocations matching the given query parameters. Results will
// be ordered by timing.start_time with most recent first, but total ordering
// of results is not guaranteed when difference in timestamps is very small.
// Results may be stale.
//
//
// An error will be reported in the following cases:
// - If a query string is not provided
// - If no field mask was given.
searchInvocations: {
    path: '/resultstoresearch.v1.ResultStoreDownload/SearchInvocations',
    requestStream: false,
    responseStream: false,
    requestType: resultstore_download_pb.SearchInvocationsRequest,
    responseType: resultstore_download_pb.SearchInvocationsResponse,
    requestSerialize: serialize_resultstoresearch_v1_SearchInvocationsRequest,
    requestDeserialize: deserialize_resultstoresearch_v1_SearchInvocationsRequest,
    responseSerialize: serialize_resultstoresearch_v1_SearchInvocationsResponse,
    responseDeserialize: deserialize_resultstoresearch_v1_SearchInvocationsResponse,
  },
  // Retrieves the invocation with the given name.
//
// An error will be reported in the following cases:
// - If the invocation is not found.
// - If the given invocation name is badly formatted.
// - If no field mask was given.
getInvocation: {
    path: '/resultstoresearch.v1.ResultStoreDownload/GetInvocation',
    requestStream: false,
    responseStream: false,
    requestType: resultstore_download_pb.GetInvocationRequest,
    responseType: invocation_pb.Invocation,
    requestSerialize: serialize_resultstoresearch_v1_GetInvocationRequest,
    requestDeserialize: deserialize_resultstoresearch_v1_GetInvocationRequest,
    responseSerialize: serialize_resultstoresearch_v1_Invocation,
    responseDeserialize: deserialize_resultstoresearch_v1_Invocation,
  },
};

exports.ResultStoreDownloadClient = grpc.makeGenericClientConstructor(ResultStoreDownloadService);
