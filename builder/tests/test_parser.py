import unittest

from builder.fields import Field, FieldSize
from builder.parser import parse_field, parse_field_list, normalize_data

class TestParser(unittest.TestCase):
    def test_parse_field(self):
        def T(value, expected):
            actual = parse_field(value)
            self.assertEqual(actual, expected)
        T('TransactionVersion', Field.TransactionVersion)
        T('version', Field.TransactionVersion)
        T('transaction_version', Field.TransactionVersion)
        T('does_not_exist', None)
        T(None, None)

    def test_parse_field_list(self):
        def T(value, expected):
            actual = parse_field_list(value)
            self.assertEqual(actual, expected)
        a1 = ['TransactionVersion', 'TransactionType', 'CurrencyIdentifier',
              'NumberOfCoins']
        a2 = ['version', 'transaction_type', 'property_to_send',
              'amount_to_send']
        a3 = ['transaction_version', 'type', None, 'junk', 'currency_id',
              'amount']
        a4 = [Field.TransactionVersion,
              FieldSize.UInt16,
              Field.CurrencyIdentifier,
              Field.NumberOfCoins]
        a5 = [None, 'junk']
        a6 = []

        expected = [Field.TransactionVersion,
                    Field.TransactionType,
                    Field.CurrencyIdentifier,
                    Field.NumberOfCoins]
        T(a1, expected)
        T(a2, expected)
        T(a3, expected)
        T(a4, expected)
        T(a5, [])
        T(a6, [])

    def test_normalize_data_tuple(self):
        def T(value, expected):
            actual = normalize_data(value)
            self.assertEqual(actual, expected)

        T('{"transaction_type": 50}', [(Field.TransactionType, 50)])
        T('{"not_available": 404}',   [])
        T('invalid_data',             [])

    def test_normalize_data(self):
        def T(value, expected):
            actual = normalize_data(value)
            self.assertEqual(actual, expected)
        
        a1 = '[{"type": "type", "value": 50}, {"type": "version", "value": 1}]'
        a2 = '[{"type": 50}, {"version": 1}]'
        a3 = '[["type", 50], ["version", 1]]'
        a4 = '[{"na": 404}, ["type", 50], {"type": "version", "value": 1}]'

        expected = [(Field.TransactionType, 50), (Field.TransactionVersion, 1)]

        T(a1, expected)
        T(a2, expected)
        T(a3, expected)
        T(a4, expected)
        T(expected, expected)


if __name__ == '__main__':
    unittest.main()
