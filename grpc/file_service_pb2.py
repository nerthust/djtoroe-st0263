# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66ile_service.proto\"\x1d\n\x08\x46ileList\x12\x11\n\tfilenames\x18\x01 \x03(\t\"%\n\x0c\x46ileResponse\x12\x15\n\rfile_contents\x18\x01 \x01(\x0c\"\x07\n\x05\x45mpty\"\x1f\n\x0b\x46ileRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t2Z\n\x0b\x46ileService\x12 \n\tListFiles\x12\x06.Empty\x1a\t.FileList\"\x00\x12)\n\x08ReadFile\x12\x0c.FileRequest\x1a\r.FileResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FILELIST._serialized_start=22
  _FILELIST._serialized_end=51
  _FILERESPONSE._serialized_start=53
  _FILERESPONSE._serialized_end=90
  _EMPTY._serialized_start=92
  _EMPTY._serialized_end=99
  _FILEREQUEST._serialized_start=101
  _FILEREQUEST._serialized_end=132
  _FILESERVICE._serialized_start=134
  _FILESERVICE._serialized_end=224
# @@protoc_insertion_point(module_scope)
