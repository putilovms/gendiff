import gendiff.constants as const
import copy


def deep_merge(dict1, dict2):
    for key in dict2:
        if key in dict1:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                deep_merge(dict1[key], dict2[key])
            elif dict1[key] != dict2[key]:
                dict1[key] = [dict1[key], dict2[key]]
        else:
            dict1[key] = dict2[key]
    return dict1


def set_del_node(tree, delete, merge_dict):
    for k in delete:
        tree[k] = {'status': const.DEL,
                   'format': False, 'value': merge_dict[k]}


def set_add_node(tree, add, merge_dict):
    for k in add:
        tree[k] = {'status': const.ADD,
                   'format': False, 'value': merge_dict[k]}


def set_edit_node(tree, edit, merge_dict):
    for k in edit:
        if isinstance(merge_dict[k], list):
            tree[k] = {'status': const.EDIT, 'format': False,
                       'value': merge_dict[k][0], 'old': merge_dict[k][1]}


def set_equal_node(tree, equal, merge_dict, dict1, dict2):
    for k in equal:
        if isinstance(merge_dict[k], dict):
            tree[k] = {'status': const.EQUAL, 'format': True,
                       'value': ast_tree(merge_dict[k], dict1[k], dict2[k])}
        elif not isinstance(merge_dict[k], list):
            tree[k] = {'status': const.EQUAL,
                       'format': False, 'value': merge_dict[k]}


def ast_tree(merge_dict, dict1, dict2):
    result = {}
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    delete = keys1 - keys2
    set_del_node(result, delete, merge_dict)
    add = keys2 - keys1
    set_add_node(result, add, merge_dict)
    equal = keys1 & keys2
    set_edit_node(result, equal, merge_dict)
    set_equal_node(result, equal, merge_dict, dict1, dict2)
    return result


def sort_tree(tree):
    tree = dict(sorted(tree.items()))
    for v in tree.values():
        if isinstance(v, dict) and isinstance(v.get('value'), dict):
            v['value'] = sort_tree(v['value'])
    return tree


def get_ast_tree(dict1, dict2):
    merge_dict = copy.deepcopy(dict1)
    deep_merge(merge_dict, dict2)
    result = ast_tree(merge_dict, dict1, dict2)
    result = sort_tree(result)
    return result
