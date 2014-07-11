from enum import Enum, IntEnum

from stream import StreamIO

class FieldError(Exception):
    pass
    
class FieldSize(IntEnum):
    UInt8  = 1
    UInt16 = 2
    UInt32 = 4
    UInt64 = 8
    String = 9

class Field(IntEnum):
    TransactionVersion = FieldSize.UInt16
    TransactionType    = FieldSize.UInt16
    CurrencyIdentifier = FieldSize.UInt32
    NumberOfCoins      = FieldSize.UInt64
    NumberOfBlocks     = FieldSize.UInt8
    Action             = FieldSize.UInt8
    Ecosystem          = FieldSize.UInt8
    PropertyType       = FieldSize.UInt16
    Text               = FieldSize.String
    Timestamp          = FieldSize.UInt64
    Percentage         = FieldSize.UInt8

    @classmethod
    def find(cls, name):
        try:
            return Field[name]
        except KeyError:
            pass        
        name_normalized = str(name.strip())
        name_normalized = name.replace('-', '')
        name_normalized = name_normalized.replace('_', '')
        name_normalized = name_normalized.upper()
        for name, field in Field.__members__.items():
            field_name = name.upper()
            if field_name == name_normalized:
                return field
        raise FieldError('invalid field: "%s"'%name)

class FieldSerializer(object):
    @classmethod
    def stream_serialize(cls, stream, size, value):
        if size == FieldSize.UInt8:
            stream.write_uint8(value)
        elif size == FieldSize.UInt16:
            stream.write_uint16(value)
        elif size == FieldSize.UInt32:
            stream.write_uint32(value)
        elif size == FieldSize.UInt64:
            stream.write_uint64(value)
        elif size == FieldSize.String:
            stream.write_string(value)

    @classmethod
    def stream_deserialize(cls, stream, size):
        if size == FieldSize.UInt8:
            return stream.read_uint8()
        if size == FieldSize.UInt16:
            return stream.read_uint16()
        if size == FieldSize.UInt32:
            return stream.read_uint32()
        if size == FieldSize.UInt64:
            return stream.read_uint64()
        if size == FieldSize.String:
            return stream.read_string()
        return None
            
    @classmethod
    def serialize(cls, size, value):
        stream = StreamIO()
        cls.stream_serialize(stream, size, value)
        return stream.getvalue()

    @classmethod
    def deserialize(cls, data, size):
        return cls.stream_deserialize(StreamIO(data), size)


class TransactionSerializer(object):
    @classmethod
    def stream_serialize(cls, stream, fields):        
        for field in fields:
            FieldSerializer.stream_serialize(stream, field[0], field[1])

    @classmethod
    def stream_deserialize(cls, stream, field_sizes):
        data = []
        for size in field_sizes:
            value = FieldSerializer.stream_deserialize(stream, size)
            data.append((size, value))
        return data

    @classmethod
    def serialize(cls, fields):
        stream = StreamIO()
        cls.stream_serialize(stream, fields)
        return stream.getvalue()

    @classmethod
    def deserialize(cls, data, field_sizes):
        return cls.stream_deserialize(StreamIO(data), field_sizes)
