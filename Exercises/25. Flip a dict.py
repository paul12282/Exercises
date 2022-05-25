d = {'a': 1, 'b': 2, 'c': 3}


def flip_dict(my_dictionary):
    output = {value: key
              for key, value in my_dictionary.items()}
    return output


print(flip_dict(d))
