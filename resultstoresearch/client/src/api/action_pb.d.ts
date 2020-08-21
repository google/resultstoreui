import * as jspb from "google-protobuf"

import * as common_pb from './common_pb';
import * as coverage_pb from './coverage_pb';
import * as file_pb from './file_pb';
import * as file_processing_error_pb from './file_processing_error_pb';
import * as test_suite_pb from './test_suite_pb';
import * as duration_pb from './duration_pb';

export class Action extends jspb.Message {
  getName(): string;
  setName(value: string): Action;

  getId(): Action.Id | undefined;
  setId(value?: Action.Id): Action;
  hasId(): boolean;
  clearId(): Action;

  getStatusAttributes(): common_pb.StatusAttributes | undefined;
  setStatusAttributes(value?: common_pb.StatusAttributes): Action;
  hasStatusAttributes(): boolean;
  clearStatusAttributes(): Action;

  getTiming(): common_pb.Timing | undefined;
  setTiming(value?: common_pb.Timing): Action;
  hasTiming(): boolean;
  clearTiming(): Action;

  getBuildAction(): BuildAction | undefined;
  setBuildAction(value?: BuildAction): Action;
  hasBuildAction(): boolean;
  clearBuildAction(): Action;

  getTestAction(): TestAction | undefined;
  setTestAction(value?: TestAction): Action;
  hasTestAction(): boolean;
  clearTestAction(): Action;

  getActionAttributes(): ActionAttributes | undefined;
  setActionAttributes(value?: ActionAttributes): Action;
  hasActionAttributes(): boolean;
  clearActionAttributes(): Action;

  getActionDependenciesList(): Array<common_pb.Dependency>;
  setActionDependenciesList(value: Array<common_pb.Dependency>): Action;
  clearActionDependenciesList(): Action;
  addActionDependencies(value?: common_pb.Dependency, index?: number): common_pb.Dependency;

  getPropertiesList(): Array<common_pb.Property>;
  setPropertiesList(value: Array<common_pb.Property>): Action;
  clearPropertiesList(): Action;
  addProperties(value?: common_pb.Property, index?: number): common_pb.Property;

  getFilesList(): Array<file_pb.File>;
  setFilesList(value: Array<file_pb.File>): Action;
  clearFilesList(): Action;
  addFiles(value?: file_pb.File, index?: number): file_pb.File;

  getFileSetsList(): Array<string>;
  setFileSetsList(value: Array<string>): Action;
  clearFileSetsList(): Action;
  addFileSets(value: string, index?: number): Action;

  getCoverage(): coverage_pb.ActionCoverage | undefined;
  setCoverage(value?: coverage_pb.ActionCoverage): Action;
  hasCoverage(): boolean;
  clearCoverage(): Action;

  getFileProcessingErrorsList(): Array<file_processing_error_pb.FileProcessingErrors>;
  setFileProcessingErrorsList(value: Array<file_processing_error_pb.FileProcessingErrors>): Action;
  clearFileProcessingErrorsList(): Action;
  addFileProcessingErrors(value?: file_processing_error_pb.FileProcessingErrors, index?: number): file_processing_error_pb.FileProcessingErrors;

  getActionTypeCase(): Action.ActionTypeCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): Action.AsObject;
  static toObject(includeInstance: boolean, msg: Action): Action.AsObject;
  static serializeBinaryToWriter(message: Action, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): Action;
  static deserializeBinaryFromReader(message: Action, reader: jspb.BinaryReader): Action;
}

export namespace Action {
  export type AsObject = {
    name: string,
    id?: Action.Id.AsObject,
    statusAttributes?: common_pb.StatusAttributes.AsObject,
    timing?: common_pb.Timing.AsObject,
    buildAction?: BuildAction.AsObject,
    testAction?: TestAction.AsObject,
    actionAttributes?: ActionAttributes.AsObject,
    actionDependenciesList: Array<common_pb.Dependency.AsObject>,
    propertiesList: Array<common_pb.Property.AsObject>,
    filesList: Array<file_pb.File.AsObject>,
    fileSetsList: Array<string>,
    coverage?: coverage_pb.ActionCoverage.AsObject,
    fileProcessingErrorsList: Array<file_processing_error_pb.FileProcessingErrors.AsObject>,
  }

