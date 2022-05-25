my_list = [[1, 2], [3, 4]]

def flatten(a_list):
    output = [elements
              for element in a_list
              for elements in element]
    return output


print(flatten(my_list))