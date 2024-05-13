import json
import itertools
import os
import yaml


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
    return {k: v for k, v in a.items()
            if (k not in b) or (k in b and b[k] != v)}


def format_value(v):
    return str(v).lower() if isinstance(v, bool) else v


def generate_diff(path1, path2):
    f1 = get_file(path1)
    f2 = get_file(path2)
    tab = {'equal': '    ', 'del': '  - ', 'add': '  + '}
    result = []
    diff1 = diff(f1, f2)
    diff2 = diff(f2, f1)
    for k, v in f1.items():
        match (k in diff1, k in diff2):
            case(True, False):
                result.append(f'{tab["del"]}{k}: {format_value(v)}')
            case(True, True):
                result.append(f'{tab["del"]}{k}: {format_value(v)}')
                result.append(f'{tab["add"]}{k}: {format_value(f2[k])}')
            case(False, False):
                result.append(f'{tab["equal"]}{k}: {format_value(v)}')
    for k, v in diff2.items():
        if k not in f1:
            result.append(f'{tab["add"]}{k}: {format_value(v)}')
    result = itertools.chain("{", result, "}")
    return '\n'.join(result)
