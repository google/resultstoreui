// package: resultstoresearch.v1
// file: file.proto

/* tslint:disable */
/* eslint-disable */

import * as jspb from "google-protobuf";
import * as wrappers_pb from "./wrappers_pb";

export class File extends jspb.Message { 
    getUid(): string;
    setUid(value: string): File;

    getUri(): string;
    setUri(value: string): File;


    hasLength(): boolean;
    clearLength(): void;
    getLength(): wrappers_pb.Int64Value | undefined;
    setLength(value?: wrappers_pb.Int64Value): File;

    getContentType(): string;
    setContentType(value: string): File;


    hasArchiveEntry(): boolean;
    clearArchiveEntry(): void;
    getArchiveEntry(): ArchiveEntry | undefined;
    setArchiveEntry(value?: ArchiveEntry): File;

    getContentViewer(): string;
    setContentViewer(value: string): File;

    getHidden(): boolean;
    setHidden(value: boolean): File;

    getDescription(): string;
    setDescription(value: string): File;

    getDigest(): string;
    setDigest(value: string): File;

    getHashType(): File.HashType;
    setHashType(value: File.HashType): File;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): File.AsObject;
    static toObject(includeInstance: boolean, msg: File): File.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: File, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): File;
    static deserializeBinaryFromReader(message: File, reader: jspb.BinaryReader): File;
}

export namespace File {
    export type AsObject = {
        uid: string,
        uri: string,
        length?: wrappers_pb.Int64Value.AsObject,
        contentType: string,
        archiveEntry?: ArchiveEntry.AsObject,
        contentViewer: string,
        hidden: boolean,
        description: string,
        digest: string,
        hashType: File.HashType,
    }

    export enum HashType {
    HASH_TYPE_UNSPECIFIED = 0,
    MD5 = 1,
    SHA1 = 2,
    SHA256 = 3,
    }

}

export class ArchiveEntry extends jspb.Message { 
    getPath(): string;
    setPath(value: string): ArchiveEntry;


    hasLength(): boolean;
    clearLength(): void;
    getLength(): wrappers_pb.Int64Value | undefined;
    setLength(value?: wrappers_pb.Int64Value): ArchiveEntry;

    getContentType(): string;
    setContentType(value: string): ArchiveEntry;


    serializeBinary(): Uint8Array;
    toObject(includeInstance?: boolean): ArchiveEntry.AsObject;
    static toObject(includeInstance: boolean, msg: ArchiveEntry): ArchiveEntry.AsObject;
    static extensions: {[key: number]: jspb.ExtensionFieldInfo<jspb.Message>};
    static extensionsBinary: {[key: number]: jspb.ExtensionFieldBinaryInfo<jspb.Message>};
    static serializeBinaryToWriter(message: ArchiveEntry, writer: jspb.BinaryWriter): void;
    static deserializeBinary(bytes: Uint8Array): ArchiveEntry;
    static deserializeBinaryFromReader(message: ArchiveEntry, reader: jspb.BinaryReader): ArchiveEntry;
}

export namespace ArchiveEntry {
    export type AsObject = {
        path: string,
        length?: wrappers_pb.Int64Value.AsObject,
        contentType: string,
    }
}
