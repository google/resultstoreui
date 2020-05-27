# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class ExecutionStrategy(enum.IntEnum):
    """
    Indicates how/where this Action was executed.

    Attributes:
      EXECUTION_STRATEGY_UNSPECIFIED (int): The action did not indicate how it was executed.
      OTHER_ENVIRONMENT (int): The action was executed in some other form.
      REMOTE_SERVICE (int): The action used a remote build service.
      LOCAL_PARALLEL (int): The action was executed locally, in parallel with other actions.
      LOCAL_SEQUENTIAL (int): The action was executed locally, without parallelism.
    """
    EXECUTION_STRATEGY_UNSPECIFIED = 0
    OTHER_ENVIRONMENT = 1
    REMOTE_SERVICE = 2
    LOCAL_PARALLEL = 3
    LOCAL_SEQUENTIAL = 4


class FileProcessingErrorType(enum.IntEnum):
    """
    Errors in file post-processing are categorized using this enum.

    Attributes:
      FILE_PROCESSING_ERROR_TYPE_UNSPECIFIED (int): Type unspecified or not listed here.
      GENERIC_READ_ERROR (int): A read error occurred trying to read the file.
      GENERIC_PARSE_ERROR (int): There was an error trying to parse the file.
      FILE_TOO_LARGE (int): File is exceeds size limit.
      OUTPUT_TOO_LARGE (int): The result of parsing the file exceeded size limit.
      ACCESS_DENIED (int): Read access to the file was denied by file system.
      DEADLINE_EXCEEDED (int): Deadline exceeded trying to read the file.
      NOT_FOUND (int): File not found.
      FILE_EMPTY (int): File is empty but was expected to have content.
    """
    FILE_PROCESSING_ERROR_TYPE_UNSPECIFIED = 0
    GENERIC_READ_ERROR = 1
    GENERIC_PARSE_ERROR = 2
    FILE_TOO_LARGE = 3
    OUTPUT_TOO_LARGE = 4
    ACCESS_DENIED = 5
    DEADLINE_EXCEEDED = 6
    NOT_FOUND = 7
    FILE_EMPTY = 8


class Language(enum.IntEnum):
    """
    These correspond to the prefix of the rule name. Eg cc_test has
    language CC.

    Attributes:
      LANGUAGE_UNSPECIFIED (int): Language unspecified or not listed here.
      NONE (int): Not related to any particular language
      ANDROID (int): Android
      AS (int): ActionScript (Flash)
      CC (int): C++ or C
      CSS (int): Cascading-Style-Sheets
      DART (int): Dart
      GO (int): Go
      GWT (int): Google-Web-Toolkit
      HASKELL (int): Haskell
      JAVA (int): Java
      JS (int): Javascript
      LISP (int): Lisp
      OBJC (int): Objective-C
      PY (int): Python
      SH (int): Shell (Typically Bash)
      SWIFT (int): Swift
      TS (int): Typescript
      WEB (int): Webtesting
      SCALA (int): Scala
      PROTO (int): Protocol Buffer
      XML (int): Extensible Markup Language
    """
    LANGUAGE_UNSPECIFIED = 0
    NONE = 1
    ANDROID = 2
    AS = 3
    CC = 4
    CSS = 5
    DART = 6
    GO = 7
    GWT = 8
    HASKELL = 9
    JAVA = 10
    JS = 11
    LISP = 12
    OBJC = 13
    PY = 14
    SH = 15
    SWIFT = 16
    TS = 18
    WEB = 19
    SCALA = 20
    PROTO = 21
    XML = 22


class Status(enum.IntEnum):
    """
    Status of a resource.

    Attributes:
      STATUS_UNSPECIFIED (int): The implicit default enum value. Should never be set.
      BUILDING (int): Displays as "Building". Means the target is compiling, linking, etc.
      BUILT (int): Displays as "Built". Means the target was built successfully.
      If testing was requested, it should never reach this status: it should go
      straight from BUILDING to TESTING.
      FAILED_TO_BUILD (int): Displays as "Broken". Means build failure such as compile error.
      TESTING (int): Displays as "Testing". Means the test is running.
      PASSED (int): Displays as "Passed". Means the test was run and passed.
      FAILED (int): Displays as "Failed". Means the test was run and failed.
      TIMED_OUT (int): Displays as "Timed out". Means the test didn't finish in time.
      CANCELLED (int): Displays as "Cancelled". Means the build or test was cancelled.
      E.g. User hit control-C.
      TOOL_FAILED (int): Displays as "Tool Failed". Means the build or test had internal tool
      failure.
      INCOMPLETE (int): Displays as "Incomplete". Means the build or test did not complete.
      This might happen when a build breakage or test failure causes the tool
      to stop trying to build anything more or run any more tests, with the
      default bazel --nokeep_going option or the --notest_keep_going option.
      FLAKY (int): Displays as "Flaky". Means the aggregate status contains some runs that
      were successful, and some that were not.
      UNKNOWN (int): Displays as "Unknown". Means the tool uploading to the server died
      mid-upload or does not know the state.
      SKIPPED (int): Displays as "Skipped". Means building and testing were skipped.
      (E.g. Restricted to a different configuration.)
    """
    STATUS_UNSPECIFIED = 0
    BUILDING = 1
    BUILT = 2
    FAILED_TO_BUILD = 3
    TESTING = 4
    PASSED = 5
    FAILED = 6
    TIMED_OUT = 7
    CANCELLED = 8
    TOOL_FAILED = 9
    INCOMPLETE = 10
    FLAKY = 11
    UNKNOWN = 12
    SKIPPED = 13


