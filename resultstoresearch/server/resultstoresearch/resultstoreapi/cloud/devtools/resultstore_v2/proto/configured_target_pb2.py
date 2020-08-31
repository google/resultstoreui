# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/devtools/resultstore_v2/proto/configured_target.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resultstoreapi.cloud.devtools.resultstore_v2.proto import common_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2
from resultstoreapi.cloud.devtools.resultstore_v2.proto import file_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/devtools/resultstore_v2/proto/configured_target.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2P\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  serialized_pb=b'\nBgoogle/cloud/devtools/resultstore_v2/proto/configured_target.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x37google/cloud/devtools/resultstore_v2/proto/common.proto\x1a\x35google/cloud/devtools/resultstore_v2/proto/file.proto\x1a\x1egoogle/protobuf/duration.proto\"\xf6\x03\n\x10\x43onfiguredTarget\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\x02id\x18\x02 \x01(\x0b\x32\x33.google.devtools.resultstore.v2.ConfiguredTarget.Id\x12K\n\x11status_attributes\x18\x03 \x01(\x0b\x32\x30.google.devtools.resultstore.v2.StatusAttributes\x12\x36\n\x06timing\x18\x04 \x01(\x0b\x32&.google.devtools.resultstore.v2.Timing\x12Q\n\x0ftest_attributes\x18\x06 \x01(\x0b\x32\x38.google.devtools.resultstore.v2.ConfiguredTestAttributes\x12<\n\nproperties\x18\x07 \x03(\x0b\x32(.google.devtools.resultstore.v2.Property\x12\x33\n\x05\x66iles\x18\x08 \x03(\x0b\x32$.google.devtools.resultstore.v2.File\x1aH\n\x02Id\x12\x15\n\rinvocation_id\x18\x01 \x01(\t\x12\x11\n\ttarget_id\x18\x02 \x01(\t\x12\x18\n\x10\x63onfiguration_id\x18\x03 \x01(\t\"\x83\x01\n\x18\x43onfiguredTestAttributes\x12\x17\n\x0ftotal_run_count\x18\x02 \x01(\x05\x12\x19\n\x11total_shard_count\x18\x03 \x01(\x05\x12\x33\n\x10timeout_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationBq\n\"com.google.devtools.resultstore.v2P\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2.DESCRIPTOR,google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_CONFIGUREDTARGET_ID = _descriptor.Descriptor(
  name='Id',
  full_name='google.devtools.resultstore.v2.ConfiguredTarget.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invocation_id', full_name='google.devtools.resultstore.v2.ConfiguredTarget.Id.invocation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_id', full_name='google.devtools.resultstore.v2.ConfiguredTarget.Id.target_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configuration_id', full_name='google.devtools.resultstore.v2.ConfiguredTarget.Id.configuration_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=677,
  serialized_end=749,
)

_CONFIGUREDTARGET = _descriptor.Descriptor(
  name='ConfiguredTarget',
  full_name='google.devtools.resultstore.v2.ConfiguredTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.resultstore.v2.ConfiguredTarget.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.devtools.resultstore.v2.ConfiguredTarget.id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status_attributes', full_name='google.devtools.resultstore.v2.ConfiguredTarget.status_attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timing', full_name='google.devtools.resultstore.v2.ConfiguredTarget.timing', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='test_attributes', full_name='google.devtools.resultstore.v2.ConfiguredTarget.test_attributes', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='google.devtools.resultstore.v2.ConfiguredTarget.properties', index=5,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='files', full_name='google.devtools.resultstore.v2.ConfiguredTarget.files', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CONFIGUREDTARGET_ID, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=749,
)


_CONFIGUREDTESTATTRIBUTES = _descriptor.Descriptor(
  name='ConfiguredTestAttributes',
  full_name='google.devtools.resultstore.v2.ConfiguredTestAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_run_count', full_name='google.devtools.resultstore.v2.ConfiguredTestAttributes.total_run_count', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_shard_count', full_name='google.devtools.resultstore.v2.ConfiguredTestAttributes.total_shard_count', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout_duration', full_name='google.devtools.resultstore.v2.ConfiguredTestAttributes.timeout_duration', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=883,
)

