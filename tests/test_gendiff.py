from gendiff import generate_diff


def open_txt_file(file_path):
    with open(file_path) as file:
        data = file.read()
        return data


def test_generate_diff():
    result = generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')
    expected_value = open_txt_file('./tests/fixtures/expected_value.txt')
    assert result == expected_value