  export class Id extends jspb.Message {
    getInvocationId(): string;
    setInvocationId(value: string): Id;

    getTargetId(): string;
    setTargetId(value: string): Id;

    getConfigurationId(): string;
    setConfigurationId(value: string): Id;

    getActionId(): string;
    setActionId(value: string): Id;

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
      configurationId: string,
      actionId: string,
    }
  }


  export enum ActionTypeCase { 
    ACTION_TYPE_NOT_SET = 0,
    BUILD_ACTION = 9,
    TEST_ACTION = 10,
  }
}

export class BuildAction extends jspb.Message {
  getType(): string;
  setType(value: string): BuildAction;

  getPrimaryInputPath(): string;
  setPrimaryInputPath(value: string): BuildAction;

  getPrimaryOutputPath(): string;
  setPrimaryOutputPath(value: string): BuildAction;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): BuildAction.AsObject;
  static toObject(includeInstance: boolean, msg: BuildAction): BuildAction.AsObject;
  static serializeBinaryToWriter(message: BuildAction, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): BuildAction;
  static deserializeBinaryFromReader(message: BuildAction, reader: jspb.BinaryReader): BuildAction;
}

export namespace BuildAction {
  export type AsObject = {
    type: string,
    primaryInputPath: string,
    primaryOutputPath: string,
  }
}

export class TestAction extends jspb.Message {
  getTestTiming(): TestTiming | undefined;
  setTestTiming(value?: TestTiming): TestAction;
  hasTestTiming(): boolean;
  clearTestTiming(): TestAction;

  getShardNumber(): number;
  setShardNumber(value: number): TestAction;

  getRunNumber(): number;
  setRunNumber(value: number): TestAction;

  getAttemptNumber(): number;
  setAttemptNumber(value: number): TestAction;

  getTestSuite(): test_suite_pb.TestSuite | undefined;
  setTestSuite(value?: test_suite_pb.TestSuite): TestAction;
  hasTestSuite(): boolean;
  clearTestSuite(): TestAction;

  getWarningsList(): Array<TestWarning>;
  setWarningsList(value: Array<TestWarning>): TestAction;
  clearWarningsList(): TestAction;
  addWarnings(value?: TestWarning, index?: number): TestWarning;

  getEstimatedMemoryBytes(): number;
  setEstimatedMemoryBytes(value: number): TestAction;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestAction.AsObject;
  static toObject(includeInstance: boolean, msg: TestAction): TestAction.AsObject;
  static serializeBinaryToWriter(message: TestAction, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestAction;
  static deserializeBinaryFromReader(message: TestAction, reader: jspb.BinaryReader): TestAction;
}

export namespace TestAction {
  export type AsObject = {
    testTiming?: TestTiming.AsObject,
    shardNumber: number,
    runNumber: number,
    attemptNumber: number,
    testSuite?: test_suite_pb.TestSuite.AsObject,
    warningsList: Array<TestWarning.AsObject>,
    estimatedMemoryBytes: number,
  }
}

export class ActionAttributes extends jspb.Message {
  getExecutionStrategy(): ExecutionStrategy;
  setExecutionStrategy(value: ExecutionStrategy): ActionAttributes;

  getExitCode(): number;
  setExitCode(value: number): ActionAttributes;

  getHostname(): string;
  setHostname(value: string): ActionAttributes;

  getInputFileInfo(): InputFileInfo | undefined;
  setInputFileInfo(value?: InputFileInfo): ActionAttributes;
  hasInputFileInfo(): boolean;
  clearInputFileInfo(): ActionAttributes;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): ActionAttributes.AsObject;
  static toObject(includeInstance: boolean, msg: ActionAttributes): ActionAttributes.AsObject;
  static serializeBinaryToWriter(message: ActionAttributes, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): ActionAttributes;
  static deserializeBinaryFromReader(message: ActionAttributes, reader: jspb.BinaryReader): ActionAttributes;
}

export namespace ActionAttributes {
  export type AsObject = {
    executionStrategy: ExecutionStrategy,
    exitCode: number,
    hostname: string,
    inputFileInfo?: InputFileInfo.AsObject,
  }
}

