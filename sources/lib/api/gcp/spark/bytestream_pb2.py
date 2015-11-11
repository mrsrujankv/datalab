# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/bytestream/bytestream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
import google3
from google3.net.proto2.python.public import descriptor as _descriptor
from google3.net.proto2.python.public import message as _message
from google3.net.proto2.python.public import reflection as _reflection
from google3.net.proto2.python.public import symbol_database as _symbol_database
from google3.net.proto2.proto import descriptor_pb2
import sys
try:
  __import__('google3.net.rpc.python.rpc_internals_lite')
  __import__('google3.net.rpc.python.pywraprpc_lite')
  rpc_internals = sys.modules.get('google3.net.rpc.python.rpc_internals_lite')
  pywraprpc = sys.modules.get('google3.net.rpc.python.pywraprpc_lite')
  _client_stub_base_class = rpc_internals.StubbyRPCBaseStub
except ImportError:
  _client_stub_base_class = object
try:
  __import__('google3.net.rpc.python.rpcserver')
  rpcserver = sys.modules.get('google3.net.rpc.python.rpcserver')
  _server_stub_base_class = rpcserver.BaseRpcServer
except ImportError:
  _server_stub_base_class = object
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google3.google.api import annotations_pb2 as google3_dot_google_dot_api_dot_annotations__pb2
from google3.google.protobuf import wrappers_pb2 as google3_dot_google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/bytestream/bytestream.proto',
  package='google.bytestream',
  syntax='proto3',
  serialized_pb=_b('\n\"google/bytestream/bytestream.proto\x12\x11google.bytestream\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\"Q\n\x0bReadRequest\x12\x19\n\rresource_name\x18\x01 \x01(\tB\x02h\x00\x12\x13\n\x0bread_offset\x18\x02 \x01(\x03\x12\x12\n\nread_limit\x18\x03 \x01(\x03\"s\n\x0cReadResponse\x12\x10\n\x04\x64\x61ta\x18\n \x01(\x0c\x42\x02\x08\x01\x12Q\n\x13\x66inal_resource_size\x18\x14 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x17\xfa\xd2\xe4\x93\x02\x11\x12\x0fGOOGLE_INTERNAL\"g\n\x0cWriteRequest\x12\x19\n\rresource_name\x18\x01 \x01(\tB\x02h\x00\x12\x14\n\x0cwrite_offset\x18\x02 \x01(\x03\x12\x14\n\x0c\x66inish_write\x18\x03 \x01(\x08\x12\x10\n\x04\x64\x61ta\x18\n \x01(\x0c\x42\x02\x08\x01\"\'\n\rWriteResponse\x12\x16\n\x0e\x63ommitted_size\x18\x01 \x01(\x03\"4\n\x17QueryWriteStatusRequest\x12\x19\n\rresource_name\x18\x01 \x01(\tB\x02h\x00\"D\n\x18QueryWriteStatusResponse\x12\x16\n\x0e\x63ommitted_size\x18\x01 \x01(\x03\x12\x10\n\x08\x63omplete\x18\x02 \x01(\x08\x32\xaa\x02\n\nByteStream\x12T\n\x04Read\x12\x1e.google.bytestream.ReadRequest\x1a\x1f.google.bytestream.ReadResponse\"\t\xa8\x01\x01\xc8\x01\x80\xf8\x80\x03\x30\x01\x12W\n\x05Write\x12\x1f.google.bytestream.WriteRequest\x1a .google.bytestream.WriteResponse\"\t\xa0\x01\x01\xc0\x01\x80\xf8\x80\x03(\x01\x12m\n\x10QueryWriteStatus\x12*.google.bytestream.QueryWriteStatusRequest\x1a+.google.bytestream.QueryWriteStatusResponse\"\x00\x42:\n\x15\x63om.google.bytestreamB\x0f\x42yteStreamProtob\x10\x62ytestream.protob\x06proto3')
  ,
  dependencies=[google3_dot_google_dot_api_dot_annotations__pb2.DESCRIPTOR,google3_dot_google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='google.bytestream.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.bytestream.ReadRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))),
    _descriptor.FieldDescriptor(
      name='read_offset', full_name='google.bytestream.ReadRequest.read_offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_limit', full_name='google.bytestream.ReadRequest.read_limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=200,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='google.bytestream.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='google.bytestream.ReadResponse.data', index=0,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\010\001'))),
    _descriptor.FieldDescriptor(
      name='final_resource_size', full_name='google.bytestream.ReadResponse.final_resource_size', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\322\344\223\002\021\022\017GOOGLE_INTERNAL'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=317,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='google.bytestream.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.bytestream.WriteRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))),
    _descriptor.FieldDescriptor(
      name='write_offset', full_name='google.bytestream.WriteRequest.write_offset', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finish_write', full_name='google.bytestream.WriteRequest.finish_write', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='google.bytestream.WriteRequest.data', index=3,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\010\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=422,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='google.bytestream.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='committed_size', full_name='google.bytestream.WriteResponse.committed_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=463,
)


