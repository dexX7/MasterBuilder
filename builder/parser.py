import json

from fields import Field, FieldSize

def parse_field(name):    
    if isinstance(name, Field) or isinstance(name, FieldSize):
        size = name
    else:
        size = Field.find(name)
    return size

def parse_field_list(field_names):
    fields = []
    for name in field_names:
        size = parse_field(name)
        if size != None:
            fields.append(size)
    return fields

def parse_dict(element):
    assert isinstance(element, dict)

    # {"version": 0} -> ("version", 0)
    if len(element) == 1:        
        key = dict.keys(element)[0]
        return (key, element[key],)

    # {"type": "version", "value": 0} -> ("version", 0)
    if len(element) == 2 and 'type' in element and 'value' in element:
        return (element['type'], element['value'],)

    # {"version": 0, "amount": 9001) -> [("type", 7), ("amount", 9001)]
    fields = []
    for key in element.iterkeys():
        field = (key, element[key],)
        fields.append(field)
    return fields

def parse_list(elements):
    assert isinstance(elements, list)

    fields = []
    for element in elements:
        if isinstance(element, dict):
            element = parse_dict(element)
        if len(element) != 2:
            continue
        field = (parse_field(element[0]), element[1])
        if field[0] != None:
            fields.append(field)
                        
    return fields

def parse_str(element):
    assert isinstance(element, str)
    try:
        return json.loads(element)
    except:
        return []
    
def normalize_data(fields):
    """Returns [(Field.Type, value), (Field.Type, value)]"""    
    if isinstance(fields, str):
        fields = parse_str(fields)

    if isinstance(fields, dict):
        fields = parse_dict(fields)

    if isinstance(fields, tuple):
        fields = [fields]

    if isinstance(fields, list):
        fields = parse_list(fields)

    return fields
