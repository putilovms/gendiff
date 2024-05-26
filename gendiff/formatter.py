from gendiff.formats.stylish import format_stylish
from gendiff.formats.plain import format_plain
from gendiff.formats.json import format_json


def format_tree(ast_tree, format):
    result = []
    match format:
        case 'stylish':
            result = format_stylish(ast_tree)
            return '\n'.join(result)
        case 'plain':
            result = format_plain(ast_tree)
            return '\n'.join(result)
        case 'json':
            result = format_json(ast_tree)
            return result
