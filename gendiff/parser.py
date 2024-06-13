import json
import yaml


def parse(content, type):
    data = ''
    match type:
        case 'yml':
            try:
                data = yaml.safe_load(content)
            except yaml.YAMLError as e:
                print("Invalid YAML syntax:", e)

        case 'json':
            try:
                data = json.loads(content)
            except json.JSONDecodeError as e:
                print("Invalid JSON syntax:", e)
    return data
