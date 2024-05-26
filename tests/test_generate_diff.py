from gendiff.scripts.gendiff import generate_diff
import pytest

PATH = 'tests/fixtures/'
TEST_DATA = [
    ('flat_file1.json', 'flat_file2.json', 'flat_stylish_exp.txt', 'stylish'),
    ('flat_file1.yml', 'flat_file2.yml', 'flat_stylish_exp.txt', 'stylish'),
    ('deep_file1.json', 'deep_file2.json', 'deep_stylish_exp.txt', 'stylish'),
    ('deep_file1.yml', 'deep_file2.yml', 'deep_stylish_exp.txt', 'stylish'),
    ('deep_file1.json', 'deep_file2.json', 'deep_plain_exp.txt', 'plain'),
    ('deep_file1.yml', 'deep_file2.yml', 'deep_plain_exp.txt', 'plain'),
]


def get_path(path):
    return PATH + path


@pytest.mark.parametrize("file1, file2, expected, format_output", TEST_DATA)
def test_generate_diff(file1, file2, expected, format_output):
    with open(get_path(expected), 'r') as f:
        expected_result = f.read()
    assert generate_diff(get_path(file1), get_path(file2),
                         format_output) == expected_result