export class InputFileInfo extends jspb.Message {
  getCount(): number;
  setCount(value: number): InputFileInfo;

  getDistinctCount(): number;
  setDistinctCount(value: number): InputFileInfo;

  getCountLimit(): number;
  setCountLimit(value: number): InputFileInfo;

  getDistinctBytes(): number;
  setDistinctBytes(value: number): InputFileInfo;

  getDistinctByteLimit(): number;
  setDistinctByteLimit(value: number): InputFileInfo;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): InputFileInfo.AsObject;
  static toObject(includeInstance: boolean, msg: InputFileInfo): InputFileInfo.AsObject;
  static serializeBinaryToWriter(message: InputFileInfo, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): InputFileInfo;
  static deserializeBinaryFromReader(message: InputFileInfo, reader: jspb.BinaryReader): InputFileInfo;
}

export namespace InputFileInfo {
  export type AsObject = {
    count: number,
    distinctCount: number,
    countLimit: number,
    distinctBytes: number,
    distinctByteLimit: number,
  }
}

export class LocalTestTiming extends jspb.Message {
  getTestProcessDuration(): duration_pb.Duration | undefined;
  setTestProcessDuration(value?: duration_pb.Duration): LocalTestTiming;
  hasTestProcessDuration(): boolean;
  clearTestProcessDuration(): LocalTestTiming;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): LocalTestTiming.AsObject;
  static toObject(includeInstance: boolean, msg: LocalTestTiming): LocalTestTiming.AsObject;
  static serializeBinaryToWriter(message: LocalTestTiming, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): LocalTestTiming;
  static deserializeBinaryFromReader(message: LocalTestTiming, reader: jspb.BinaryReader): LocalTestTiming;
}

export namespace LocalTestTiming {
  export type AsObject = {
    testProcessDuration?: duration_pb.Duration.AsObject,
  }
}

export class RemoteTestAttemptTiming extends jspb.Message {
  getQueueDuration(): duration_pb.Duration | undefined;
  setQueueDuration(value?: duration_pb.Duration): RemoteTestAttemptTiming;
  hasQueueDuration(): boolean;
  clearQueueDuration(): RemoteTestAttemptTiming;

  getUploadDuration(): duration_pb.Duration | undefined;
  setUploadDuration(value?: duration_pb.Duration): RemoteTestAttemptTiming;
  hasUploadDuration(): boolean;
  clearUploadDuration(): RemoteTestAttemptTiming;

  getMachineSetupDuration(): duration_pb.Duration | undefined;
  setMachineSetupDuration(value?: duration_pb.Duration): RemoteTestAttemptTiming;
  hasMachineSetupDuration(): boolean;
  clearMachineSetupDuration(): RemoteTestAttemptTiming;

  getTestProcessDuration(): duration_pb.Duration | undefined;
  setTestProcessDuration(value?: duration_pb.Duration): RemoteTestAttemptTiming;
  hasTestProcessDuration(): boolean;
  clearTestProcessDuration(): RemoteTestAttemptTiming;

  getDownloadDuration(): duration_pb.Duration | undefined;
  setDownloadDuration(value?: duration_pb.Duration): RemoteTestAttemptTiming;
  hasDownloadDuration(): boolean;
  clearDownloadDuration(): RemoteTestAttemptTiming;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteTestAttemptTiming.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteTestAttemptTiming): RemoteTestAttemptTiming.AsObject;
  static serializeBinaryToWriter(message: RemoteTestAttemptTiming, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteTestAttemptTiming;
  static deserializeBinaryFromReader(message: RemoteTestAttemptTiming, reader: jspb.BinaryReader): RemoteTestAttemptTiming;
}

export namespace RemoteTestAttemptTiming {
  export type AsObject = {
    queueDuration?: duration_pb.Duration.AsObject,
    uploadDuration?: duration_pb.Duration.AsObject,
    machineSetupDuration?: duration_pb.Duration.AsObject,
    testProcessDuration?: duration_pb.Duration.AsObject,
    downloadDuration?: duration_pb.Duration.AsObject,
  }
}

export class RemoteTestTiming extends jspb.Message {
  getLocalAnalysisDuration(): duration_pb.Duration | undefined;
  setLocalAnalysisDuration(value?: duration_pb.Duration): RemoteTestTiming;
  hasLocalAnalysisDuration(): boolean;
  clearLocalAnalysisDuration(): RemoteTestTiming;

