from gendiff.scripts.gendiff import generate_diff

PATH = 'tests/fixtures/yml/'


def test_diff():
    file1_path = PATH + 'diff1.yml'
    file2_path = PATH + 'diff2.yml'
    assert generate_diff(file1_path, file2_path) == '''{
  - follow: false
  + verbose: true
}'''


def test_diff_values():
    file1_path = PATH + 'diff_values1.yml'
    file2_path = PATH + 'diff_values2.yml'
    assert generate_diff(file1_path, file2_path) == '''{
  - host: hexlet.io
  + host: yandex.ru
}'''


def test_equal():
    file_path = PATH + 'equal.yml'
    assert generate_diff(file_path, file_path) == '''{
    host: hexlet.io
}'''


def test_add():
    file1_path = PATH + 'add1.yml'
    file2_path = PATH + 'add2.yml'
    assert generate_diff(file1_path, file2_path) == '''{
    host: hexlet.io
  + verbose: true
}'''


def test_diff_values_position():
    file1_path = PATH + 'diff_values_pos1.yml'
    file2_path = PATH + 'diff_values_pos2.yml'
    assert generate_diff(file1_path, file2_path) == '''{
    follow: false
  - host: hexlet.io
  + host: yandex.ru
}'''


def test_extension():
    file1_path = PATH + 'extension.yml'
    file2_path = PATH + 'extension.yaml'
    assert generate_diff(file1_path, file2_path) == '''{
    host: hexlet.io
}'''


def test_only_value():
    file1_path = PATH + 'value1.yml'
    file2_path = PATH + 'value2.yml'
    assert generate_diff(file1_path, file2_path) == '''{
  - key: value
  + key: true
}'''
