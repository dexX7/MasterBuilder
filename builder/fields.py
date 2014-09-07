from enum import IntEnum

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
    def add_alias(cls, field, alias):
        for name in alias:
            cls._member_map_[name] = field
            
    @classmethod
    def list_alias(cls, value):
        alias = []
        for name, member in list(cls.__members__.items()):
            if value == member:
                alias.append(name)
        return alias
    
    @classmethod
    def find(cls, name):
        def normalize(word):
            normalized_word = str(word)
            normalized_word = normalized_word.strip()
            normalized_word = normalized_word.replace('-', '')
            normalized_word = normalized_word.replace('_', '')
            normalized_word = normalized_word.upper()
            return normalized_word
        try:
            return Field[name]
        except KeyError:
            pass
        name_normalized = normalize(name)
        for key, value in list(cls.__members__.items()):
            field_name = normalize(key)
            if field_name == name_normalized:
                return value
        return None

Field.add_alias(FieldSize.UInt8,  # 1 byte
                ['uint8', 'int8', 'ubyte', 'byte'])
Field.add_alias(FieldSize.UInt16, # 2 byte
                ['uint16', 'uchar', 'ushort', 'int16', 'char', 'short'])
Field.add_alias(FieldSize.UInt32, # 4 byte
                ['uint32', 'uint', 'uinteger', 'int32', 'int', 'integer'])
Field.add_alias(FieldSize.UInt64, # 8 byte
                ['uint64', 'ulong', 'int64', 'long', 'double'])
Field.add_alias(FieldSize.String, # var len
                ['string'])

Field.add_alias(Field.TransactionVersion,
                ['transaction_version', 'version'])
Field.add_alias(Field.TransactionType,
                ['transaction_type', 'type'])
Field.add_alias(Field.CurrencyIdentifier,
                ['currency_identifier', 'currency_id', 'currency_to_send', 
                 'currency_to_transfer', 'currency_for_sale', 
                 'currency_desired', 'currency_id_desired', 
                 'currency_identifier_desired', 'previous_currency_id', 
                 'previous_currency_identifier', 'property_identifier', 
                 'property_id', 'property_to_send', 'property_to_transfer', 
                 'property_for_sale', 'property_desired', 
                 'property_id_desired', 'property_identifier_desired', 
                 'previous_property_id', 'previous_property_identifier',
                 'property', 'currency'])
Field.add_alias(Field.NumberOfCoins,
                ['number_of_coins', 'amount', 'amount_to_send', 
                 'amount_for_sale', 'amount_desired', 'fee', 'minimum_fee',
                 'transaction_fee', 'min_fee', 'min_transaction_fee', 
                 'minimum_transaction_fee', 'amount_to_transfer', 
                 'amount_to_create', 'amount_per_unit', 
                 'amount_per_unit_vested', 'number_properties'])
Field.add_alias(Field.NumberOfBlocks,
                ['number_of_blocks', 'block_limit', 'block_time_limit', 
                 'payment_timeframe', 'time_limit', 'time_limit_in_blocks'])
Field.add_alias(Field.Action,
                ['action'])
Field.add_alias(Field.Ecosystem,
                ['ecosystem'])
Field.add_alias(Field.PropertyType,
                ['property_type'])
Field.add_alias(Field.Text,
                ['text', 'null_terminated_string', 
                 'property_category', 'property_subcategory', 
                 'property_label', 'property_name', 'property_url',
                 'property_uri', 'property_description', 'property_data',
                 'property_information', 'property_info'])
Field.add_alias(Field.Timestamp,
                ['timestamp', 'unix_timestamp', 'deadline', 'utc_datetime',
                 'gmt_datetime'])
Field.add_alias(Field.Percentage,
                ['percentage', 'bonus', 'earlybird_bonus',
                 'early_bird_bonus', 'bonus_per_week',
                 'percentage_for_issuer', 'bonus_for_issuer',
                 'percentage_for_issuer'])
