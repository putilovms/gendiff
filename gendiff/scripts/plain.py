from gendiff.scripts.formatter import format_value


def pre_plain(ast_tree):
    def walk(tree, acc, path=''):
        for k, v in tree.items():
            p = (path + '.' + k).strip('.')
            if isinstance(v, list):
                if isinstance(v[0], dict):
                    acc[p] = v
                    walk(tree[k][0], acc, p)
                else:
                    acc[p] = v
    result = {}
    walk(ast_tree, result)
    return result


def plain(ast_tree):
    tree = pre_plain(ast_tree)
    result = []
    for k, v in tree.items():
        match v[1]:
            case 'del':
                result.append(f"Property '{k}' was removed")
            case 'add':
                s = '[complex value]' if isinstance(
                    v[0], dict) else format_value(v[0], True)
                result.append(f"Property '{k}' was added with value: {s}")
            case 'edit':
                s1 = '[complex value]' if isinstance(
                    v[0], dict) else format_value(v[0], True)
                s2 = '[complex value]' if isinstance(
                    v[2], dict) else format_value(v[2], True)
                result.append(f"Property '{k}' was updated. From {s1} to {s2}")
    # print(json.dumps(result, indent=4))
    return result
