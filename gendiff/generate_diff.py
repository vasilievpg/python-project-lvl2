#!/usr/bin/env python

import argparse
from gendiff.parse_file import open_file
from gendiff.diff_constructor import construct_diff


def generate_diff(file_path1, file_path2):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)
    result = construct_diff(data1, data2)
    return result


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
