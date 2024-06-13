import os


def get_content(file_path):
    try:
        with open(file_path, 'r') as f:
            _, ext = os.path.splitext(file_path)
            content = f.read()
    except OSError:
        print(f"Could not open/read file: {file_path}")
    return (content, get_type(ext))


def get_type(ext):
    match ext:
        case '.yml' | '.yaml':
            return 'yml'
        case '.json':
            return 'json'
        case _:
            raise ValueError(f"This extension is not supported - {ext}")
