import json
import itertools
import os
import yaml

TAB = {'equal': '  ', 'del': '- ', 'add': '+ ', 'unform': '  '}
R = '    '


def get_file(file_path):
    with open(file_path, 'r') as f:
        _, ext = os.path.splitext(file_path)
        match ext:
            case '.yml' | '.yaml':
                return yaml.load(f, Loader=yaml.FullLoader)
            case '.json':
                return json.load(f)
            case _:
                raise ValueError(f"This extension is not supported - {ext}")


def diff(a, b):
    result = {}
    for k, v in a.items():
        if isinstance(v, dict):
            result[k] = diff(v, b[k]) if k in b else v
        else:
            if (k not in b) or (k in b and b[k] != v):
                result[k] = v
    return result


def ast_tree(d1, d2, f1, f2):
    result = {}
    for k, v in f1.items():
        match (k in d1, k in d2):
            case(True, False):
                result[k] = [v, 'del', None]
            case(True, True):
                if isinstance(v, dict) and isinstance(f2[k], dict):
                    result[k] = [
                        ast_tree(d1[k], d2[k], f1[k], f2[k]), 'equal', None]
                else:
                    result[k] = [v, 'edit', f2[k]]
            case(False, False):
                if isinstance(v, dict):
                    result[k] = [
                        ast_tree(d1[k], d2[k], f1[k], f2[k]), 'equal', None]
                else:
                    result[k] = [v, 'equal', None]
    for k, v in d2.items():
        if k not in f1:
            result[k] = [v, 'add', None]
    return result


def get_ast_tree(path1, path2):
    file1 = get_file(path1)
    file2 = get_file(path2)
    diff1 = diff(file1, file2)
    diff2 = diff(file2, file1)
    result = ast_tree(diff1, diff2, file1, file2)
    result = sort_tree(result)
    return result


def sort_tree(tree):
    tree = dict(sorted(tree.items()))
    for k, v in tree.items():
        if isinstance(v, list) and isinstance(v[0], dict):
            tree[k][0] = sort_tree(v[0])
    return tree


def format_value(v):
    if isinstance(v, bool):
        result = str(v).lower()
    elif v is None:
        result = 'null'
    else:
        result = str(v)
    return result


def pre_stylish(tree):
    result = {}
    for k, v in tree.items():
        if isinstance(v, list) and \
                (isinstance(v[0], dict) or (isinstance(v[2], dict))):
            if v[1] == 'edit':
                result[TAB['del'] + k] = pre_stylish(
                    tree[k][0]) if isinstance(v[0], dict) else tree[k][0]
                result[TAB['add'] + k] = pre_stylish(
                    tree[k][2]) if isinstance(v[2], dict) else tree[k][2]
            else:
                result[TAB[v[1]] + k] = pre_stylish(tree[k][0])
        elif isinstance(v, list):
            if v[1] == 'edit':
                result[TAB['del'] + k] = tree[k][0]
                result[TAB['add'] + k] = tree[k][2]
            else:
                result[TAB[v[1]] + k] = tree[k][0]
        else:
            result[TAB['unform'] + k] = pre_stylish(
                tree[k]) if isinstance(v, dict) else tree[k]
    return result


def stylish(tree, acc, depth=0):
    for k, v in tree.items():
        r = (R * (depth + 1))
        if isinstance(v, dict):
            acc.append(r[:-2] + k + ': {')
            stylish(v, acc, depth + 1)
            acc.append(r + '}')
        else:
            acc.append(r[:-2] + k + ': ' + format_value(v))


def format_tree(ast_tree, format):
    result = []
    match format:
        case 'stylish':
            tree = pre_stylish(ast_tree)
            stylish(tree, result)
            result = itertools.chain("{", result, "}")
            result = '\n'.join(result)
    return result


def generate_diff(path1, path2, format='stylish'):
    tree = get_ast_tree(path1, path2)
    # print(json.dumps(tree, indent=4))
    result = format_tree(tree, format)
    return result
