import * as jspb from "google-protobuf"

import * as common_pb from './common_pb';
import * as file_pb from './file_pb';

export class TestSuite extends jspb.Message {
  getSuiteName(): string;
  setSuiteName(value: string): TestSuite;

  getTestsList(): Array<Test>;
  setTestsList(value: Array<Test>): TestSuite;
  clearTestsList(): TestSuite;
  addTests(value?: Test, index?: number): Test;

  getFailuresList(): Array<TestFailure>;
  setFailuresList(value: Array<TestFailure>): TestSuite;
  clearFailuresList(): TestSuite;
  addFailures(value?: TestFailure, index?: number): TestFailure;

  getErrorsList(): Array<TestError>;
  setErrorsList(value: Array<TestError>): TestSuite;
  clearErrorsList(): TestSuite;
  addErrors(value?: TestError, index?: number): TestError;

  getTiming(): common_pb.Timing | undefined;
  setTiming(value?: common_pb.Timing): TestSuite;
  hasTiming(): boolean;
  clearTiming(): TestSuite;

  getPropertiesList(): Array<common_pb.Property>;
  setPropertiesList(value: Array<common_pb.Property>): TestSuite;
  clearPropertiesList(): TestSuite;
  addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): TestSuite;
  clearFilesList(): TestSuite;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestSuite.AsObject;
  static toObject(includeInstance: boolean, msg: TestSuite): TestSuite.AsObject;
  static serializeBinaryToWriter(message: TestSuite, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestSuite;
  static deserializeBinaryFromReader(message: TestSuite, reader: jspb.BinaryReader): TestSuite;
}

export namespace TestSuite {
  export type AsObject = {
    suiteName: string,
    testsList: Array<Test.AsObject>,
    failuresList: Array<TestFailure.AsObject>,
    errorsList: Array<TestError.AsObject>,
    timing?: common_pb.Timing.AsObject,
    propertiesList: Array<common_pb.Property.AsObject>,
    filesList: Array<file_pb.File.AsObject>,
  }
}

export class Test extends jspb.Message {
  getTestCase(): TestCase | undefined;
  setTestCase(value?: TestCase): Test;
  hasTestCase(): boolean;
  clearTestCase(): Test;

  getTestSuite(): TestSuite | undefined;
  setTestSuite(value?: TestSuite): Test;
  hasTestSuite(): boolean;
  clearTestSuite(): Test;

  getTestTypeCase(): Test.TestTypeCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Test.AsObject;
  static toObject(includeInstance: boolean, msg: Test): Test.AsObject;
  static serializeBinaryToWriter(message: Test, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Test;
  static deserializeBinaryFromReader(message: Test, reader: jspb.BinaryReader): Test;
}

export namespace Test {
  export type AsObject = {
    testCase?: TestCase.AsObject,
    testSuite?: TestSuite.AsObject,
  }

  export enum TestTypeCase { 
    TEST_TYPE_NOT_SET = 0,
    TEST_CASE = 1,
    TEST_SUITE = 2,
  }
}

export class TestCase extends jspb.Message {
  getCaseName(): string;
  setCaseName(value: string): TestCase;

  getClassName(): string;
  setClassName(value: string): TestCase;

  getResult(): TestCase.Result;
  setResult(value: TestCase.Result): TestCase;

  getFailuresList(): Array<TestFailure>;
  setFailuresList(value: Array<TestFailure>): TestCase;
  clearFailuresList(): TestCase;
  addFailures(value?: TestFailure, index?: number): TestFailure;

  getErrorsList(): Array<TestError>;
  setErrorsList(value: Array<TestError>): TestCase;
  clearErrorsList(): TestCase;
  addErrors(value?: TestError, index?: number): TestError;

  getTiming(): common_pb.Timing | undefined;
  setTiming(value?: common_pb.Timing): TestCase;
  hasTiming(): boolean;
  clearTiming(): TestCase;

  getPropertiesList(): Array<common_pb.Property>;
  setPropertiesList(value: Array<common_pb.Property>): TestCase;
  clearPropertiesList(): TestCase;
  addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): TestCase;
  clearFilesList(): TestCase;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestCase.AsObject;
  static toObject(includeInstance: boolean, msg: TestCase): TestCase.AsObject;
  static serializeBinaryToWriter(message: TestCase, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestCase;
  static deserializeBinaryFromReader(message: TestCase, reader: jspb.BinaryReader): TestCase;
}

export namespace TestCase {
  export type AsObject = {
    caseName: string,
    className: string,
    result: TestCase.Result,
    failuresList: Array<TestFailure.AsObject>,
    errorsList: Array<TestError.AsObject>,
    timing?: common_pb.Timing.AsObject,
    propertiesList: Array<common_pb.Property.AsObject>,
    filesList: Array<file_pb.File.AsObject>,
  }

  export enum Result { 
    RESULT_UNSPECIFIED = 0,
    COMPLETED = 1,
    INTERRUPTED = 2,
    CANCELLED = 3,
    FILTERED = 4,
    SKIPPED = 5,
    SUPPRESSED = 6,
  }
}

export class TestFailure extends jspb.Message {
  getFailureMessage(): string;
  setFailureMessage(value: string): TestFailure;

  getExceptionType(): string;
  setExceptionType(value: string): TestFailure;

  getStackTrace(): string;
  setStackTrace(value: string): TestFailure;

  getExpectedList(): Array<string>;
  setExpectedList(value: Array<string>): TestFailure;
  clearExpectedList(): TestFailure;
  addExpected(value: string, index?: number): TestFailure;

  getActualList(): Array<string>;
  setActualList(value: Array<string>): TestFailure;
  clearActualList(): TestFailure;
  addActual(value: string, index?: number): TestFailure;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestFailure.AsObject;
  static toObject(includeInstance: boolean, msg: TestFailure): TestFailure.AsObject;
  static serializeBinaryToWriter(message: TestFailure, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestFailure;
  static deserializeBinaryFromReader(message: TestFailure, reader: jspb.BinaryReader): TestFailure;
}

export namespace TestFailure {
  export type AsObject = {
    failureMessage: string,
    exceptionType: string,
    stackTrace: string,
    expectedList: Array<string>,
    actualList: Array<string>,
  }
}

export class TestError extends jspb.Message {
  getErrorMessage(): string;
  setErrorMessage(value: string): TestError;

  getExceptionType(): string;
  setExceptionType(value: string): TestError;

  getStackTrace(): string;
  setStackTrace(value: string): TestError;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestError.AsObject;
  static toObject(includeInstance: boolean, msg: TestError): TestError.AsObject;
  static serializeBinaryToWriter(message: TestError, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestError;
  static deserializeBinaryFromReader(message: TestError, reader: jspb.BinaryReader): TestError;
}

export namespace TestError {
  export type AsObject = {
    errorMessage: string,
    exceptionType: string,
    stackTrace: string,
  }
}

