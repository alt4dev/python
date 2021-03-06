# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: definitions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='definitions.proto',
  package='proto',
  syntax='proto3',
  serialized_options=b'Z\007.;proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64\x65\x66initions.proto\x12\x05proto\"\x90\x02\n\x03Log\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06thread\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x1c\n\x06\x63laims\x18\x04 \x03(\x0b\x32\x0c.proto.Claim\x12\x0c\n\x04\x66ile\x18\x05 \x01(\t\x12\x0c\n\x04line\x18\x06 \x01(\r\x12\x10\n\x08\x66unction\x18\x07 \x01(\t\x12\x1f\n\x05level\x18\x08 \x01(\x0e\x32\x10.proto.Log.Level\x12\x11\n\ttimestamp\x18\t \x01(\x04\x12\r\n\x05group\x18\n \x01(\x08\"I\n\x05Level\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\t\n\x05\x44\x45\x42UG\x10\x02\x12\x0b\n\x07WARNING\x10\x03\x12\t\n\x05\x45RROR\x10\x04\x12\t\n\x05\x46\x41TAL\x10\x05\"\x81\x01\n\x05\x43laim\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.proto.Claim.Type\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\":\n\x04Type\x12\n\n\x06STRING\x10\x00\x12\n\n\x06NUMBER\x10\x01\x12\x0b\n\x07\x42OOLEAN\x10\x02\x12\r\n\tTIMESTAMP\x10\x03\"\x94\x01\n\x06Result\x12$\n\x06status\x18\x01 \x01(\x0e\x32\x14.proto.Result.Status\x12\x0f\n\x07message\x18\x02 \x01(\t\"S\n\x06Status\x12\x10\n\x0c\x41\x43KNOWLEDGED\x10\x00\x12\x10\n\x0cUNAUTHORIZED\x10\x01\x12\x11\n\rACCESS_DENIED\x10\x02\x12\x12\n\x0eINTERNAL_ERROR\x10\x03\"[\n\x08\x41uditLog\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x1c\n\x06\x63laims\x18\x02 \x03(\x0b\x32\x0c.proto.Claim\x12\r\n\x05topic\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\"\xcc\x01\n\tCondition\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12/\n\ncomparison\x18\x02 \x01(\x0e\x32\x1b.proto.Condition.Comparison\x12\r\n\x05value\x18\x03 \x01(\t\"p\n\nComparison\x12\t\n\x05\x45QUAL\x10\x00\x12\r\n\tNOT_EQUAL\x10\x01\x12\x10\n\x0cGREATER_THAN\x10\x02\x12\x14\n\x10GREATER_OR_EQUAL\x10\x03\x12\r\n\tLESS_THAN\x10\x04\x12\x11\n\rLESS_OR_EQUAL\x10\x05\"L\n\x05Query\x12\r\n\x05topic\x18\x01 \x01(\t\x12$\n\nconditions\x18\x02 \x03(\x0b\x32\x10.proto.Condition\x12\x0e\n\x06\x63ursor\x18\x03 \x01(\t\"\xd7\x01\n\x0bQueryResult\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.proto.QueryResult\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x1d\n\x04logs\x18\x03 \x03(\x0b\x32\x0f.proto.AuditLog\x12\x0e\n\x06\x63ursor\x18\x04 \x01(\t\"d\n\x0bQueryStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x10\n\x0cUNAUTHORIZED\x10\x01\x12\x11\n\rACCESS_DENIED\x10\x03\x12\x0f\n\x0bQUERY_ERROR\x10\x04\x12\x12\n\x0eINTERNAL_ERROR\x10\x05\x32\x97\x01\n\x07Logging\x12\'\n\x08WriteLog\x12\n.proto.Log\x1a\r.proto.Result\"\x00\x12\x31\n\rWriteAuditLog\x12\x0f.proto.AuditLog\x1a\r.proto.Result\"\x00\x12\x30\n\nAuditQuery\x12\x0c.proto.Query\x1a\x12.proto.QueryResult\"\x00\x42\tZ\x07.;protob\x06proto3'
)



_LOG_LEVEL = _descriptor.EnumDescriptor(
  name='Level',
  full_name='proto.Log.Level',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEBUG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=228,
  serialized_end=301,
)
_sym_db.RegisterEnumDescriptor(_LOG_LEVEL)

_CLAIM_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='proto.Claim.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NUMBER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=375,
  serialized_end=433,
)
_sym_db.RegisterEnumDescriptor(_CLAIM_TYPE)

_RESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='proto.Result.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACKNOWLEDGED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=501,
  serialized_end=584,
)
_sym_db.RegisterEnumDescriptor(_RESULT_STATUS)

_CONDITION_COMPARISON = _descriptor.EnumDescriptor(
  name='Comparison',
  full_name='proto.Condition.Comparison',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EQUAL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_EQUAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREATER_THAN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GREATER_OR_EQUAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS_THAN', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LESS_OR_EQUAL', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=772,
  serialized_end=884,
)
_sym_db.RegisterEnumDescriptor(_CONDITION_COMPARISON)

_QUERYRESULT_QUERYSTATUS = _descriptor.EnumDescriptor(
  name='QueryStatus',
  full_name='proto.QueryResult.QueryStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNAUTHORIZED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUERY_ERROR', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1080,
  serialized_end=1180,
)
_sym_db.RegisterEnumDescriptor(_QUERYRESULT_QUERYSTATUS)


