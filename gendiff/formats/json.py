import json


def format_json(ast_tree):
    result = json.dumps(ast_tree, indent=4)
    return result
