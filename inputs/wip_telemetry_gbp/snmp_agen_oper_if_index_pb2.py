# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='test.proto',
  package='cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index',
  syntax='proto3',
  serialized_pb=_b('\n\ntest.proto\x12\x35\x63isco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index\"3\n\x18snmp_ifindex_ifname_KEYS\x12\x17\n\x0finterface_index\x18\x01 \x01(\r\"-\n\x13snmp_ifindex_ifname\x12\x16\n\x0einterface_name\x18\x32 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SNMP_IFINDEX_IFNAME_KEYS = _descriptor.Descriptor(
  name='snmp_ifindex_ifname_KEYS',
  full_name='cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname_KEYS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_index', full_name='cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname_KEYS.interface_index', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=69,
  serialized_end=120,
)


_SNMP_IFINDEX_IFNAME = _descriptor.Descriptor(
  name='snmp_ifindex_ifname',
  full_name='cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface_name', full_name='cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname.interface_name', index=0,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=122,
  serialized_end=167,
)

DESCRIPTOR.message_types_by_name['snmp_ifindex_ifname_KEYS'] = _SNMP_IFINDEX_IFNAME_KEYS
DESCRIPTOR.message_types_by_name['snmp_ifindex_ifname'] = _SNMP_IFINDEX_IFNAME

snmp_ifindex_ifname_KEYS = _reflection.GeneratedProtocolMessageType('snmp_ifindex_ifname_KEYS', (_message.Message,), dict(
  DESCRIPTOR = _SNMP_IFINDEX_IFNAME_KEYS,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname_KEYS)
  ))
_sym_db.RegisterMessage(snmp_ifindex_ifname_KEYS)

snmp_ifindex_ifname = _reflection.GeneratedProtocolMessageType('snmp_ifindex_ifname', (_message.Message,), dict(
  DESCRIPTOR = _SNMP_IFINDEX_IFNAME,
  __module__ = 'test_pb2'
  # @@protoc_insertion_point(class_scope:cisco_ios_xr_snmp_agent_oper.snmp.if_indexes.if_index.snmp_ifindex_ifname)
  ))
_sym_db.RegisterMessage(snmp_ifindex_ifname)


# @@protoc_insertion_point(module_scope)
