from gendiff.normalizer import normalize_value
import gendiff.constants as const


TAB = {const.EQUAL: '  ', const.DEL: '- ',
       const.ADD: '+ ', const.UNFORM: '  '}


def get_deep_edit_node(k, v, type, ast_key):
    result = {}
    if isinstance(v[ast_key], dict):
        result[TAB[type] + k] = pre_stylish(v[ast_key])
    else:
        result[TAB[type] + k] = v[ast_key]
    return result


def get_deep_formated_node(k, v):
    result = {}
    if v['status'] == const.EDIT:
        result.update(get_deep_edit_node(k, v, const.DEL, 'value'))
        result.update(get_deep_edit_node(k, v, const.ADD, 'old'))
    else:
        result[TAB[v['status']] + k] = pre_stylish(v['value'])
    return result


def get_plain_formated_node(k, v):
    result = {}
    if v['status'] == const.EDIT:
        result[TAB[const.DEL] + k] = v['value']
        result[TAB[const.ADD] + k] = v['old']
    else:
        result[TAB[v['status']] + k] = v['value']
    return result


def get_not_formated_node(k, v):
    result = {}
    result[TAB[const.UNFORM] + k] = pre_stylish(
        v) if isinstance(v, dict) else v
    return result


def pre_stylish(tree):
    result = {}
    for k, v in tree.items():
        if isinstance(v, dict) and ('format' in v) \
                and (isinstance(v['value'], dict)
                     or isinstance(v.get('old'), dict)):
            result.update(get_deep_formated_node(k, v))
        elif isinstance(v, dict) and ('format' in v):
            result.update(get_plain_formated_node(k, v))
        else:
            result.update(get_not_formated_node(k, v))
    return result


def format_stylish(ast_tree):
    def walk(tree, acc, depth=0):
        R = '    '
        for k, v in tree.items():
            r = (R * (depth + 1))
            if isinstance(v, dict):
                acc.append(r[:-2] + k + ': {')
                walk(v, acc, depth + 1)
                acc.append(r + '}')
            else:
                acc.append(r[:-2] + k + ': ' + normalize_value(v))
    result = []
    result.append("{")
    walk(pre_stylish(ast_tree), result)
    result.append("}")
    return result
