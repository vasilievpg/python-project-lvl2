from gendiff import generate_diff
from pprint3x import pprint


def open_txt_file(file_path):
    with open(file_path) as file:
        data = file.read()
        return data


# def test_generate_diff_json():
#     result = generate_diff(
#         './tests/fixtures/file1.json', './tests/fixtures/file2.json')
#     expected_value = open_txt_file('./tests/fixtures/diff_plain.txt')
#     assert result == expected_value


# def test_generate_diff_yaml():
#     result = generate_diff(
#         './tests/fixtures/file1.yaml', './tests/fixtures/file2.yml')
#     expected_value = open_txt_file('./tests/fixtures/diff_plain.txt')
#     assert result == expected_value


def test_generate_diff_json_nested():
    result = generate_diff(
        './tests/fixtures/file1_nested.json',
        './tests/fixtures/file2_nested.json')
    print('\n')
    pprint(result)
    # expected_value = open_txt_file('./tests/fixtures/diff_plain.txt')
    # assert result == expected_value
