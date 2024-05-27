import gendiff.constants as const


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
                result[k] = {'status': const.DEL, 'format': False, 'value': v}
            case(True, True):
                if isinstance(v, dict) and isinstance(f2[k], dict):
                    result[k] = {'status': const.EQUAL, 'format': True,
                                 'value': ast_tree(d1[k], d2[k], f1[k], f2[k])}
                else:
                    result[k] = {'status': const.EDIT,
                                 'format': False, 'value': v, 'old': f2[k]}
            case(False, False):
                if isinstance(v, dict):
                    result[k] = {'status': const.EQUAL, 'format': True,
                                 'value': ast_tree(d1[k], d2[k], f1[k], f2[k])}
                else:
                    result[k] = {'status': const.EQUAL,
                                 'format': False, 'value': v}
    for k, v in d2.items():
        if k not in f1:
            result[k] = {'status': const.ADD, 'format': False, 'value': v}
    return result


def sort_tree(tree):
    tree = dict(sorted(tree.items()))
    for v in tree.values():
        if isinstance(v, dict) and isinstance(v.get('value'), dict):
            v['value'] = sort_tree(v['value'])
    return tree


def get_ast_tree(dict1, dict2):
    diff1 = diff(dict1, dict2)
    diff2 = diff(dict2, dict1)
    result = ast_tree(diff1, diff2, dict1, dict2)
    result = sort_tree(result)
    return result
