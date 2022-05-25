numbers = [1, 2, 3, 1, 2, 3, 4, 1]


def how_many_different_numbers(numbers):  # returns only the unique elements from the list
    unique_numbers = set(numbers)
    return len(unique_numbers)


print(how_many_different_numbers(numbers))
