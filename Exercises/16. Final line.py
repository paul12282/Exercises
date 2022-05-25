def get_final_line(file):
    with open(file, mode='r') as f:
        last_line = ''
        for current_line in f:
            last_line = current_line
        print(last_line)


# get_final_line(r'C:\Users\Paul\PycharmProjects\Testing\Exercises\Lorem_ipsum.txt')

def get_sum_of_ints(file):
    with open(file, mode='r') as f:
        result = []
        int_sum = 0
        for line in f:
            for words in line.split(' '):
                if words.isdigit():
                    result.append(words)
        for element in result:
            int_sum += int(element)
        return int_sum


print(get_sum_of_ints(r'C:\Users\Paul\PycharmProjects\Testing\Exercises\Lorem_ipsum.txt'))