_CONFIGUREDTARGET_ID.containing_type = _CONFIGUREDTARGET
_CONFIGUREDTARGET.fields_by_name['id'].message_type = _CONFIGUREDTARGET_ID
_CONFIGUREDTARGET.fields_by_name['status_attributes'].message_type = google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2._STATUSATTRIBUTES
_CONFIGUREDTARGET.fields_by_name['timing'].message_type = google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2._TIMING
_CONFIGUREDTARGET.fields_by_name['test_attributes'].message_type = _CONFIGUREDTESTATTRIBUTES
_CONFIGUREDTARGET.fields_by_name['properties'].message_type = google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2._PROPERTY
_CONFIGUREDTARGET.fields_by_name['files'].message_type = google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__pb2._FILE
_CONFIGUREDTESTATTRIBUTES.fields_by_name['timeout_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['ConfiguredTarget'] = _CONFIGUREDTARGET
DESCRIPTOR.message_types_by_name['ConfiguredTestAttributes'] = _CONFIGUREDTESTATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfiguredTarget = _reflection.GeneratedProtocolMessageType('ConfiguredTarget', (_message.Message,), {

  'Id' : _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
    'DESCRIPTOR' : _CONFIGUREDTARGET_ID,
    '__module__' : 'resultstoreapi.cloud.devtools.resultstore_v2.proto.configured_target_pb2'
    ,
    '__doc__': """The resource ID components that identify the
    ConfiguredTarget.
    
    
    Attributes:
        invocation_id:
            The Invocation ID.
        target_id:
            The Target ID.
        configuration_id:
            The Configuration ID.
    """,
    # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ConfiguredTarget.Id)
    })
  ,
  'DESCRIPTOR' : _CONFIGUREDTARGET,
  '__module__' : 'resultstoreapi.cloud.devtools.resultstore_v2.proto.configured_target_pb2'
  ,
  '__doc__': """Each ConfiguredTarget represents data for a given
  configuration of a given target in a given Invocation. Every
  ConfiguredTarget should have at least one Action as a child resource
  before the invocation is finalized. Refer to the Action’s documentation
  for more info on this.
  
  
  Attributes:
      name:
          The resource name. Its format must be: invocations/\
          :math:`{INVOCATION_ID}/targets/`\ {url_encode(TARGET_ID)}/conf
          iguredTargets/${url_encode(CONFIG_ID)} where ${CONFIG_ID} must
          match the ID of an existing Configuration under this
          Invocation.
      id:
          The resource ID components that identify the ConfiguredTarget.
          They must match the resource name after proper encoding.
      status_attributes:
          The aggregate status for this configuration of this target. If
          testing was not requested, set this to the build status
          (e.g. BUILT or FAILED_TO_BUILD).
      timing:
          Captures the start time and duration of this configured
          target.
      test_attributes:
          Test specific attributes for this ConfiguredTarget.
      properties:
          Arbitrary name-value pairs. This is implemented as a multi-
          map. Multiple properties are allowed with the same key.
          Properties will be returned in lexicographical order by key.
      files:
          A list of file references for configured target level files.
          The file IDs must be unique within this list. Duplicate file
          IDs will result in an error. Files will be returned in
          lexicographical order by ID.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ConfiguredTarget)
  })
_sym_db.RegisterMessage(ConfiguredTarget)
_sym_db.RegisterMessage(ConfiguredTarget.Id)

ConfiguredTestAttributes = _reflection.GeneratedProtocolMessageType('ConfiguredTestAttributes', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGUREDTESTATTRIBUTES,
  '__module__' : 'resultstoreapi.cloud.devtools.resultstore_v2.proto.configured_target_pb2'
  ,
  '__doc__': """Attributes that apply only to test actions under this
  configured target.
  
  
  Attributes:
      total_run_count:
          Total number of test runs. For example, in bazel this is
          specified with –runs_per_test. Zero if runs_per_test is not
          used.
      total_shard_count:
          Total number of test shards. Zero if shard count was not
          specified.
      timeout_duration:
          How long test is allowed to run.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.ConfiguredTestAttributes)
  })
_sym_db.RegisterMessage(ConfiguredTestAttributes)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)