import binascii
import struct
import sys

def x(h):
    """Convert a hex string to bytes."""
    if sys.version > '3':
        return binascii.unhexlify(h.encode('utf8'))
    else:
        return binascii.unhexlify(h)

def b2x(b):
    """Convert bytes to a hex string."""
    if sys.version > '3':
        return binascii.hexlify(b).decode('utf8')
    else:
        return binascii.hexlify(b)
        
def lx(h):
    """Convert a little-endian hex string to bytes."""
    import sys
    if sys.version > '3':
        return binascii.unhexlify(h.encode('utf8'))[::-1]
    else:
        return binascii.unhexlify(h)[::-1]

def b2lx(b):
    """Convert bytes to a little-endian hex string."""
    if sys.version > '3':
        return binascii.hexlify(b[::-1]).decode('utf8')
    else:
        return binascii.hexlify(b[::-1])

def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False
