import json
import yaml


def parse(content, type):
    match type:
        case 'yml':
            return yaml.safe_load(content)
        case 'json':
            return json.loads(content)
