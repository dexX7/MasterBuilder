import json

from serialize import TransactionSerializer, Field
from utils import b2x, x

def create_transaction(data):
    transaction_raw = TransactionSerializer.serialize(data)
    transaction_hex = b2x(transaction_raw)
    return transaction_hex

def decode_transaction(hex, field_sizes):
    data = TransactionSerializer.deserialize(x(hex), field_sizes)
    return data

# TODO: parse from json, parse to json
# TODO: cli
# TODO: type checking
# TODO: exception handling
# TODO: help
# TODO: tests