  getAttemptsList(): Array<RemoteTestAttemptTiming>;
  setAttemptsList(value: Array<RemoteTestAttemptTiming>): RemoteTestTiming;
  clearAttemptsList(): RemoteTestTiming;
  addAttempts(value?: RemoteTestAttemptTiming, index?: number): RemoteTestAttemptTiming;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): RemoteTestTiming.AsObject;
  static toObject(includeInstance: boolean, msg: RemoteTestTiming): RemoteTestTiming.AsObject;
  static serializeBinaryToWriter(message: RemoteTestTiming, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): RemoteTestTiming;
  static deserializeBinaryFromReader(message: RemoteTestTiming, reader: jspb.BinaryReader): RemoteTestTiming;
}

export namespace RemoteTestTiming {
  export type AsObject = {
    localAnalysisDuration?: duration_pb.Duration.AsObject,
    attemptsList: Array<RemoteTestAttemptTiming.AsObject>,
  }
}

export class TestTiming extends jspb.Message {
  getLocal(): LocalTestTiming | undefined;
  setLocal(value?: LocalTestTiming): TestTiming;
  hasLocal(): boolean;
  clearLocal(): TestTiming;

  getRemote(): RemoteTestTiming | undefined;
  setRemote(value?: RemoteTestTiming): TestTiming;
  hasRemote(): boolean;
  clearRemote(): TestTiming;

  getSystemTimeDuration(): duration_pb.Duration | undefined;
  setSystemTimeDuration(value?: duration_pb.Duration): TestTiming;
  hasSystemTimeDuration(): boolean;
  clearSystemTimeDuration(): TestTiming;

  getUserTimeDuration(): duration_pb.Duration | undefined;
  setUserTimeDuration(value?: duration_pb.Duration): TestTiming;
  hasUserTimeDuration(): boolean;
  clearUserTimeDuration(): TestTiming;

  getTestCaching(): TestCaching;
  setTestCaching(value: TestCaching): TestTiming;

  getLocationCase(): TestTiming.LocationCase;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestTiming.AsObject;
  static toObject(includeInstance: boolean, msg: TestTiming): TestTiming.AsObject;
  static serializeBinaryToWriter(message: TestTiming, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestTiming;
  static deserializeBinaryFromReader(message: TestTiming, reader: jspb.BinaryReader): TestTiming;
}

export namespace TestTiming {
  export type AsObject = {
    local?: LocalTestTiming.AsObject,
    remote?: RemoteTestTiming.AsObject,
    systemTimeDuration?: duration_pb.Duration.AsObject,
    userTimeDuration?: duration_pb.Duration.AsObject,
    testCaching: TestCaching,
  }

  export enum LocationCase { 
    LOCATION_NOT_SET = 0,
    LOCAL = 1,
    REMOTE = 2,
  }
}

export class TestWarning extends jspb.Message {
  getWarningMessage(): string;
  setWarningMessage(value: string): TestWarning;

  serializeBinary(): Uint8Array;
  toObject(includeInstance?: boolean): TestWarning.AsObject;
  static toObject(includeInstance: boolean, msg: TestWarning): TestWarning.AsObject;
  static serializeBinaryToWriter(message: TestWarning, writer: jspb.BinaryWriter): void;
  static deserializeBinary(bytes: Uint8Array): TestWarning;
  static deserializeBinaryFromReader(message: TestWarning, reader: jspb.BinaryReader): TestWarning;
}

export namespace TestWarning {
  export type AsObject = {
    warningMessage: string,
  }
}

export enum ExecutionStrategy { 
  EXECUTION_STRATEGY_UNSPECIFIED = 0,
  OTHER_ENVIRONMENT = 1,
  REMOTE_SERVICE = 2,
  LOCAL_PARALLEL = 3,
  LOCAL_SEQUENTIAL = 4,
}
export enum TestCaching { 
  TEST_CACHING_UNSPECIFIED = 0,
  LOCAL_CACHE_HIT = 1,
  REMOTE_CACHE_HIT = 2,
  CACHE_MISS = 3,
}
