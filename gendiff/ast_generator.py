from gendiff.parser import parse
from gendiff.loader import get_content


def diff(a, b):
    result = {}
    for k, v in a.items():
        if isinstance(v, dict):
            if (k in b) and isinstance(b[k], dict):
                result[k] = diff(v, b[k])
            else:
                result[k] = v
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
    file1 = parse(*get_content(path1))
    file2 = parse(*get_content(path2))
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
