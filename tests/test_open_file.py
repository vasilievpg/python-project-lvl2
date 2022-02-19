from gendiff import open_file


def test_open_file():
    content = open_file('./tests/fixtures/file1.json')
    assert content == {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False}