_QUERYWRITESTATUSREQUEST = _descriptor.Descriptor(
  name='QueryWriteStatusRequest',
  full_name='google.bytestream.QueryWriteStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.bytestream.QueryWriteStatusRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=517,
)


_QUERYWRITESTATUSRESPONSE = _descriptor.Descriptor(
  name='QueryWriteStatusResponse',
  full_name='google.bytestream.QueryWriteStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='committed_size', full_name='google.bytestream.QueryWriteStatusResponse.committed_size', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='complete', full_name='google.bytestream.QueryWriteStatusResponse.complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=587,
)

_READRESPONSE.fields_by_name['final_resource_size'].message_type = google3_dot_google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['QueryWriteStatusRequest'] = _QUERYWRITESTATUSREQUEST
DESCRIPTOR.message_types_by_name['QueryWriteStatusResponse'] = _QUERYWRITESTATUSRESPONSE

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), dict(
  DESCRIPTOR = _READREQUEST,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.ReadRequest)
  ))
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), dict(
  DESCRIPTOR = _READRESPONSE,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.ReadResponse)
  ))
_sym_db.RegisterMessage(ReadResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), dict(
  DESCRIPTOR = _WRITEREQUEST,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.WriteRequest)
  ))
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), dict(
  DESCRIPTOR = _WRITERESPONSE,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.WriteResponse)
  ))
_sym_db.RegisterMessage(WriteResponse)

QueryWriteStatusRequest = _reflection.GeneratedProtocolMessageType('QueryWriteStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYWRITESTATUSREQUEST,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.QueryWriteStatusRequest)
  ))
_sym_db.RegisterMessage(QueryWriteStatusRequest)

QueryWriteStatusResponse = _reflection.GeneratedProtocolMessageType('QueryWriteStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYWRITESTATUSRESPONSE,
  __module__ = 'google3.google.bytestream.bytestream_pb2'
  # @@protoc_insertion_point(class_scope:google.bytestream.QueryWriteStatusResponse)
  ))
