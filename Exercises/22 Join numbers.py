def join_numbers(input_range):
    return ','.join(str(numbers)
                    for numbers in input_range)


# print(join_numbers(range(15)))


words = "10 abc 20 de44 30 55fg 40"


def sum_numbers(numbers):
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())


print(sum_numbers('1 2 3 a b c 4'))
