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


def ast_tree(dict1, dict2):
    def walk(dict1, dict2, diff1, diff2):
        result = {}
        for k, v in dict1.items():
            match (k in diff1, k in diff2):
                case(True, False):
                    result[k] = {'status': const.DEL,
                                 'format': False, 'value': v}
                case(True, True):
                    if isinstance(v, dict) and isinstance(dict2[k], dict):
                        result[k] = {'status': const.EQUAL, 'format': True,
                                     'value': walk(dict1[k], dict2[k],
                                                   diff1[k], diff2[k])}
                    else:
                        result[k] = {'status': const.EDIT,
                                     'format': False, 'value': v, 'old': dict2[k]}
                case(False, False):
                    if isinstance(v, dict):
                        result[k] = {'status': const.EQUAL, 'format': True,
                                     'value': walk(dict1[k], dict2[k],
                                                   diff1[k], diff2[k])}
                    else:
                        result[k] = {'status': const.EQUAL,
                                     'format': False, 'value': v}
        for k, v in diff2.items():
            if k not in dict1:
                result[k] = {'status': const.ADD, 'format': False, 'value': v}
        return result
    diff1 = diff(dict1, dict2)
    diff2 = diff(dict2, dict1)
    return walk(dict1, dict2, diff1, diff2)


def sort_tree(tree):
    tree = dict(sorted(tree.items()))
    for v in tree.values():
        if isinstance(v, dict) and isinstance(v.get('value'), dict):
            v['value'] = sort_tree(v['value'])
    return tree


def get_ast_tree(dict1, dict2):
    result = ast_tree(dict1, dict2)
    result = sort_tree(result)
    return result
