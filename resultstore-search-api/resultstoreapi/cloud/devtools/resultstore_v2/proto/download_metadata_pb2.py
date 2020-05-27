# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/devtools/resultstore_v2/proto/download_metadata.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from resultstoreapi.cloud.devtools.resultstore_v2.proto import common_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/devtools/resultstore_v2/proto/download_metadata.proto',
  package='google.devtools.resultstore.v2',
  syntax='proto3',
  serialized_options=b'\n\"com.google.devtools.resultstore.v2P\001ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstore',
  serialized_pb=b'\nBgoogle/cloud/devtools/resultstore_v2/proto/download_metadata.proto\x12\x1egoogle.devtools.resultstore.v2\x1a\x37google/cloud/devtools/resultstore_v2/proto/common.proto\"e\n\x10\x44ownloadMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x43\n\rupload_status\x18\x02 \x01(\x0e\x32,.google.devtools.resultstore.v2.UploadStatusBq\n\"com.google.devtools.resultstore.v2P\x01ZIgoogle.golang.org/genproto/googleapis/devtools/resultstore/v2;resultstoreb\x06proto3'
  ,
  dependencies=[google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2.DESCRIPTOR,])




_DOWNLOADMETADATA = _descriptor.Descriptor(
  name='DownloadMetadata',
  full_name='google.devtools.resultstore.v2.DownloadMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.resultstore.v2.DownloadMetadata.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upload_status', full_name='google.devtools.resultstore.v2.DownloadMetadata.upload_status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=159,
  serialized_end=260,
)

_DOWNLOADMETADATA.fields_by_name['upload_status'].enum_type = google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_common__pb2._UPLOADSTATUS
DESCRIPTOR.message_types_by_name['DownloadMetadata'] = _DOWNLOADMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DownloadMetadata = _reflection.GeneratedProtocolMessageType('DownloadMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADMETADATA,
  '__module__' : 'resultstoreapi.cloud.devtools.resultstore_v2.proto.download_metadata_pb2'
  ,
  '__doc__': """The download metadata for an invocation
  
  
  Attributes:
      name:
          The name of the download metadata. Its format will be:
          invocations/${INVOCATION_ID}/downloadMetadata
      upload_status:
          Indicates the upload status of the invocation, whether it is
          post-processing, or immutable, etc.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.resultstore.v2.DownloadMetadata)
  })
_sym_db.RegisterMessage(DownloadMetadata)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
