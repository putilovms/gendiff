from gendiff.normalizer import normalize_value
import gendiff.constants as const


def pre_plain(ast_tree):
    def walk(tree, acc, path=''):
        for k, v in tree.items():
            p = (path + '.' + k).strip('.')
            if isinstance(v, dict):
                if v['format']:
                    acc[p] = v
                    walk(v['value'], acc, p)
                else:
                    acc[p] = v
    result = {}
    walk(ast_tree, result)
    return result


def format_plain(ast_tree):
    tree = pre_plain(ast_tree)
    result = []
    for k, v in tree.items():
        match v['status']:
            case const.DEL:
                result.append(f"Property '{k}' was removed")
            case const.ADD:
                s = '[complex value]' if isinstance(
                    v['value'], dict) else normalize_value(v['value'], True)
                result.append(f"Property '{k}' was added with value: {s}")
            case const.EDIT:
                s1 = '[complex value]' if isinstance(
                    v['value'], dict) else normalize_value(v['value'], True)
                s2 = '[complex value]' if isinstance(
                    v['old'], dict) else normalize_value(v['old'], True)
                result.append(f"Property '{k}' was updated. From {s1} to {s2}")
    return result
