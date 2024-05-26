import json


def format_json(tree):
    result = json.dumps(tree, indent=4)
    return result
