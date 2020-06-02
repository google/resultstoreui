import * as jspb from "google-protobuf"

import * as common_pb from './common_pb';
import * as coverage_pb from './coverage_pb';
import * as coverage_summary_pb from './coverage_summary_pb';
import * as file_pb from './file_pb';
import * as file_processing_error_pb from './file_processing_error_pb';

export class Invocation extends jspb.Message {
  getName(): string;
  setName(value: string): Invocation;

  getId(): Id | undefined;
  setId(value?: Id): Invocation;
  hasId(): boolean;
  clearId(): Invocation;

  getStatusAttributes(): common_pb.StatusAttributes | undefined;
  setStatusAttributes(value?: common_pb.StatusAttributes): Invocation;
  hasStatusAttributes(): boolean;
  clearStatusAttributes(): Invocation;

  getTiming(): common_pb.Timing | undefined;
  setTiming(value?: common_pb.Timing): Invocation;
  hasTiming(): boolean;
  clearTiming(): Invocation;

  getInvocationAttributes(): InvocationAttributes | undefined;
  setInvocationAttributes(value?: InvocationAttributes): Invocation;
  hasInvocationAttributes(): boolean;
  clearInvocationAttributes(): Invocation;

  getWorkspaceInfo(): WorkspaceInfo | undefined;
  setWorkspaceInfo(value?: WorkspaceInfo): Invocation;
  hasWorkspaceInfo(): boolean;
  clearWorkspaceInfo(): Invocation;

  getPropertiesList(): Array<common_pb.Property>;
  setPropertiesList(value: Array<common_pb.Property>): Invocation;
  clearPropertiesList(): Invocation;
  addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): Invocation;
  clearFilesList(): Invocation;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  getCoverageSummariesList(): Array<coverage_summary_pb.LanguageCoverageSummary>;
  setCoverageSummariesList(value: Array<coverage_summary_pb.LanguageCoverageSummary>): Invocation;
  clearCoverageSummariesList(): Invocation;
  addCoverageSummaries(value?: coverage_summary_pb.LanguageCoverageSummary, index?: number): coverage_summary_pb.LanguageCoverageSummary;

  getAggregateCoverage(): coverage_pb.AggregateCoverage | undefined;
  setAggregateCoverage(value?: coverage_pb.AggregateCoverage): Invocation;
  hasAggregateCoverage(): boolean;
  clearAggregateCoverage(): Invocation;

  getFileProcessingErrorsList(): Array<file_processing_error_pb.FileProcessingErrors>;
  setFileProcessingErrorsList(value: Array<file_processing_error_pb.FileProcessingErrors>): Invocation;
  clearFileProcessingErrorsList(): Invocation;
  addFileProcessingErrors(value?: file_processing_error_pb.FileProcessingErrors, index?: number): file_processing_error_pb.FileProcessingErrors;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Invocation.AsObject;
  static toObject(includeInstance: boolean, msg: Invocation): Invocation.AsObject;
  static serializeBinaryToWriter(message: Invocation, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Invocation;
  static deserializeBinaryFromReader(message: Invocation, reader: jspb.BinaryReader): Invocation;
}

export namespace Invocation {
  export type AsObject = {
    name: string,
    id?: Id.AsObject,
    statusAttributes?: common_pb.StatusAttributes.AsObject,
    timing?: common_pb.Timing.AsObject,
    invocationAttributes?: InvocationAttributes.AsObject,
    workspaceInfo?: WorkspaceInfo.AsObject,
    propertiesList: Array<common_pb.Property.AsObject>,
    filesList: Array<file_pb.File.AsObject>,
    coverageSummariesList: Array<coverage_summary_pb.LanguageCoverageSummary.AsObject>,
    aggregateCoverage?: coverage_pb.AggregateCoverage.AsObject,
    fileProcessingErrorsList: Array<file_processing_error_pb.FileProcessingErrors.AsObject>,
  }

  export class Id extends jspb.Message {
    getInvocationId(): string;
    setInvocationId(value: string): Id;

    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Id.AsObject;
    static toObject(includeInstance: boolean, msg: Id): Id.AsObject;
    static serializeBinaryToWriter(message: Id, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Id;
    static deserializeBinaryFromReader(message: Id, reader: jspb.BinaryReader): Id;
  }

  export namespace Id {
    export type AsObject = {
      invocationId: string,
    }
  }

}

export class WorkspaceContext extends jspb.Message {
  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): WorkspaceContext.AsObject;
  static toObject(includeInstance: boolean, msg: WorkspaceContext): WorkspaceContext.AsObject;
  static serializeBinaryToWriter(message: WorkspaceContext, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): WorkspaceContext;
  static deserializeBinaryFromReader(message: WorkspaceContext, reader: jspb.BinaryReader): WorkspaceContext;
}

