def first_last(sequence):  # using slicing not indexing to keep the original sequence type
    return sequence[:1] + sequence[-1:]


print(first_last([1, 2, 3, 22]))


def largest_element(sequence):
    output = 0
    for element in sequence:
        if int(element) > 0:
            output = element
        return output


print(largest_element("3004"))


def odd_even_sum(my_list):
    output_even = 0
    output_odd = 0
    for i, element in enumerate(my_list):
        if (i % 2) == 0:
            output_even += element
        else:
            output_odd += element
    return [output_even, output_odd]


print(odd_even_sum([10, 20, 30, 40, 50, 60]))


def plus_minus():
    pass
