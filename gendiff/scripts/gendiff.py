#!/usr/bin/env python3
import argparse
import json
import itertools


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output'
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()


def diff(a, b):
    return {k: v for k, v in a.items()
            if (k not in b) or (k in b and b[k] != v)}


def generate_diff(path1, path2):
    f1 = json.load(open(path1))
    f2 = json.load(open(path2))
    tab_equal = '    '
    tab_del = '  - '
    tab_add = '  + '
    result = []
    diff1 = diff(f1, f2)
    diff2 = diff(f2, f1)
    for k, v in f1.items():
        match (k in diff1, k in diff2):
            case(True, False):
                result.append(f'{tab_del}{k}: {v}')
            case(False, True):
                result.append(f'{tab_add}{k}: {v}')
            case(True, True):
                result.append(f'{tab_del}{k}: {v}')
                result.append(f'{tab_add}{k}: {f2[k]}')
            case(False, False):
                result.append(f'{tab_equal}{k}: {v}')
    for k, v in diff2.items():
        if k not in f1:
            result.append(f'{tab_add}{k}: {v}')
    result = itertools.chain("{", result, "}")
    return '\n'.join(result)
