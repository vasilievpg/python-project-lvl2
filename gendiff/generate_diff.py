#!/usr/bin/env python

import argparse
import json


def open_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
        return data


def replace_capital(word):
    if word is True:
        return 'true'
    if word is False:
        return 'false'
    return word


def generate_diff(file_path1, file_path2):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)
    keys = data1.keys() | data2.keys()
    diff_dict = {}
    for key in sorted(keys):
        if key not in data1:
            diff_dict[f'+ {key}'] = replace_capital(data2[key])
        elif key not in data2:
            diff_dict[f'- {key}'] = replace_capital(data1[key])
        elif data1[key] == data2[key]:
            diff_dict[f'  {key}'] = replace_capital(data1[key])
        else:
            diff_dict[f'- {key}'] = replace_capital(data1[key])
            diff_dict[f'+ {key}'] = replace_capital(data2[key])
    diff_list = ['{']
    for key, value in diff_dict.items():
        diff_list.append(f'  {key}: {value}')
    diff_list.append('}')
    return '\n'.join(diff_list)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    my_namespace = parser.parse_args()
    file_path1 = my_namespace.first_file
    file_path2 = my_namespace.second_file
    print('\n' + generate_diff(file_path1, file_path2))


if __name__ == '__main__':
    main()
