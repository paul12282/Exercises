def get_sv(file):
    with open(file, 'r') as f:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        output = [word for word in f.read().split() if vowels < set(word)]
        return output


print(get_sv(r'C:\Users\Paul\PycharmProjects\Testing\Exercises\Lorem_ipsum.txt'))
