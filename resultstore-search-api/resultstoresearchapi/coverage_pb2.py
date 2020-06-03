# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coverage.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='coverage.proto',
  package='resultstoresearch.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0e\x63overage.proto\x12\x14resultstoresearch.v1\"B\n\x0cLineCoverage\x12\x1a\n\x12instrumented_lines\x18\x01 \x01(\x0c\x12\x16\n\x0e\x65xecuted_lines\x18\x02 \x01(\x0c\"c\n\x0e\x42ranchCoverage\x12\x16\n\x0e\x62ranch_present\x18\x01 \x01(\x0c\x12\x18\n\x10\x62ranches_in_line\x18\x02 \x03(\x05\x12\x10\n\x08\x65xecuted\x18\x03 \x01(\x0c\x12\r\n\x05taken\x18\x04 \x01(\x0c\"\x96\x01\n\x0c\x46ileCoverage\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x39\n\rline_coverage\x18\x02 \x01(\x0b\x32\".resultstoresearch.v1.LineCoverage\x12=\n\x0f\x62ranch_coverage\x18\x03 \x01(\x0b\x32$.resultstoresearch.v1.BranchCoverage\"L\n\x0e\x41\x63tionCoverage\x12:\n\x0e\x66ile_coverages\x18\x02 \x03(\x0b\x32\".resultstoresearch.v1.FileCoverage\"O\n\x11\x41ggregateCoverage\x12:\n\x0e\x66ile_coverages\x18\x01 \x03(\x0b\x32\".resultstoresearch.v1.FileCoverageb\x06proto3'
)




_LINECOVERAGE = _descriptor.Descriptor(
  name='LineCoverage',
  full_name='resultstoresearch.v1.LineCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instrumented_lines', full_name='resultstoresearch.v1.LineCoverage.instrumented_lines', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executed_lines', full_name='resultstoresearch.v1.LineCoverage.executed_lines', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=40,
  serialized_end=106,
)


_BRANCHCOVERAGE = _descriptor.Descriptor(
  name='BranchCoverage',
  full_name='resultstoresearch.v1.BranchCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='branch_present', full_name='resultstoresearch.v1.BranchCoverage.branch_present', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branches_in_line', full_name='resultstoresearch.v1.BranchCoverage.branches_in_line', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='executed', full_name='resultstoresearch.v1.BranchCoverage.executed', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='taken', full_name='resultstoresearch.v1.BranchCoverage.taken', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=108,
  serialized_end=207,
)


_FILECOVERAGE = _descriptor.Descriptor(
  name='FileCoverage',
  full_name='resultstoresearch.v1.FileCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='resultstoresearch.v1.FileCoverage.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line_coverage', full_name='resultstoresearch.v1.FileCoverage.line_coverage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch_coverage', full_name='resultstoresearch.v1.FileCoverage.branch_coverage', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=210,
  serialized_end=360,
)


_ACTIONCOVERAGE = _descriptor.Descriptor(
  name='ActionCoverage',
  full_name='resultstoresearch.v1.ActionCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_coverages', full_name='resultstoresearch.v1.ActionCoverage.file_coverages', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=362,
  serialized_end=438,
)


_AGGREGATECOVERAGE = _descriptor.Descriptor(
  name='AggregateCoverage',
  full_name='resultstoresearch.v1.AggregateCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_coverages', full_name='resultstoresearch.v1.AggregateCoverage.file_coverages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=440,
  serialized_end=519,
)

_FILECOVERAGE.fields_by_name['line_coverage'].message_type = _LINECOVERAGE
_FILECOVERAGE.fields_by_name['branch_coverage'].message_type = _BRANCHCOVERAGE
_ACTIONCOVERAGE.fields_by_name['file_coverages'].message_type = _FILECOVERAGE
_AGGREGATECOVERAGE.fields_by_name['file_coverages'].message_type = _FILECOVERAGE
DESCRIPTOR.message_types_by_name['LineCoverage'] = _LINECOVERAGE
DESCRIPTOR.message_types_by_name['BranchCoverage'] = _BRANCHCOVERAGE
DESCRIPTOR.message_types_by_name['FileCoverage'] = _FILECOVERAGE
DESCRIPTOR.message_types_by_name['ActionCoverage'] = _ACTIONCOVERAGE
DESCRIPTOR.message_types_by_name['AggregateCoverage'] = _AGGREGATECOVERAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LineCoverage = _reflection.GeneratedProtocolMessageType('LineCoverage', (_message.Message,), {
  'DESCRIPTOR' : _LINECOVERAGE,
  '__module__' : 'coverage_pb2'
  # @@protoc_insertion_point(class_scope:resultstoresearch.v1.LineCoverage)
  })
_sym_db.RegisterMessage(LineCoverage)

BranchCoverage = _reflection.GeneratedProtocolMessageType('BranchCoverage', (_message.Message,), {
  'DESCRIPTOR' : _BRANCHCOVERAGE,
  '__module__' : 'coverage_pb2'
  # @@protoc_insertion_point(class_scope:resultstoresearch.v1.BranchCoverage)
  })
_sym_db.RegisterMessage(BranchCoverage)

FileCoverage = _reflection.GeneratedProtocolMessageType('FileCoverage', (_message.Message,), {
  'DESCRIPTOR' : _FILECOVERAGE,
  '__module__' : 'coverage_pb2'
  # @@protoc_insertion_point(class_scope:resultstoresearch.v1.FileCoverage)
  })
_sym_db.RegisterMessage(FileCoverage)

ActionCoverage = _reflection.GeneratedProtocolMessageType('ActionCoverage', (_message.Message,), {
  'DESCRIPTOR' : _ACTIONCOVERAGE,
  '__module__' : 'coverage_pb2'
  # @@protoc_insertion_point(class_scope:resultstoresearch.v1.ActionCoverage)
  })
_sym_db.RegisterMessage(ActionCoverage)

AggregateCoverage = _reflection.GeneratedProtocolMessageType('AggregateCoverage', (_message.Message,), {
  'DESCRIPTOR' : _AGGREGATECOVERAGE,
  '__module__' : 'coverage_pb2'
  # @@protoc_insertion_point(class_scope:resultstoresearch.v1.AggregateCoverage)
  })
_sym_db.RegisterMessage(AggregateCoverage)


# @@protoc_insertion_point(module_scope)
