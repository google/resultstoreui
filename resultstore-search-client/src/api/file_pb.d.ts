import * as jspb from "google-protobuf"

import * as wrappers_pb from './wrappers_pb';

export class File extends jspb.Message {
  getUid(): string;
  setUid(value: string): File;

  getUri(): string;
  setUri(value: string): File;

  getLength(): wrappers_pb.Int64Value | undefined;
  setLength(value?: wrappers_pb.Int64Value): File;
  hasLength(): boolean;
  clearLength(): File;

  getContentType(): string;
  setContentType(value: string): File;

  getArchiveEntry(): ArchiveEntry | undefined;
  setArchiveEntry(value?: ArchiveEntry): File;
  hasArchiveEntry(): boolean;
  clearArchiveEntry(): File;

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

  getLength(): wrappers_pb.Int64Value | undefined;
  setLength(value?: wrappers_pb.Int64Value): ArchiveEntry;
  hasLength(): boolean;
  clearLength(): ArchiveEntry;

  getContentType(): string;
  setContentType(value: string): ArchiveEntry;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ArchiveEntry.AsObject;
  static toObject(includeInstance: boolean, msg: ArchiveEntry): ArchiveEntry.AsObject;
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

