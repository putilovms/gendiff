from gendiff.scripts.gendiff import generate_diff

PATH = 'tests/fixtures/recursion/'

stylish = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_diff_del_branch_stylish():
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


def test_diff_del_branch_stylish():
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
    assert generate_diff(file1_path, file2_path) == stylish


def test_diff_yml_stylish():
    file1_path = PATH + 'file_r1.yml'
    file2_path = PATH + 'file_r2.yml'
    assert generate_diff(file1_path, file2_path) == stylish
