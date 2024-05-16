from gendiff.scripts.gendiff import generate_diff

PATH = 'tests/fixtures/recursion/'


def test_diff_plain():
    file1_path = PATH + 'file_r1.json'
    file2_path = PATH + 'file_r2.json'
    assert generate_diff(file1_path, file2_path, 'plain') == \
        '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