class TargetType(enum.IntEnum):
    """
    These correspond to the suffix of the rule name. Eg cc_test has type
    TEST.

    Attributes:
      TARGET_TYPE_UNSPECIFIED (int): Unspecified by the build system.
      APPLICATION (int): An application e.g. ios_application.
      BINARY (int): A binary target e.g. cc_binary.
      LIBRARY (int): A library target e.g. java_library
      PACKAGE (int): A package
      TEST (int): Any test target, in bazel that means a rule with a '_test' suffix.
    """
    TARGET_TYPE_UNSPECIFIED = 0
    APPLICATION = 1
    BINARY = 2
    LIBRARY = 3
    PACKAGE = 4
    TEST = 5


class TestCaching(enum.IntEnum):
    """
    Most build systems cache build results to speed up incremental builds.
    Some also cache test results too. This indicates whether the test results
    were found in a cache, and where that cache was located.

    Attributes:
      TEST_CACHING_UNSPECIFIED (int): The implicit default enum value. Should never be set.
      LOCAL_CACHE_HIT (int): The test result was found in a local cache, so it wasn't run again.
      REMOTE_CACHE_HIT (int): The test result was found in a remote cache, so it wasn't run again.
      CACHE_MISS (int): The test result was not found in any cache, so it had to be run again.
    """
    TEST_CACHING_UNSPECIFIED = 0
    LOCAL_CACHE_HIT = 1
    REMOTE_CACHE_HIT = 2
    CACHE_MISS = 3


class TestSize(enum.IntEnum):
    """
    Indicates how big the user indicated the test action was.

    Attributes:
      TEST_SIZE_UNSPECIFIED (int): Unspecified by the user.
      SMALL (int): Unit test taking less than 1 minute.
      MEDIUM (int): Integration tests taking less than 5 minutes.
      LARGE (int): End-to-end tests taking less than 15 minutes.
      ENORMOUS (int): Even bigger than LARGE.
      OTHER_SIZE (int): Something that doesn't fit into the above categories.
    """
    TEST_SIZE_UNSPECIFIED = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    ENORMOUS = 4
    OTHER_SIZE = 5


class UploadStatus(enum.IntEnum):
    """
    Indicates the upload status of the invocation, whether it is
    post-processing, or immutable, etc.

    Attributes:
      UPLOAD_STATUS_UNSPECIFIED (int): The implicit default enum value. Should never be set.
      UPLOADING (int): The invocation is still uploading to the ResultStore.
      POST_PROCESSING (int): The invocation upload is complete. The ResultStore is still post-processing
      the invocation.
      IMMUTABLE (int): All post-processing is complete, and the invocation is now immutable.
    """
    UPLOAD_STATUS_UNSPECIFIED = 0
    UPLOADING = 1
    POST_PROCESSING = 2
    IMMUTABLE = 3


class File(object):
    class HashType(enum.IntEnum):
        """
        If known, the hash function used to compute this digest.

        Attributes:
          HASH_TYPE_UNSPECIFIED (int): Unknown
          MD5 (int): MD5
          SHA1 (int): SHA-1
          SHA256 (int): SHA-256
        """
        HASH_TYPE_UNSPECIFIED = 0
        MD5 = 1
        SHA1 = 2
        SHA256 = 3


class TestCase(object):
    class Result(enum.IntEnum):
        """
        The result of running a test case.

        Attributes:
          RESULT_UNSPECIFIED (int): The implicit default enum value. Do not use.
          COMPLETED (int): Test case ran to completion. Look for failures or errors to determine
          whether it passed, failed, or errored.
          INTERRUPTED (int): Test case started but did not complete because the test harness received
          a signal and decided to stop running tests.
          CANCELLED (int): Test case was not started because the test harness received a SIGINT or
          timed out.
          FILTERED (int): Test case was not run because the user or process running the test
          specified a filter that excluded this test case.
          SKIPPED (int): Test case was not run to completion because the test case decided it
          should not be run (eg. due to a failed assumption in a JUnit4 test).
          Per-test setup or tear-down may or may not have run.
          SUPPRESSED (int): The test framework did not run the test case because it was labeled as
          suppressed.  Eg. if someone temporarily disables a failing test.
        """
        RESULT_UNSPECIFIED = 0
        COMPLETED = 1
        INTERRUPTED = 2
        CANCELLED = 3
        FILTERED = 4
        SKIPPED = 5
        SUPPRESSED = 6


class UploadRequest(object):
    class UploadOperation(enum.IntEnum):
        """
        The operation for the request (e.g. Create(), Update(), etc.)

        Attributes:
          UPLOAD_OPERATION_UNSPECIFIED (int): Unspecified
          CREATE (int): Create the given resources.
          For more information, check the Create APIs.
          UPDATE (int): Applies a standard update to the resource identified by the given
          proto's name. For more information, see the Update APIs.
          UploadBatch does not support arbitrary field masks. The list of allowed
          field masks can be found below.
          MERGE (int): Applies an merge update to the resource identified by the given
          proto's name. For more information, see the Merge APIs. Currently, only
          the "files" and "file_processing_errors" fields are supported by this
          operation.
          FINALIZE (int): Declares the resource with the given name as finalized and immutable by
          the uploader. Only supported for Invocation, Target, ConfiguredTarget.
          There must be no operation on child resources after parent resource is
          Finalized. If there is a Finalize of Invocation, it must be the final
          UploadRequest. For more information, see the Finalize APIs.
          An empty resource should be provided below.
        """
        UPLOAD_OPERATION_UNSPECIFIED = 0
        CREATE = 1
        UPDATE = 2
        MERGE = 3
        FINALIZE = 4
    