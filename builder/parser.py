from fields import Field

def parse_field(name):
    size = Field.find(name)
    return size

def parse_field_list(field_names):
    fields = []
    for name in field_names:
        size = parse_field(name)
        if size != None:
            fields.append(size)
        else:            
            pass # maybe be more strict
    return fields
