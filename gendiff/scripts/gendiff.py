#!/usr/bin/env python3
import argparse
from gendiff.scripts.diff_parser import generate_diff


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


def main():
    args = get_argument()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
