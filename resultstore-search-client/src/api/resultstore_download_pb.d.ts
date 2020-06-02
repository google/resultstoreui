import * as jspb from "google-protobuf"

import * as invocation_pb from './invocation_pb';

export class SearchInvocationsRequest extends jspb.Message {
  getPageSize(): number;
  setPageSize(value: number): SearchInvocationsRequest;

  getPageToken(): string;
  setPageToken(value: string): SearchInvocationsRequest;

  getOffset(): number;
  setOffset(value: number): SearchInvocationsRequest;

  getQuery(): string;
  setQuery(value: string): SearchInvocationsRequest;

  getProjectId(): string;
  setProjectId(value: string): SearchInvocationsRequest;

  getExactMatch(): boolean;
  setExactMatch(value: boolean): SearchInvocationsRequest;

  getPageStartCase(): SearchInvocationsRequest.PageStartCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SearchInvocationsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: SearchInvocationsRequest): SearchInvocationsRequest.AsObject;
  static serializeBinaryToWriter(message: SearchInvocationsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SearchInvocationsRequest;
  static deserializeBinaryFromReader(message: SearchInvocationsRequest, reader: jspb.BinaryReader): SearchInvocationsRequest;
}

export namespace SearchInvocationsRequest {
  export type AsObject = {
    pageSize: number,
    pageToken: string,
    offset: number,
    query: string,
    projectId: string,
    exactMatch: boolean,
  }

  export enum PageStartCase { 
    PAGE_START_NOT_SET = 0,
    PAGE_TOKEN = 2,
    OFFSET = 3,
  }
}

export class GetInvocationRequest extends jspb.Message {
  getName(): string;
  setName(value: string): GetInvocationRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetInvocationRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetInvocationRequest): GetInvocationRequest.AsObject;
  static serializeBinaryToWriter(message: GetInvocationRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetInvocationRequest;
  static deserializeBinaryFromReader(message: GetInvocationRequest, reader: jspb.BinaryReader): GetInvocationRequest;
}

export namespace GetInvocationRequest {
  export type AsObject = {
    name: string,
  }
}

export class SearchInvocationsResponse extends jspb.Message {
  getInvocationsList(): Array<invocation_pb.Invocation>;
  setInvocationsList(value: Array<invocation_pb.Invocation>): SearchInvocationsResponse;
  clearInvocationsList(): SearchInvocationsResponse;
  addInvocations(value?: invocation_pb.Invocation, index?: number): invocation_pb.Invocation;

  getNextPageToken(): string;
  setNextPageToken(value: string): SearchInvocationsResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): SearchInvocationsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: SearchInvocationsResponse): SearchInvocationsResponse.AsObject;
  static serializeBinaryToWriter(message: SearchInvocationsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): SearchInvocationsResponse;
  static deserializeBinaryFromReader(message: SearchInvocationsResponse, reader: jspb.BinaryReader): SearchInvocationsResponse;
}

export namespace SearchInvocationsResponse {
  export type AsObject = {
    invocationsList: Array<invocation_pb.Invocation.AsObject>,
    nextPageToken: string,
  }
}

