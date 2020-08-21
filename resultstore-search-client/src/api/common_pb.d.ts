import * as jspb from "google-protobuf"

import * as duration_pb from './duration_pb';
import * as timestamp_pb from './timestamp_pb';

export class StatusAttributes extends jspb.Message {
  getStatus(): Status;
  setStatus(value: Status): StatusAttributes;

  getDescription(): string;
  setDescription(value: string): StatusAttributes;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): StatusAttributes.AsObject;
  static toObject(includeInstance: boolean, msg: StatusAttributes): StatusAttributes.AsObject;
  static serializeBinaryToWriter(message: StatusAttributes, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): StatusAttributes;
  static deserializeBinaryFromReader(message: StatusAttributes, reader: jspb.BinaryReader): StatusAttributes;
}

export namespace StatusAttributes {
  export type AsObject = {
    status: Status,
    description: string,
  }
}

export class Property extends jspb.Message {
  getKey(): string;
  setKey(value: string): Property;

  getValue(): string;
  setValue(value: string): Property;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Property.AsObject;
  static toObject(includeInstance: boolean, msg: Property): Property.AsObject;
  static serializeBinaryToWriter(message: Property, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Property;
  static deserializeBinaryFromReader(message: Property, reader: jspb.BinaryReader): Property;
}

export namespace Property {
  export type AsObject = {
    key: string,
    value: string,
  }
}

export class Timing extends jspb.Message {
  getStartTime(): timestamp_pb.Timestamp | undefined;
  setStartTime(value?: timestamp_pb.Timestamp): Timing;
  hasStartTime(): boolean;
  clearStartTime(): Timing;

  getDuration(): duration_pb.Duration | undefined;
  setDuration(value?: duration_pb.Duration): Timing;
  hasDuration(): boolean;
  clearDuration(): Timing;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Timing.AsObject;
  static toObject(includeInstance: boolean, msg: Timing): Timing.AsObject;
  static serializeBinaryToWriter(message: Timing, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Timing;
  static deserializeBinaryFromReader(message: Timing, reader: jspb.BinaryReader): Timing;
}

export namespace Timing {
  export type AsObject = {
    startTime?: timestamp_pb.Timestamp.AsObject,
    duration?: duration_pb.Duration.AsObject,
  }
}

export class Dependency extends jspb.Message {
  getTarget(): string;
  setTarget(value: string): Dependency;

  getConfiguredTarget(): string;
  setConfiguredTarget(value: string): Dependency;

  getAction(): string;
  setAction(value: string): Dependency;

  getLabel(): string;
  setLabel(value: string): Dependency;

  getResourceCase(): Dependency.ResourceCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Dependency.AsObject;
  static toObject(includeInstance: boolean, msg: Dependency): Dependency.AsObject;
  static serializeBinaryToWriter(message: Dependency, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Dependency;
  static deserializeBinaryFromReader(message: Dependency, reader: jspb.BinaryReader): Dependency;
}

export namespace Dependency {
  export type AsObject = {
    target: string,
    configuredTarget: string,
    action: string,
    label: string,
  }

  export enum ResourceCase { 
    RESOURCE_NOT_SET = 0,
    TARGET = 1,
    CONFIGURED_TARGET = 2,
    ACTION = 3,
  }
}

export enum Language { 
  LANGUAGE_UNSPECIFIED = 0,
  NONE = 1,
  ANDROID = 2,
  AS = 3,
  CC = 4,
  CSS = 5,
  DART = 6,
  GO = 7,
  GWT = 8,
  HASKELL = 9,
  JAVA = 10,
  JS = 11,
  LISP = 12,
  OBJC = 13,
  PY = 14,
  SH = 15,
  SWIFT = 16,
  TS = 18,
  WEB = 19,
  SCALA = 20,
  PROTO = 21,
  XML = 22,
}
export enum Status { 
  STATUS_UNSPECIFIED = 0,
  BUILDING = 1,
  BUILT = 2,
  FAILED_TO_BUILD = 3,
  TESTING = 4,
  PASSED = 5,
  FAILED = 6,
  TIMED_OUT = 7,
  CANCELLED = 8,
  TOOL_FAILED = 9,
  INCOMPLETE = 10,
  FLAKY = 11,
  UNKNOWN = 12,
  SKIPPED = 13,
}
export enum UploadStatus { 
  UPLOAD_STATUS_UNSPECIFIED = 0,
  UPLOADING = 1,
  POST_PROCESSING = 2,
  IMMUTABLE = 3,
}
