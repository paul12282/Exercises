def largest_word(files):
    with open(files, mode='r') as f:
        all_words = [word for word in f.read().split()]
        return sorted(all_words)[-1]


print(largest_word(r'C:\Users\Paul\PycharmProjects\Testing\Exercises\Lorem_ipsum.txt'))