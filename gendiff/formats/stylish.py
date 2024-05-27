from gendiff.normalizer import normalize_value
import gendiff.constants as const


def pre_stylish(tree):
    TAB = {const.EQUAL: '  ', const.DEL: '- ',
           const.ADD: '+ ', const.UNFORM: '  '}
    result = {}

    for k, v in tree.items():
        if isinstance(v, dict) and ('format' in v) \
                and (isinstance(v['value'], dict)
                     or isinstance(v.get('old'), dict)):
            if v['status'] == const.EDIT:
                result[TAB[const.DEL] + k] = pre_stylish(
                    v['value']) if isinstance(v['value'], dict) else v['value']
                result[TAB[const.ADD] + k] = pre_stylish(
                    v['old']) if isinstance(v['old'], dict) else v['old']
            else:
                result[TAB[v['status']] + k] = pre_stylish(v['value'])
        elif isinstance(v, dict) and ('format' in v):
            if v['status'] == const.EDIT:
                result[TAB[const.DEL] + k] = v['value']
                result[TAB[const.ADD] + k] = v['old']
            else:
                result[TAB[v['status']] + k] = v['value']
        else:
            result[TAB[const.UNFORM] + k] = pre_stylish(
                v) if isinstance(v, dict) else v
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
