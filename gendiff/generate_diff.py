#!/usr/bin/env python

import argparse
import json


def generate_diff(file_path1, file_path2):
    with json.load(open(file_path1)) as file1:
        with json.load(open(file_path2)) as file2:
            return file_path1, file_path2


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
