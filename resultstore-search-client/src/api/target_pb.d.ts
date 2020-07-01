import * as jspb from "google-protobuf"

import * as common_pb from './common_pb';
import * as file_pb from './file_pb';

export class Target extends jspb.Message {
  getName(): string;
  setName(value: string): Target;

  getId(): Id | undefined;
  setId(value?: Id): Target;
  hasId(): boolean;
  clearId(): Target;

  getStatusAttributes(): common_pb.StatusAttributes | undefined;
  setStatusAttributes(value?: common_pb.StatusAttributes): Target;
  hasStatusAttributes(): boolean;
  clearStatusAttributes(): Target;

  getTiming(): common_pb.Timing | undefined;
  setTiming(value?: common_pb.Timing): Target;
  hasTiming(): boolean;
  clearTiming(): Target;

  getTargetAttributes(): TargetAttributes | undefined;
  setTargetAttributes(value?: TargetAttributes): Target;
  hasTargetAttributes(): boolean;
  clearTargetAttributes(): Target;

  getTestAttributes(): TestAttributes | undefined;
  setTestAttributes(value?: TestAttributes): Target;
  hasTestAttributes(): boolean;
  clearTestAttributes(): Target;

  getPropertiesList(): Array<common_pb.Property>;
  setPropertiesList(value: Array<common_pb.Property>): Target;
  clearPropertiesList(): Target;
  addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): Target;
  clearFilesList(): Target;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  getVisible(): boolean;
  setVisible(value: boolean): Target;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Target.AsObject;
  static toObject(includeInstance: boolean, msg: Target): Target.AsObject;
  static serializeBinaryToWriter(message: Target, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Target;
  static deserializeBinaryFromReader(message: Target, reader: jspb.BinaryReader): Target;
}

export namespace Target {
  export type AsObject = {
    name: string,
    id?: Id.AsObject,
    statusAttributes?: common_pb.StatusAttributes.AsObject,
    timing?: common_pb.Timing.AsObject,
    targetAttributes?: TargetAttributes.AsObject,
    testAttributes?: TestAttributes.AsObject,
    propertiesList: Array<common_pb.Property.AsObject>,
    filesList: Array<file_pb.File.AsObject>,
    visible: boolean,
  }

  export class Id extends jspb.Message {
    getInvocationId(): string;
    setInvocationId(value: string): Id;

    getTargetId(): string;
    setTargetId(value: string): Id;

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
      targetId: string,
    }
  }

}

export class TargetAttributes extends jspb.Message {
  getType(): TargetType;
  setType(value: TargetType): TargetAttributes;

  getLanguage(): common_pb.Language;
  setLanguage(value: common_pb.Language): TargetAttributes;

  getTagsList(): Array<string>;
  setTagsList(value: Array<string>): TargetAttributes;
  clearTagsList(): TargetAttributes;
  addTags(value: string, index?: number): TargetAttributes;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TargetAttributes.AsObject;
  static toObject(includeInstance: boolean, msg: TargetAttributes): TargetAttributes.AsObject;
  static serializeBinaryToWriter(message: TargetAttributes, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TargetAttributes;
  static deserializeBinaryFromReader(message: TargetAttributes, reader: jspb.BinaryReader): TargetAttributes;
}

export namespace TargetAttributes {
  export type AsObject = {
    type: TargetType,
    language: common_pb.Language,
    tagsList: Array<string>,
  }
}

export class TestAttributes extends jspb.Message {
  getSize(): TestSize;
  setSize(value: TestSize): TestAttributes;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestAttributes.AsObject;
  static toObject(includeInstance: boolean, msg: TestAttributes): TestAttributes.AsObject;
  static serializeBinaryToWriter(message: TestAttributes, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestAttributes;
  static deserializeBinaryFromReader(message: TestAttributes, reader: jspb.BinaryReader): TestAttributes;
}

export namespace TestAttributes {
  export type AsObject = {
    size: TestSize,
  }
}

export enum TargetType { 
  TARGET_TYPE_UNSPECIFIED = 0,
  APPLICATION = 1,
  BINARY = 2,
  LIBRARY = 3,
  PACKAGE = 4,
  TEST = 5,
}
export enum TestSize { 
  TEST_SIZE_UNSPECIFIED = 0,
  SMALL = 1,
  MEDIUM = 2,
  LARGE = 3,
  ENORMOUS = 4,
  OTHER_SIZE = 5,
}
