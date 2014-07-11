import struct

class StreamIO(object):
    def __init__(self, data=b''):
        self.input = data
        self.read_cursor = 0

    def clear(self):
        self.input = b''
        self.read_cursor = 0

    def reset(self):
        self.seek(0)

    def seek(self, position):
        self.read_cursor = position

    def getvalue(self):
        return self.input

    def read(self, size):
        buf = self.input[self.read_cursor:self.read_cursor+size]
        self.read_cursor += size
        return buf

    def write(self, value):
        size = len(value)
        self.input += value
        self.read_cursor += size

    def unpack(self, format):
        size = struct.calcsize(format)
        try:
            buf = self.read(size)
            return struct.unpack(format, buf)[0]
        except:
            return b''

    def pack(self, format, value):
        try:
            buf = struct.pack(format, value)
            self.write(buf)
        except:
            pass
        
    def write_string(self, message):
        self.write(message)
        self.write_uint8(0)

    def read_string(self):
        msg = b''
        buf = self.read(1)
        while buf and buf != b'\x00':
            msg += buf
            buf = self.read(1)
        return msg

    def read_uint8(self):
        return self.unpack('>B')

    def read_uint16(self):
        return self.unpack('>H')

    def read_uint32(self):
        return self.unpack('>I')

    def read_uint64(self):
        return self.unpack('>Q')

    def write_uint8(self, value):
        self.pack('>B', value)

    def write_uint16(self, value):
        self.pack('>H', value)

    def write_uint32(self, value):
        self.pack('>I', value)

    def write_uint64(self, value):
        self.pack('>Q', value)
