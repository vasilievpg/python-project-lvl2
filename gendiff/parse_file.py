import json
import yaml


def open_file(file_path):
    with open(file_path) as file:
        file_extension = file_path[-4:]
        if file_extension == 'json':
            data = json.load(file)
        if file_extension == 'yaml' or file_extension == '.yml':
            data = yaml.load(file, Loader=yaml.Loader)
        return data
