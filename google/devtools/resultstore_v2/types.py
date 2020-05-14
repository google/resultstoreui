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


from __future__ import absolute_import
import sys

from google.api_core.protobuf_helpers import get_messages

from google.devtools.resultstore_v2.proto import action_pb2
from google.devtools.resultstore_v2.proto import common_pb2
from google.devtools.resultstore_v2.proto import configuration_pb2
from google.devtools.resultstore_v2.proto import configured_target_pb2
from google.devtools.resultstore_v2.proto import coverage_pb2
from google.devtools.resultstore_v2.proto import coverage_summary_pb2
from google.devtools.resultstore_v2.proto import download_metadata_pb2
from google.devtools.resultstore_v2.proto import file_pb2
from google.devtools.resultstore_v2.proto import file_processing_error_pb2
from google.devtools.resultstore_v2.proto import file_set_pb2
from google.devtools.resultstore_v2.proto import invocation_pb2
from google.devtools.resultstore_v2.proto import resultstore_download_pb2
from google.devtools.resultstore_v2.proto import resultstore_file_download_pb2
from google.devtools.resultstore_v2.proto import resultstore_upload_pb2
from google.devtools.resultstore_v2.proto import target_pb2
from google.devtools.resultstore_v2.proto import test_suite_pb2
from google.devtools.resultstore_v2.proto import upload_metadata_pb2
from google.protobuf import duration_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2
from google.protobuf import wrappers_pb2


_shared_modules = [
    duration_pb2,
    empty_pb2,
    field_mask_pb2,
    timestamp_pb2,
    wrappers_pb2,
]

_local_modules = [
    action_pb2,
    common_pb2,
    configuration_pb2,
    configured_target_pb2,
    coverage_pb2,
    coverage_summary_pb2,
    download_metadata_pb2,
    file_pb2,
    file_processing_error_pb2,
    file_set_pb2,
    invocation_pb2,
    resultstore_download_pb2,
    resultstore_file_download_pb2,
    resultstore_upload_pb2,
    target_pb2,
    test_suite_pb2,
    upload_metadata_pb2,
]

names = []

for module in _shared_modules:  # pragma: NO COVER
    for name, message in get_messages(module).items():
        setattr(sys.modules[__name__], name, message)
        names.append(name)
for module in _local_modules:
      for name, message in get_messages(module).items():
          message.__module__ = 'google.devtools.resultstore_v2.types'
          setattr(sys.modules[__name__], name, message)
          names.append(name)


__all__ = tuple(sorted(names))