export namespace WorkspaceContext {
  export type AsObject = {
  }
}

export class WorkspaceInfo extends jspb.Message {
  getWorkspaceContext(): WorkspaceContext | undefined;
  setWorkspaceContext(value?: WorkspaceContext): WorkspaceInfo;
  hasWorkspaceContext(): boolean;
  clearWorkspaceContext(): WorkspaceInfo;

  getHostname(): string;
  setHostname(value: string): WorkspaceInfo;

  getWorkingDirectory(): string;
  setWorkingDirectory(value: string): WorkspaceInfo;

  getToolTag(): string;
  setToolTag(value: string): WorkspaceInfo;

  getCommandLinesList(): Array<CommandLine>;
  setCommandLinesList(value: Array<CommandLine>): WorkspaceInfo;
  clearCommandLinesList(): WorkspaceInfo;
  addCommandLines(value?: CommandLine, index?: number): CommandLine;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): WorkspaceInfo.AsObject;
  static toObject(includeInstance: boolean, msg: WorkspaceInfo): WorkspaceInfo.AsObject;
  static serializeBinaryToWriter(message: WorkspaceInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): WorkspaceInfo;
  static deserializeBinaryFromReader(message: WorkspaceInfo, reader: jspb.BinaryReader): WorkspaceInfo;
}

export namespace WorkspaceInfo {
  export type AsObject = {
    workspaceContext?: WorkspaceContext.AsObject,
    hostname: string,
    workingDirectory: string,
    toolTag: string,
    commandLinesList: Array<CommandLine.AsObject>,
  }
}

export class CommandLine extends jspb.Message {
  getLabel(): string;
  setLabel(value: string): CommandLine;

  getTool(): string;
  setTool(value: string): CommandLine;

  getArgsList(): Array<string>;
  setArgsList(value: Array<string>): CommandLine;
  clearArgsList(): CommandLine;
  addArgs(value: string, index?: number): CommandLine;

  getCommand(): string;
  setCommand(value: string): CommandLine;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): CommandLine.AsObject;
  static toObject(includeInstance: boolean, msg: CommandLine): CommandLine.AsObject;
  static serializeBinaryToWriter(message: CommandLine, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): CommandLine;
  static deserializeBinaryFromReader(message: CommandLine, reader: jspb.BinaryReader): CommandLine;
}

export namespace CommandLine {
  export type AsObject = {
    label: string,
    tool: string,
    argsList: Array<string>,
    command: string,
  }
}

export class InvocationAttributes extends jspb.Message {
  getProjectId(): string;
  setProjectId(value: string): InvocationAttributes;

  getUsersList(): Array<string>;
  setUsersList(value: Array<string>): InvocationAttributes;
  clearUsersList(): InvocationAttributes;
  addUsers(value: string, index?: number): InvocationAttributes;

  getLabelsList(): Array<string>;
  setLabelsList(value: Array<string>): InvocationAttributes;
  clearLabelsList(): InvocationAttributes;
  addLabels(value: string, index?: number): InvocationAttributes;

  getDescription(): string;
  setDescription(value: string): InvocationAttributes;

  getInvocationContextsList(): Array<InvocationContext>;
  setInvocationContextsList(value: Array<InvocationContext>): InvocationAttributes;
  clearInvocationContextsList(): InvocationAttributes;
  addInvocationContexts(value?: InvocationContext, index?: number): InvocationContext;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InvocationAttributes.AsObject;
  static toObject(includeInstance: boolean, msg: InvocationAttributes): InvocationAttributes.AsObject;
  static serializeBinaryToWriter(message: InvocationAttributes, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InvocationAttributes;
  static deserializeBinaryFromReader(message: InvocationAttributes, reader: jspb.BinaryReader): InvocationAttributes;
}

export namespace InvocationAttributes {
  export type AsObject = {
    projectId: string,
    usersList: Array<string>,
    labelsList: Array<string>,
    description: string,
    invocationContextsList: Array<InvocationContext.AsObject>,
  }
}

export class InvocationContext extends jspb.Message {
  getDisplayName(): string;
  setDisplayName(value: string): InvocationContext;

  getUrl(): string;
  setUrl(value: string): InvocationContext;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InvocationContext.AsObject;
  static toObject(includeInstance: boolean, msg: InvocationContext): InvocationContext.AsObject;
  static serializeBinaryToWriter(message: InvocationContext, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InvocationContext;
  static deserializeBinaryFromReader(message: InvocationContext, reader: jspb.BinaryReader): InvocationContext;
}

export namespace InvocationContext {
  export type AsObject = {
    displayName: string,
    url: string,
  }
}

