def do_stuff_1(data, config):
    if config[KEY] == "condition1":
        return convert_data_1(data)
    elif config[KEY] == "condition2":
        return convert_data_2(data)
    else:
        return convert_data_3(data)
    
    
def do_stuff_2(data, config):
    if config[KEY] == "condition1":
        return serialize_data_1(data)
    elif config[KEY] == "condition2":
        return serialize_data_2(data)
    else:
        return serialize_data_3(data)
    

def convert_data_1(a):
    return a
def convert_data_2(a):
    return a
def convert_data_3(a):
    return a
def serialize_data_1(a):
    return a
def serialize_data_2(a):
    return a
def serialize_data_3(a):
    return a


def do_stuff(data, config):
    convert_data, serialize_data = \
        convert_data_1(data), serialize_data_1(data) if config[KEY] == "condition1" \
            convert_data_2(data), serialize_data_2(data) elif config[KEY] == "condition2" \
                else convert_data_3(data), serialize_data_3(data)
                
    return convert_data, serialize_data