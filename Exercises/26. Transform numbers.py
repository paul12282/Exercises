d = {'a': 1, 'b': 2, 'c': 3}


def transform_values(my_dict):
    e = {key: value * value for key, value in my_dict.items()}
    return e


print(transform_values(d))
