# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filelocation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filelocation.proto',
  package='grpc_protos.textmining',
  syntax='proto3',
  serialized_options=_b('\n\026grpc_protos.textminingB\014FileLocationP\000'),
  serialized_pb=_b('\n\x12\x66ilelocation.proto\x12\x16grpc_protos.textmining\" \n\x0c\x46ileLocation\x12\x10\n\x08location\x18\x01 \x01(\tB(\n\x16grpc_protos.textminingB\x0c\x46ileLocationP\x00\x62\x06proto3')
)




_FILELOCATION = _descriptor.Descriptor(
  name='FileLocation',
  full_name='grpc_protos.textmining.FileLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='location', full_name='grpc_protos.textmining.FileLocation.location', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=46,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['FileLocation'] = _FILELOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileLocation = _reflection.GeneratedProtocolMessageType('FileLocation', (_message.Message,), dict(
  DESCRIPTOR = _FILELOCATION,
  __module__ = 'filelocation_pb2'
  # @@protoc_insertion_point(class_scope:grpc_protos.textmining.FileLocation)
  ))
_sym_db.RegisterMessage(FileLocation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)