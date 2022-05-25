d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
d3 = {'a': 1, 'b': 2, 'd': 4, 'e': 11}


def dictdiff(dict1, dict2):
    output_dict = {}
    all_keys = dict1.keys() | dict2.keys()
    for key in all_keys:
        if dict1.get(key) != dict2.get(key):
            output_dict[key] = [dict1.get(key), dict2.get(key)]
    return output_dict


# print(dictdiff(d1, d2))


def dict_merger(*dictionaries):
    for diction in dictionaries:
        diction.update(diction)
    return diction


print(dict_merger(d1, d2, d3))
