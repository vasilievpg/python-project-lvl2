from pprint3x import pprint


def construct_diff(data1, data2):
    keys = list(data1.keys() | data2.keys())
    diff_dict = {}
    for key in sorted(keys):
        node = mk_node(data1, data2, key)
        diff_dict[key] = node
    return diff_dict


def mk_node(data1, data2, key):
    value1 = data1.get(key)
    value2 = data2.get(key)
    if key not in data1:
        node = {
            'status': 'added',
            'key': key,
            'value': replace_bool_cap(value2),
        }
    elif key not in data2:
        node = {
            'status': 'removed',
            'key': key,
            'value': replace_bool_cap(value1),
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        node = {
            'status': 'nested',
            'children': construct_diff(value1, value2)
        }
    elif value1 == value2:
        node = {
            'status': 'unchanged',
            'key': key,
            'value': replace_bool_cap(value1),
        }
    else:
        node = {
            'status': 'changed',
            'key': key,
            'value1': replace_bool_cap(value1),
            'value2': replace_bool_cap(value2)
        }
    return node
    # diff_list = ['{']
    # for key, value in diff_dict.items():
    #     diff_list.append(f'  {key}: {value}')
    # diff_list.append('}')
    # return '\n'.join(diff_list)


def replace_bool_cap(word):
    if word is True:
        return 'true'
    if word is False:
        return 'false'
    return word
