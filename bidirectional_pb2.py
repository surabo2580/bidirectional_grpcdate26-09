# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bidirectional.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bidirectional.proto',
  package='bidirectional',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x62idirectional.proto\x12\rbidirectional\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"0\n\x0fRegisterMessage\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2\xaf\x01\n\rBidirectional\x12I\n\x11GetServerResponse\x12\x16.bidirectional.Message\x1a\x16.bidirectional.Message\"\x00(\x01\x30\x01\x12S\n\x0fGetRegisterFace\x12\x1e.bidirectional.RegisterMessage\x1a\x1e.bidirectional.RegisterMessage\"\x00\x62\x06proto3'
)




_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='bidirectional.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='bidirectional.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=38,
  serialized_end=64,
)


_REGISTERMESSAGE = _descriptor.Descriptor(
  name='RegisterMessage',
  full_name='bidirectional.RegisterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='bidirectional.RegisterMessage.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='bidirectional.RegisterMessage.message', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=114,
)

DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['RegisterMessage'] = _REGISTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'bidirectional_pb2'
  # @@protoc_insertion_point(class_scope:bidirectional.Message)
  })
_sym_db.RegisterMessage(Message)

RegisterMessage = _reflection.GeneratedProtocolMessageType('RegisterMessage', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMESSAGE,
  '__module__' : 'bidirectional_pb2'
  # @@protoc_insertion_point(class_scope:bidirectional.RegisterMessage)
  })
_sym_db.RegisterMessage(RegisterMessage)



_BIDIRECTIONAL = _descriptor.ServiceDescriptor(
  name='Bidirectional',
  full_name='bidirectional.Bidirectional',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=117,
  serialized_end=292,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='bidirectional.Bidirectional.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRegisterFace',
    full_name='bidirectional.Bidirectional.GetRegisterFace',
    index=1,
    containing_service=None,
    input_type=_REGISTERMESSAGE,
    output_type=_REGISTERMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BIDIRECTIONAL)

DESCRIPTOR.services_by_name['Bidirectional'] = _BIDIRECTIONAL

# @@protoc_insertion_point(module_scope)
