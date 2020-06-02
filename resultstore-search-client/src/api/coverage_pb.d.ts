// package: resultstoresearch.v1
// file: coverage.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";

export class LineCoverage extends jspb.Message { 
    getInstrumentedLines(): Uint8Array | string;
    getInstrumentedLines_asU8(): Uint8Array;
    getInstrumentedLines_asB64(): string;
    setInstrumentedLines(value: Uint8Array | string): LineCoverage;

    getExecutedLines(): Uint8Array | string;
    getExecutedLines_asU8(): Uint8Array;
    getExecutedLines_asB64(): string;
    setExecutedLines(value: Uint8Array | string): LineCoverage;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): LineCoverage.AsObject;
    static toObject(includeInstance: boolean, msg: LineCoverage): LineCoverage.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: LineCoverage, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): LineCoverage;
    static deserializeBinaryFromReader(message: LineCoverage, reader: jspb.BinaryReader): LineCoverage;
}

export namespace LineCoverage {
    export type AsObject = {
        instrumentedLines: Uint8Array | string,
        executedLines: Uint8Array | string,
    }
}

export class BranchCoverage extends jspb.Message { 
    getBranchPresent(): Uint8Array | string;
    getBranchPresent_asU8(): Uint8Array;
    getBranchPresent_asB64(): string;
    setBranchPresent(value: Uint8Array | string): BranchCoverage;

    clearBranchesInLineList(): void;
    getBranchesInLineList(): Array<number>;
    setBranchesInLineList(value: Array<number>): BranchCoverage;
    addBranchesInLine(value: number, index?: number): number;

    getExecuted(): Uint8Array | string;
    getExecuted_asU8(): Uint8Array;
    getExecuted_asB64(): string;
    setExecuted(value: Uint8Array | string): BranchCoverage;

    getTaken(): Uint8Array | string;
    getTaken_asU8(): Uint8Array;
    getTaken_asB64(): string;
    setTaken(value: Uint8Array | string): BranchCoverage;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): BranchCoverage.AsObject;
    static toObject(includeInstance: boolean, msg: BranchCoverage): BranchCoverage.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: BranchCoverage, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): BranchCoverage;
    static deserializeBinaryFromReader(message: BranchCoverage, reader: jspb.BinaryReader): BranchCoverage;
}

export namespace BranchCoverage {
    export type AsObject = {
        branchPresent: Uint8Array | string,
        branchesInLineList: Array<number>,
        executed: Uint8Array | string,
        taken: Uint8Array | string,
    }
}

export class FileCoverage extends jspb.Message { 
    getPath(): string;
    setPath(value: string): FileCoverage;


    hasLineCoverage(): boolean;
    clearLineCoverage(): void;
    getLineCoverage(): LineCoverage | undefined;
    setLineCoverage(value?: LineCoverage): FileCoverage;


    hasBranchCoverage(): boolean;
    clearBranchCoverage(): void;
    getBranchCoverage(): BranchCoverage | undefined;
    setBranchCoverage(value?: BranchCoverage): FileCoverage;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): FileCoverage.AsObject;
    static toObject(includeInstance: boolean, msg: FileCoverage): FileCoverage.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: FileCoverage, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): FileCoverage;
    static deserializeBinaryFromReader(message: FileCoverage, reader: jspb.BinaryReader): FileCoverage;
}

export namespace FileCoverage {
    export type AsObject = {
        path: string,
        lineCoverage?: LineCoverage.AsObject,
        branchCoverage?: BranchCoverage.AsObject,
    }
}

export class ActionCoverage extends jspb.Message { 
    clearFileCoveragesList(): void;
    getFileCoveragesList(): Array<FileCoverage>;
    setFileCoveragesList(value: Array<FileCoverage>): ActionCoverage;
    addFileCoverages(value?: FileCoverage, index?: number): FileCoverage;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): ActionCoverage.AsObject;
    static toObject(includeInstance: boolean, msg: ActionCoverage): ActionCoverage.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: ActionCoverage, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): ActionCoverage;
    static deserializeBinaryFromReader(message: ActionCoverage, reader: jspb.BinaryReader): ActionCoverage;
}

export namespace ActionCoverage {
    export type AsObject = {
        fileCoveragesList: Array<FileCoverage.AsObject>,
    }
}

export class AggregateCoverage extends jspb.Message { 
    clearFileCoveragesList(): void;
    getFileCoveragesList(): Array<FileCoverage>;
    setFileCoveragesList(value: Array<FileCoverage>): AggregateCoverage;
    addFileCoverages(value?: FileCoverage, index?: number): FileCoverage;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): AggregateCoverage.AsObject;
    static toObject(includeInstance: boolean, msg: AggregateCoverage): AggregateCoverage.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: AggregateCoverage, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): AggregateCoverage;
    static deserializeBinaryFromReader(message: AggregateCoverage, reader: jspb.BinaryReader): AggregateCoverage;
}

export namespace AggregateCoverage {
    export type AsObject = {
        fileCoveragesList: Array<FileCoverage.AsObject>,
    }
}
