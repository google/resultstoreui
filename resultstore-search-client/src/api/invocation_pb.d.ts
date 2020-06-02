// package: resultstoresearch.v1
// file: invocation.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";
import * as common_pb from "./common_pb";
import * as coverage_pb from "./coverage_pb";
import * as coverage_summary_pb from "./coverage_summary_pb";
import * as file_pb from "./file_pb";
import * as file_processing_error_pb from "./file_processing_error_pb";

export class Invocation extends jspb.Message { 
    getName(): string;
    setName(value: string): Invocation;


    hasId(): boolean;
    clearId(): void;
    getId(): Invocation.Id | undefined;
    setId(value?: Invocation.Id): Invocation;


    hasStatusAttributes(): boolean;
    clearStatusAttributes(): void;
    getStatusAttributes(): common_pb.StatusAttributes | undefined;
    setStatusAttributes(value?: common_pb.StatusAttributes): Invocation;


    hasTiming(): boolean;
    clearTiming(): void;
    getTiming(): common_pb.Timing | undefined;
    setTiming(value?: common_pb.Timing): Invocation;


    hasInvocationAttributes(): boolean;
    clearInvocationAttributes(): void;
    getInvocationAttributes(): InvocationAttributes | undefined;
    setInvocationAttributes(value?: InvocationAttributes): Invocation;


    hasWorkspaceInfo(): boolean;
    clearWorkspaceInfo(): void;
    getWorkspaceInfo(): WorkspaceInfo | undefined;
    setWorkspaceInfo(value?: WorkspaceInfo): Invocation;

    clearPropertiesList(): void;
    getPropertiesList(): Array<common_pb.Property>;
    setPropertiesList(value: Array<common_pb.Property>): Invocation;
    addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

    clearFilesList(): void;
    getFilesList(): Array<file_pb.File>;
    setFilesList(value: Array<file_pb.File>): Invocation;
    addFiles(value?: file_pb.File, index?: number): file_pb.File;

    clearCoverageSummariesList(): void;
    getCoverageSummariesList(): Array<coverage_summary_pb.LanguageCoverageSummary>;
    setCoverageSummariesList(value: Array<coverage_summary_pb.LanguageCoverageSummary>): Invocation;
    addCoverageSummaries(value?: coverage_summary_pb.LanguageCoverageSummary, index?: number): coverage_summary_pb.LanguageCoverageSummary;


    hasAggregateCoverage(): boolean;
    clearAggregateCoverage(): void;
    getAggregateCoverage(): coverage_pb.AggregateCoverage | undefined;
    setAggregateCoverage(value?: coverage_pb.AggregateCoverage): Invocation;

    clearFileProcessingErrorsList(): void;
    getFileProcessingErrorsList(): Array<file_processing_error_pb.FileProcessingErrors>;
    setFileProcessingErrorsList(value: Array<file_processing_error_pb.FileProcessingErrors>): Invocation;
    addFileProcessingErrors(value?: file_processing_error_pb.FileProcessingErrors, index?: number): file_processing_error_pb.FileProcessingErrors;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): Invocation.AsObject;
    static toObject(includeInstance: boolean, msg: Invocation): Invocation.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: Invocation, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): Invocation;
    static deserializeBinaryFromReader(message: Invocation, reader: jspb.BinaryReader): Invocation;
}

export namespace Invocation {
    export type AsObject = {
        name: string,
        id?: Invocation.Id.AsObject,
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
        static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
        static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
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
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: WorkspaceContext, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): WorkspaceContext;
    static deserializeBinaryFromReader(message: WorkspaceContext, reader: jspb.BinaryReader): WorkspaceContext;
}

export namespace WorkspaceContext {
    export type AsObject = {
    }
}

export class WorkspaceInfo extends jspb.Message { 

    hasWorkspaceContext(): boolean;
    clearWorkspaceContext(): void;
    getWorkspaceContext(): WorkspaceContext | undefined;
    setWorkspaceContext(value?: WorkspaceContext): WorkspaceInfo;

    getHostname(): string;
    setHostname(value: string): WorkspaceInfo;

    getWorkingDirectory(): string;
    setWorkingDirectory(value: string): WorkspaceInfo;

    getToolTag(): string;
    setToolTag(value: string): WorkspaceInfo;

    clearCommandLinesList(): void;
    getCommandLinesList(): Array<CommandLine>;
    setCommandLinesList(value: Array<CommandLine>): WorkspaceInfo;
    addCommandLines(value?: CommandLine, index?: number): CommandLine;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): WorkspaceInfo.AsObject;
    static toObject(includeInstance: boolean, msg: WorkspaceInfo): WorkspaceInfo.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
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

    clearArgsList(): void;
    getArgsList(): Array<string>;
    setArgsList(value: Array<string>): CommandLine;
    addArgs(value: string, index?: number): string;

    getCommand(): string;
    setCommand(value: string): CommandLine;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): CommandLine.AsObject;
    static toObject(includeInstance: boolean, msg: CommandLine): CommandLine.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
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

    clearUsersList(): void;
    getUsersList(): Array<string>;
    setUsersList(value: Array<string>): InvocationAttributes;
    addUsers(value: string, index?: number): string;

    clearLabelsList(): void;
    getLabelsList(): Array<string>;
    setLabelsList(value: Array<string>): InvocationAttributes;
    addLabels(value: string, index?: number): string;

    getDescription(): string;
    setDescription(value: string): InvocationAttributes;

    clearInvocationContextsList(): void;
    getInvocationContextsList(): Array<InvocationContext>;
    setInvocationContextsList(value: Array<InvocationContext>): InvocationAttributes;
    addInvocationContexts(value?: InvocationContext, index?: number): InvocationContext;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): InvocationAttributes.AsObject;
    static toObject(includeInstance: boolean, msg: InvocationAttributes): InvocationAttributes.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
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
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
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
