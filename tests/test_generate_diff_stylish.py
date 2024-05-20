from gendiff.scripts.gendiff import generate_diff

PATH = 'tests/fixtures/recursion/'


def test_diff_del_branch_first_stylish():
    file1_path = PATH + 'edit_branch1.json'
    file2_path = PATH + 'edit_branch2.json'
    assert generate_diff(file1_path, file2_path) == '''{
    group1: {
      - nest: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
      + nest: str
    }
}'''


def test_diff_del_branch_second_stylish():
    file1_path = PATH + 'edit_branch2.json'
    file2_path = PATH + 'edit_branch1.json'
    assert generate_diff(file1_path, file2_path) == '''{
    group1: {
      - nest: str
      + nest: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }
}'''


def test_diff_json_stylish():
    file1_path = PATH + 'file_r1.json'
    file2_path = PATH + 'file_r2.json'
    with open(PATH + 'expected.txt', 'r') as f:
        expected_result = f.read()
    assert generate_diff(file1_path, file2_path) == expected_result


def test_diff_yml_stylish():
    file1_path = PATH + 'file_r1.yml'
    file2_path = PATH + 'file_r2.yml'
    with open(PATH + 'expected.txt', 'r') as f:
        expected_result = f.read()
    assert generate_diff(file1_path, file2_path) == expected_result
