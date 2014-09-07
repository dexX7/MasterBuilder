import json
import unittest

from collections import OrderedDict

from builder.serialize import TransactionSerializer
from builder.parser import normalize_data
from builder.utils import b2x, x


def create_transaction(data):
    fields = normalize_data(data)
    transaction_raw = TransactionSerializer.serialize(fields)
    transaction_hex = b2x(transaction_raw)
    return transaction_hex

def decode_transaction(hex, field_sizes):
    data = TransactionSerializer.deserialize(x(hex), field_sizes)
    return data

# TODO: cli
# TODO: exception handling
# TODO: help
# TODO: tests
if __name__ == '__main__':

    tx_test = """[
        {"type": "version",  "value": 0},
        {"type": "type",     "value": 0},
        {"type": "property", "value": 3},
        {"type": "amount",   "value": 50000}
      ]"""

    tx_hex = create_transaction(tx_test)

    print(tx_hex)
