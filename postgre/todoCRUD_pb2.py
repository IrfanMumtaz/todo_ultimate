# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todoCRUD.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='todoCRUD.proto',
  package='todoCRUD',
  syntax='proto3',
  serialized_options=None,
<<<<<<< HEAD
  serialized_pb=_b('\n\x0etodoCRUD.proto\x12\x08todoCRUD\"\x0c\n\nAllRequest\"\x1c\n\rSingleRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\"Q\n\x0eSingleResponse\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"C\n\rCreateRequest\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"P\n\rUpdateRequest\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"\x89\x01\n\x0b\x41llResponse\x12\x34\n\x06result\x18\x01 \x03(\x0b\x32$.todoCRUD.AllResponse.SingleResponse\x1a\x44\n\x0eSingleResponse\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t2\xd3\x02\n\x08ToDoCRUD\x12;\n\x05tasks\x12\x14.todoCRUD.AllRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x30\x01\x12\x41\n\ntaskSingle\x12\x17.todoCRUD.SingleRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskCreate\x12\x17.todoCRUD.CreateRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskUpdate\x12\x17.todoCRUD.UpdateRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskDelete\x12\x17.todoCRUD.SingleRequest\x1a\x18.todoCRUD.DeleteResponse\"\x00\x62\x06proto3')
=======
  serialized_pb=_b('\n\x0etodoCRUD.proto\x12\x08todoCRUD\"\x0c\n\nAllRequest\"\x1c\n\rSingleRequest\x12\x0b\n\x03_id\x18\x01 \x01(\x05\"Q\n\x0eSingleResponse\x12\x0b\n\x03_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"C\n\rCreateRequest\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"P\n\rUpdateRequest\x12\x0b\n\x03_id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"\x89\x01\n\x0b\x41llResponse\x12\x34\n\x06result\x18\x01 \x03(\x0b\x32$.todoCRUD.AllResponse.SingleResponse\x1a\x44\n\x0eSingleResponse\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t2\xd3\x02\n\x08ToDoCRUD\x12;\n\x05tasks\x12\x14.todoCRUD.AllRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x30\x01\x12\x41\n\ntaskSingle\x12\x17.todoCRUD.SingleRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskCreate\x12\x17.todoCRUD.CreateRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskUpdate\x12\x17.todoCRUD.UpdateRequest\x1a\x18.todoCRUD.SingleResponse\"\x00\x12\x41\n\ntaskDelete\x12\x17.todoCRUD.SingleRequest\x1a\x18.todoCRUD.DeleteResponse\"\x00\x62\x06proto3')
>>>>>>> ced95405fb919911260ae988f63a4674a0020e6f
)




_ALLREQUEST = _descriptor.Descriptor(
  name='AllRequest',
  full_name='todoCRUD.AllRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=28,
  serialized_end=40,
)


_SINGLEREQUEST = _descriptor.Descriptor(
  name='SingleRequest',
  full_name='todoCRUD.SingleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='todoCRUD.SingleRequest._id', index=0,
<<<<<<< HEAD
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
=======
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
>>>>>>> ced95405fb919911260ae988f63a4674a0020e6f
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
  serialized_start=42,
  serialized_end=70,
)


_SINGLERESPONSE = _descriptor.Descriptor(
  name='SingleResponse',
  full_name='todoCRUD.SingleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='todoCRUD.SingleResponse._id', index=0,
<<<<<<< HEAD
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
=======
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
>>>>>>> ced95405fb919911260ae988f63a4674a0020e6f
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='todoCRUD.SingleResponse.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todoCRUD.SingleResponse.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todoCRUD.SingleResponse.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=72,
  serialized_end=153,
)


_CREATEREQUEST = _descriptor.Descriptor(
  name='CreateRequest',
  full_name='todoCRUD.CreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='todoCRUD.CreateRequest.title', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todoCRUD.CreateRequest.description', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todoCRUD.CreateRequest.status', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=155,
  serialized_end=222,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='todoCRUD.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='todoCRUD.DeleteResponse.message', index=0,
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
  serialized_start=224,
  serialized_end=257,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='todoCRUD.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='todoCRUD.UpdateRequest._id', index=0,
<<<<<<< HEAD
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
=======
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
>>>>>>> ced95405fb919911260ae988f63a4674a0020e6f
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='todoCRUD.UpdateRequest.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todoCRUD.UpdateRequest.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todoCRUD.UpdateRequest.status', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=259,
  serialized_end=339,
)


