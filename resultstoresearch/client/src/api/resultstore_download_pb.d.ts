import * as jspb from "google-protobuf"

import * as invocation_pb from './invocation_pb';
import * as target_pb from './target_pb';
import * as file_pb from './file_pb';

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

  getTool(): string;
  setTool(value: string): SearchInvocationsRequest;

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
    tool: string,
  }

  export enum PageStartCase { 
    PAGE_START_NOT_SET = 0,
    PAGE_TOKEN = 2,
    OFFSET = 3,
  }
}

export class SearchInvocationsResponse extends jspb.Message {
  getInvocationsList(): Array<invocation_pb.Invocation>;
  setInvocationsList(value: Array<invocation_pb.Invocation>): SearchInvocationsResponse;
  clearInvocationsList(): SearchInvocationsResponse;
  addInvocations(value?: invocation_pb.Invocation, index?: number): invocation_pb.Invocation;

  getNextPageToken(): string;
  setNextPageToken(value: string): SearchInvocationsResponse;

  getToolsListList(): Array<string>;
  setToolsListList(value: Array<string>): SearchInvocationsResponse;
  clearToolsListList(): SearchInvocationsResponse;
  addToolsList(value: string, index?: number): SearchInvocationsResponse;

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
    toolsListList: Array<string>,
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

export class ListTargetsRequest extends jspb.Message {
  getParent(): string;
  setParent(value: string): ListTargetsRequest;

  getPageSize(): number;
  setPageSize(value: number): ListTargetsRequest;

  getPageToken(): string;
  setPageToken(value: string): ListTargetsRequest;

  getOffset(): number;
  setOffset(value: number): ListTargetsRequest;

  getFilter(): string;
  setFilter(value: string): ListTargetsRequest;

  getPageStartCase(): ListTargetsRequest.PageStartCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListTargetsRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListTargetsRequest): ListTargetsRequest.AsObject;
  static serializeBinaryToWriter(message: ListTargetsRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListTargetsRequest;
  static deserializeBinaryFromReader(message: ListTargetsRequest, reader: jspb.BinaryReader): ListTargetsRequest;
}

export namespace ListTargetsRequest {
  export type AsObject = {
    parent: string,
    pageSize: number,
    pageToken: string,
    offset: number,
    filter: string,
  }

  export enum PageStartCase { 
    PAGE_START_NOT_SET = 0,
    PAGE_TOKEN = 3,
    OFFSET = 4,
  }
}

export class ListTargetsResponse extends jspb.Message {
  getTargetsList(): Array<target_pb.Target>;
  setTargetsList(value: Array<target_pb.Target>): ListTargetsResponse;
  clearTargetsList(): ListTargetsResponse;
  addTargets(value?: target_pb.Target, index?: number): target_pb.Target;

  getNextPageToken(): string;
  setNextPageToken(value: string): ListTargetsResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListTargetsResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListTargetsResponse): ListTargetsResponse.AsObject;
  static serializeBinaryToWriter(message: ListTargetsResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListTargetsResponse;
  static deserializeBinaryFromReader(message: ListTargetsResponse, reader: jspb.BinaryReader): ListTargetsResponse;
}

export namespace ListTargetsResponse {
  export type AsObject = {
    targetsList: Array<target_pb.Target.AsObject>,
    nextPageToken: string,
  }
}

export class ListTargetSubFilesRequest extends jspb.Message {
  getParent(): string;
  setParent(value: string): ListTargetSubFilesRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListTargetSubFilesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: ListTargetSubFilesRequest): ListTargetSubFilesRequest.AsObject;
  static serializeBinaryToWriter(message: ListTargetSubFilesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListTargetSubFilesRequest;
  static deserializeBinaryFromReader(message: ListTargetSubFilesRequest, reader: jspb.BinaryReader): ListTargetSubFilesRequest;
}

export namespace ListTargetSubFilesRequest {
  export type AsObject = {
    parent: string,
  }
}

export class ListTargetSubFilesResponse extends jspb.Message {
  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): ListTargetSubFilesResponse;
  clearFilesList(): ListTargetSubFilesResponse;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ListTargetSubFilesResponse.AsObject;
  static toObject(includeInstance: boolean, msg: ListTargetSubFilesResponse): ListTargetSubFilesResponse.AsObject;
  static serializeBinaryToWriter(message: ListTargetSubFilesResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ListTargetSubFilesResponse;
  static deserializeBinaryFromReader(message: ListTargetSubFilesResponse, reader: jspb.BinaryReader): ListTargetSubFilesResponse;
}

export namespace ListTargetSubFilesResponse {
  export type AsObject = {
    filesList: Array<file_pb.File.AsObject>,
  }
}

export class GetFileRequest extends jspb.Message {
  getUri(): string;
  setUri(value: string): GetFileRequest;

  getReadOffset(): number;
  setReadOffset(value: number): GetFileRequest;

  getReadLimit(): number;
  setReadLimit(value: number): GetFileRequest;

  getArchiveEntry(): string;
  setArchiveEntry(value: string): GetFileRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFileRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetFileRequest): GetFileRequest.AsObject;
  static serializeBinaryToWriter(message: GetFileRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFileRequest;
  static deserializeBinaryFromReader(message: GetFileRequest, reader: jspb.BinaryReader): GetFileRequest;
}

export namespace GetFileRequest {
  export type AsObject = {
    uri: string,
    readOffset: number,
    readLimit: number,
    archiveEntry: string,
  }
}

export class GetFileResponse extends jspb.Message {
  getData(): Uint8Array | string;
  getData_asU8(): Uint8Array;
  getData_asB64(): string;
  setData(value: Uint8Array | string): GetFileResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetFileResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetFileResponse): GetFileResponse.AsObject;
  static serializeBinaryToWriter(message: GetFileResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetFileResponse;
  static deserializeBinaryFromReader(message: GetFileResponse, reader: jspb.BinaryReader): GetFileResponse;
}

export namespace GetFileResponse {
  export type AsObject = {
    data: Uint8Array | string,
  }
}

export class GetInitialStateRequest extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetInitialStateRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetInitialStateRequest): GetInitialStateRequest.AsObject;
  static serializeBinaryToWriter(message: GetInitialStateRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetInitialStateRequest;
  static deserializeBinaryFromReader(message: GetInitialStateRequest, reader: jspb.BinaryReader): GetInitialStateRequest;
}