_LOG = _descriptor.Descriptor(
  name='Log',
  full_name='proto.Log',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='proto.Log.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thread', full_name='proto.Log.thread', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Log.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claims', full_name='proto.Log.claims', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='proto.Log.file', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='proto.Log.line', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='function', full_name='proto.Log.function', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='level', full_name='proto.Log.level', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.Log.timestamp', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group', full_name='proto.Log.group', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOG_LEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=301,
)


_CLAIM = _descriptor.Descriptor(
  name='Claim',
  full_name='proto.Claim',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proto.Claim.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Claim.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.Claim.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLAIM_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=433,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='proto.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.Result.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.Result.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESULT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=584,
)


_AUDITLOG = _descriptor.Descriptor(
  name='AuditLog',
  full_name='proto.AuditLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.AuditLog.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claims', full_name='proto.AuditLog.claims', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='topic', full_name='proto.AuditLog.topic', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proto.AuditLog.timestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=586,
  serialized_end=677,
)


_CONDITION = _descriptor.Descriptor(
  name='Condition',
  full_name='proto.Condition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='field', full_name='proto.Condition.field', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='comparison', full_name='proto.Condition.comparison', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.Condition.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONDITION_COMPARISON,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=680,
  serialized_end=884,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='proto.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='topic', full_name='proto.Query.topic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conditions', full_name='proto.Query.conditions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='proto.Query.cursor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=886,
  serialized_end=962,
)


_QUERYRESULT = _descriptor.Descriptor(
  name='QueryResult',
  full_name='proto.QueryResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='proto.QueryResult.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='proto.QueryResult.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='logs', full_name='proto.QueryResult.logs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='proto.QueryResult.cursor', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _QUERYRESULT_QUERYSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=965,
  serialized_end=1180,
)

_LOG.fields_by_name['claims'].message_type = _CLAIM
_LOG.fields_by_name['level'].enum_type = _LOG_LEVEL
_LOG_LEVEL.containing_type = _LOG
_CLAIM.fields_by_name['type'].enum_type = _CLAIM_TYPE
_CLAIM_TYPE.containing_type = _CLAIM
_RESULT.fields_by_name['status'].enum_type = _RESULT_STATUS
_RESULT_STATUS.containing_type = _RESULT
_AUDITLOG.fields_by_name['claims'].message_type = _CLAIM
_CONDITION.fields_by_name['comparison'].enum_type = _CONDITION_COMPARISON
_CONDITION_COMPARISON.containing_type = _CONDITION
_QUERY.fields_by_name['conditions'].message_type = _CONDITION
_QUERYRESULT.fields_by_name['status'].message_type = _QUERYRESULT
_QUERYRESULT.fields_by_name['logs'].message_type = _AUDITLOG
_QUERYRESULT_QUERYSTATUS.containing_type = _QUERYRESULT
DESCRIPTOR.message_types_by_name['Log'] = _LOG
DESCRIPTOR.message_types_by_name['Claim'] = _CLAIM
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['AuditLog'] = _AUDITLOG
DESCRIPTOR.message_types_by_name['Condition'] = _CONDITION
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['QueryResult'] = _QUERYRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Log = _reflection.GeneratedProtocolMessageType('Log', (_message.Message,), {
  'DESCRIPTOR' : _LOG,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.Log)
  })
_sym_db.RegisterMessage(Log)

Claim = _reflection.GeneratedProtocolMessageType('Claim', (_message.Message,), {
  'DESCRIPTOR' : _CLAIM,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.Claim)
  })
_sym_db.RegisterMessage(Claim)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.Result)
  })
_sym_db.RegisterMessage(Result)

AuditLog = _reflection.GeneratedProtocolMessageType('AuditLog', (_message.Message,), {
  'DESCRIPTOR' : _AUDITLOG,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.AuditLog)
  })
_sym_db.RegisterMessage(AuditLog)

Condition = _reflection.GeneratedProtocolMessageType('Condition', (_message.Message,), {
  'DESCRIPTOR' : _CONDITION,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.Condition)
  })
_sym_db.RegisterMessage(Condition)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.Query)
  })
_sym_db.RegisterMessage(Query)

QueryResult = _reflection.GeneratedProtocolMessageType('QueryResult', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULT,
  '__module__' : 'definitions_pb2'
  # @@protoc_insertion_point(class_scope:proto.QueryResult)
  })
_sym_db.RegisterMessage(QueryResult)


DESCRIPTOR._options = None

_LOGGING = _descriptor.ServiceDescriptor(
  name='Logging',
  full_name='proto.Logging',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1183,
  serialized_end=1334,
  methods=[
  _descriptor.MethodDescriptor(
    name='WriteLog',
    full_name='proto.Logging.WriteLog',
    index=0,
    containing_service=None,
    input_type=_LOG,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WriteAuditLog',
    full_name='proto.Logging.WriteAuditLog',
    index=1,
    containing_service=None,
    input_type=_AUDITLOG,
    output_type=_RESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AuditQuery',
    full_name='proto.Logging.AuditQuery',
    index=2,
    containing_service=None,
    input_type=_QUERY,
    output_type=_QUERYRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGGING)

DESCRIPTOR.services_by_name['Logging'] = _LOGGING

# @@protoc_insertion_point(module_scope)
