def my_sum(*number):  # * operator takes any number of arguments
    numbers_sum = 0
    for i in number:
        numbers_sum += i
    return numbers_sum


print(my_sum(33, 44, 51, 2))


def my_sum2(my_list, x):  # using a list as an argument
    list_sum = 0
    for i in my_list:
        list_sum += i
    main_sum = x + list_sum
    return main_sum


print(my_sum2([3, 3, 3, 3], 4))


def my_average(a_list):
    result_average = 0
    for j in a_list:
        result_average = (result_average + j)
    return result_average / len(a_list)


print(my_average([2, 6, 5, 4]))


def words_length(words):  # taking the smallest, highest and the average count of letters from a list
    words_average = 0
    smallest = min((word for word in words if word), key=len)
    highest = max((word for word in words if word), key=len)
    for k in words:
        words_average += len(k)
    return len(smallest), len(highest), words_average / len(words)


words_list = ["Ap", "Calda", "Este", "Foarte", "Buna"]
print(words_length(words_list))