export namespace GetInitialStateRequest {
  export type AsObject = {
  }
}

export class GetInitialStateResponse extends jspb.Message {
  getToolsListList(): Array<string>;
  setToolsListList(value: Array<string>): GetInitialStateResponse;
  clearToolsListList(): GetInitialStateResponse;
  addToolsList(value: string, index?: number): GetInitialStateResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetInitialStateResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetInitialStateResponse): GetInitialStateResponse.AsObject;
  static serializeBinaryToWriter(message: GetInitialStateResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetInitialStateResponse;
  static deserializeBinaryFromReader(message: GetInitialStateResponse, reader: jspb.BinaryReader): GetInitialStateResponse;
}

export namespace GetInitialStateResponse {
  export type AsObject = {
    toolsListList: Array<string>,
  }
}

export class DownloadFileRequest extends jspb.Message {
  getFileName(): string;
  setFileName(value: string): DownloadFileRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DownloadFileRequest.AsObject;
  static toObject(includeInstance: boolean, msg: DownloadFileRequest): DownloadFileRequest.AsObject;
  static serializeBinaryToWriter(message: DownloadFileRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DownloadFileRequest;
  static deserializeBinaryFromReader(message: DownloadFileRequest, reader: jspb.BinaryReader): DownloadFileRequest;
}

export namespace DownloadFileRequest {
  export type AsObject = {
    fileName: string,
  }
}

export class DownloadFileResponse extends jspb.Message {
  getFileData(): string;
  setFileData(value: string): DownloadFileResponse;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): DownloadFileResponse.AsObject;
  static toObject(includeInstance: boolean, msg: DownloadFileResponse): DownloadFileResponse.AsObject;
  static serializeBinaryToWriter(message: DownloadFileResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): DownloadFileResponse;
  static deserializeBinaryFromReader(message: DownloadFileResponse, reader: jspb.BinaryReader): DownloadFileResponse;
}

export namespace DownloadFileResponse {
  export type AsObject = {
    fileData: string,
  }
}

export class TestSuiteFilter extends jspb.Message {
  getTestSuiteName(): string;
  setTestSuiteName(value: string): TestSuiteFilter;

  getToolTag(): string;
  setToolTag(value: string): TestSuiteFilter;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestSuiteFilter.AsObject;
  static toObject(includeInstance: boolean, msg: TestSuiteFilter): TestSuiteFilter.AsObject;
  static serializeBinaryToWriter(message: TestSuiteFilter, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestSuiteFilter;
  static deserializeBinaryFromReader(message: TestSuiteFilter, reader: jspb.BinaryReader): TestSuiteFilter;
}

export namespace TestSuiteFilter {
  export type AsObject = {
    testSuiteName: string,
    toolTag: string,
  }
}

export class GetTestCasesRequest extends jspb.Message {
  getPageSize(): number;
  setPageSize(value: number): GetTestCasesRequest;

  getInvocationsList(): Array<invocation_pb.Invocation>;
  setInvocationsList(value: Array<invocation_pb.Invocation>): GetTestCasesRequest;
  clearInvocationsList(): GetTestCasesRequest;
  addInvocations(value?: invocation_pb.Invocation, index?: number): invocation_pb.Invocation;

  getPageToken(): string;
  setPageToken(value: string): GetTestCasesRequest;

  getQuery(): string;
  setQuery(value: string): GetTestCasesRequest;

  getProjectId(): string;
  setProjectId(value: string): GetTestCasesRequest;

  getTool(): string;
  setTool(value: string): GetTestCasesRequest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetTestCasesRequest.AsObject;
  static toObject(includeInstance: boolean, msg: GetTestCasesRequest): GetTestCasesRequest.AsObject;
  static serializeBinaryToWriter(message: GetTestCasesRequest, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetTestCasesRequest;
  static deserializeBinaryFromReader(message: GetTestCasesRequest, reader: jspb.BinaryReader): GetTestCasesRequest;
}

export namespace GetTestCasesRequest {
  export type AsObject = {
    pageSize: number,
    invocationsList: Array<invocation_pb.Invocation.AsObject>,
    pageToken: string,
    query: string,
    projectId: string,
    tool: string,
  }
}

export class GetTestCasesResponse extends jspb.Message {
  getInvocationTestsList(): Array<invocation_pb.InvocationTest>;
  setInvocationTestsList(value: Array<invocation_pb.InvocationTest>): GetTestCasesResponse;
  clearInvocationTestsList(): GetTestCasesResponse;
  addInvocationTests(value?: invocation_pb.InvocationTest, index?: number): invocation_pb.InvocationTest;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): GetTestCasesResponse.AsObject;
  static toObject(includeInstance: boolean, msg: GetTestCasesResponse): GetTestCasesResponse.AsObject;
  static serializeBinaryToWriter(message: GetTestCasesResponse, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): GetTestCasesResponse;
  static deserializeBinaryFromReader(message: GetTestCasesResponse, reader: jspb.BinaryReader): GetTestCasesResponse;
}

export namespace GetTestCasesResponse {
  export type AsObject = {
    invocationTestsList: Array<invocation_pb.InvocationTest.AsObject>,
  }
}

