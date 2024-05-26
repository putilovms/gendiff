#!/usr/bin/env python3
import argparse
from gendiff.ast_generator import get_ast_tree
from gendiff.formatter import format_tree


def get_argument():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        default='stylish',
        help='set format of output'
    )
    return parser.parse_args()


def generate_diff(path1, path2, format='stylish'):
    tree = get_ast_tree(path1, path2)
    # print(json.dumps(tree, indent=4))
    result = format_tree(tree, format)
    return result


def main():
    args = get_argument()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