_sym_db.RegisterMessage(QueryWriteStatusResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.bytestreamB\017ByteStreamProtob\020bytestream.proto'))
_READREQUEST.fields_by_name['resource_name'].has_options = True
_READREQUEST.fields_by_name['resource_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))
_READRESPONSE.fields_by_name['data'].has_options = True
_READRESPONSE.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\010\001'))
_READRESPONSE.fields_by_name['final_resource_size'].has_options = True
_READRESPONSE.fields_by_name['final_resource_size']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\372\322\344\223\002\021\022\017GOOGLE_INTERNAL'))
_WRITEREQUEST.fields_by_name['resource_name'].has_options = True
_WRITEREQUEST.fields_by_name['resource_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))
_WRITEREQUEST.fields_by_name['data'].has_options = True
_WRITEREQUEST.fields_by_name['data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\010\001'))
_QUERYWRITESTATUSREQUEST.fields_by_name['resource_name'].has_options = True
_QUERYWRITESTATUSREQUEST.fields_by_name['resource_name']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('h\000'))


class _ByteStream_ClientBaseStub(_client_stub_base_class):
  """Makes Stubby RPC calls to a ByteStream server."""

  __slots__ = (
      '_protorpc_QueryWriteStatus', '_full_name_QueryWriteStatus',
  )

  def __init__(self, rpc_stub):
    self._stub = rpc_stub

    self._protorpc_QueryWriteStatus = pywraprpc.RPC()
    self._full_name_QueryWriteStatus = self._stub.GetFullMethodName(
        'QueryWriteStatus')

  def QueryWriteStatus(self, request, rpc=None, callback=None, response=None):
    """Make a QueryWriteStatus RPC call.

    Args:
      request: a QueryWriteStatusRequest instance.
      rpc: Optional RPC instance to use for the call.
      callback: Optional final callback. Will be called as
          callback(rpc, result) when the rpc completes. If None, the
          call is synchronous.
      response: Optional ProtocolMessage to be filled in with response.

    Returns:
      The QueryWriteStatusResponse if callback is None. Otherwise, returns None.
    """

    if response is None:
      response = QueryWriteStatusResponse
    return self._MakeCall(rpc,
                          self._full_name_QueryWriteStatus,
                          'QueryWriteStatus',
                          request,
                          response,
                          callback,
                          self._protorpc_QueryWriteStatus,
                          package_name='google.bytestream')


class _ByteStream_ClientStub(_ByteStream_ClientBaseStub):
  __slots__ = ('_params',)
  def __init__(self, rpc_stub_parameters, service_name):
    if service_name is None:
      service_name = 'ByteStream'
    _ByteStream_ClientBaseStub.__init__(self, pywraprpc.RPC_GenericStub(service_name, rpc_stub_parameters))
    self._params = rpc_stub_parameters


class _ByteStream_RPC2ClientStub(_ByteStream_ClientBaseStub):
  __slots__ = ()
  def __init__(self, server, channel, service_name):
    if service_name is None:
      service_name = 'ByteStream'
    if channel is not None:
      if channel.version() == 1:
        raise RuntimeError('Expecting an RPC2 channel to create the stub')
      _ByteStream_ClientBaseStub.__init__(self, pywraprpc.RPC_GenericStub(service_name, channel))
    elif server is not None:
      _ByteStream_ClientBaseStub.__init__(self, pywraprpc.RPC_GenericStub(service_name, pywraprpc.NewClientChannel(server)))
    else:
      raise RuntimeError('Invalid argument combination to create a stub')


class ByteStream(_server_stub_base_class):
  """Base class for ByteStream Stubby servers."""

  @classmethod
  def _MethodSignatures(cls):
    """Returns a dict of {<method-name>: (<request-type>, <response-type>)}."""
    return {
      'QueryWriteStatus': (QueryWriteStatusRequest, QueryWriteStatusResponse),
      }

  @classmethod
  def _StreamMethodSignatures(cls):
    """Returns a dict of {<method-name>: (<request-type>, <stream-type>, <response-type>)}."""
    return {
      }

  def __init__(self, *args, **kwargs):
    """Creates a Stubby RPC server.

    The arguments to this constructor are the same as the arguments to
    BaseRpcServer.__init__ in rpcserver.py *MINUS* export_name. This
    constructor passes its own value for export_name to
    BaseRpcServer.__init__, so callers of this constructor should only
    pass to this constructor values corresponding to
    BaseRpcServer.__init__'s remaining arguments.
    """
    if _server_stub_base_class is object:
      raise NotImplementedError('Add //net/rpc/python:rpcserver as a '
                                'dependency for Stubby server support.')
    _server_stub_base_class.__init__(self, 'google.bytestream.ByteStream', *args, **kwargs)

  @staticmethod
  def NewStub(rpc_stub_parameters, service_name=None):
    """Creates a new ByteStream Stubby client stub.

    Args:
      rpc_stub_parameters: an RPC_StubParameters instance.
      service_name: the service name used by the Stubby server.
    """

    if _client_stub_base_class is object:
      raise RuntimeError('Add //net/rpc/python as a dependency to use Stubby')
    return _ByteStream_ClientStub(rpc_stub_parameters, service_name)

  @staticmethod
  def NewRPC2Stub(server=None, channel=None, service_name=None):
    """Creates a new ByteStream Stubby2 client stub.

    Args:
      server: host:port or bns address.
      channel: directly use a channel to create a stub. Will ignore server
          argument if this is specified.
      service_name: the service name used by the Stubby server.
    """

    if _client_stub_base_class is object:
      raise RuntimeError('Add //net/rpc/python as a dependency to use Stubby')
    return _ByteStream_RPC2ClientStub(server, channel, service_name)

  def QueryWriteStatus(self, rpc, request, response):
    """Handles a QueryWriteStatus RPC call. You should override this.

    Args:
      rpc: a Stubby RPC object
      request: a QueryWriteStatusRequest that contains the client request
      response: a QueryWriteStatusResponse that should be modified to send the response
    """
    raise NotImplementedError

  def _AddMethodAttributes(self):
    """Sets attributes on Python RPC handlers.

    See BaseRpcServer in rpcserver.py for details.
    """
    rpcserver._GetHandlerDecorator(
        getattr(self.QueryWriteStatus, '__func__'),
        QueryWriteStatusRequest,
        QueryWriteStatusResponse,
        None,
        'INTEGRITY')

# @@protoc_insertion_point(module_scope)