_ALLRESPONSE_SINGLERESPONSE = _descriptor.Descriptor(
  name='SingleResponse',
  full_name='todoCRUD.AllResponse.SingleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='todoCRUD.AllResponse.SingleResponse.title', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='todoCRUD.AllResponse.SingleResponse.description', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='todoCRUD.AllResponse.SingleResponse.status', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=411,
  serialized_end=479,
)

_ALLRESPONSE = _descriptor.Descriptor(
  name='AllResponse',
  full_name='todoCRUD.AllResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='todoCRUD.AllResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ALLRESPONSE_SINGLERESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=479,
)

_ALLRESPONSE_SINGLERESPONSE.containing_type = _ALLRESPONSE
_ALLRESPONSE.fields_by_name['result'].message_type = _ALLRESPONSE_SINGLERESPONSE
DESCRIPTOR.message_types_by_name['AllRequest'] = _ALLREQUEST
DESCRIPTOR.message_types_by_name['SingleRequest'] = _SINGLEREQUEST
DESCRIPTOR.message_types_by_name['SingleResponse'] = _SINGLERESPONSE
DESCRIPTOR.message_types_by_name['CreateRequest'] = _CREATEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['AllResponse'] = _ALLRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AllRequest = _reflection.GeneratedProtocolMessageType('AllRequest', (_message.Message,), dict(
  DESCRIPTOR = _ALLREQUEST,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.AllRequest)
  ))
_sym_db.RegisterMessage(AllRequest)

SingleRequest = _reflection.GeneratedProtocolMessageType('SingleRequest', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEREQUEST,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.SingleRequest)
  ))
_sym_db.RegisterMessage(SingleRequest)

SingleResponse = _reflection.GeneratedProtocolMessageType('SingleResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLERESPONSE,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.SingleResponse)
  ))
_sym_db.RegisterMessage(SingleResponse)

CreateRequest = _reflection.GeneratedProtocolMessageType('CreateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEREQUEST,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.CreateRequest)
  ))
_sym_db.RegisterMessage(CreateRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEREQUEST,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.UpdateRequest)
  ))
_sym_db.RegisterMessage(UpdateRequest)

AllResponse = _reflection.GeneratedProtocolMessageType('AllResponse', (_message.Message,), dict(

  SingleResponse = _reflection.GeneratedProtocolMessageType('SingleResponse', (_message.Message,), dict(
    DESCRIPTOR = _ALLRESPONSE_SINGLERESPONSE,
    __module__ = 'todoCRUD_pb2'
    # @@protoc_insertion_point(class_scope:todoCRUD.AllResponse.SingleResponse)
    ))
  ,
  DESCRIPTOR = _ALLRESPONSE,
  __module__ = 'todoCRUD_pb2'
  # @@protoc_insertion_point(class_scope:todoCRUD.AllResponse)
  ))
_sym_db.RegisterMessage(AllResponse)
_sym_db.RegisterMessage(AllResponse.SingleResponse)



_TODOCRUD = _descriptor.ServiceDescriptor(
  name='ToDoCRUD',
  full_name='todoCRUD.ToDoCRUD',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=482,
  serialized_end=821,
  methods=[
  _descriptor.MethodDescriptor(
    name='tasks',
    full_name='todoCRUD.ToDoCRUD.tasks',
    index=0,
    containing_service=None,
    input_type=_ALLREQUEST,
    output_type=_SINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='taskSingle',
    full_name='todoCRUD.ToDoCRUD.taskSingle',
    index=1,
    containing_service=None,
    input_type=_SINGLEREQUEST,
    output_type=_SINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='taskCreate',
    full_name='todoCRUD.ToDoCRUD.taskCreate',
    index=2,
    containing_service=None,
    input_type=_CREATEREQUEST,
    output_type=_SINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='taskUpdate',
    full_name='todoCRUD.ToDoCRUD.taskUpdate',
    index=3,
    containing_service=None,
    input_type=_UPDATEREQUEST,
    output_type=_SINGLERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='taskDelete',
    full_name='todoCRUD.ToDoCRUD.taskDelete',
    index=4,
    containing_service=None,
    input_type=_SINGLEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOCRUD)

DESCRIPTOR.services_by_name['ToDoCRUD'] = _TODOCRUD

# @@protoc_insertion_point(module_scope)
