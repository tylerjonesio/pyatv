# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pyatv/protocols/mrp/protobuf/RemoveOutputDevicesMessage.proto
# Protobuf Python Version: 5.28.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    0,
    '',
    'pyatv/protocols/mrp/protobuf/RemoveOutputDevicesMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.protocols.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_protocols_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=pyatv/protocols/mrp/protobuf/RemoveOutputDevicesMessage.proto\x1a\x32pyatv/protocols/mrp/protobuf/ProtocolMessage.proto\"K\n\x1aRemoveOutputDevicesMessage\x12\x18\n\x10outputDeviceUIDs\x18\x01 \x03(\t\x12\x13\n\x0b\x65ndpointUID\x18\x02 \x01(\t:Q\n\x1aremoveOutputDevicesMessage\x12\x10.ProtocolMessage\x18\x46 \x01(\x0b\x32\x1b.RemoveOutputDevicesMessage')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyatv.protocols.mrp.protobuf.RemoveOutputDevicesMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMOVEOUTPUTDEVICESMESSAGE']._serialized_start=117
  _globals['_REMOVEOUTPUTDEVICESMESSAGE']._serialized_end=192
# @@protoc_insertion_point(module_scope)
