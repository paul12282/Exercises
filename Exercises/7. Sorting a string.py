def strsort(word: str) -> str:
    return ''.join(sorted(word))


print(strsort('cat'))


def strsort_words(words: str) -> str:
    return ', '.join(sorted(words.split(' ')))


print(strsort_words("Tom Dick Harry") == 'Dick, Harry, Tom')
print(strsort_words("Tom Dick Harry"))

def strsort_file(file):
    with open(file, mode='r') as f:
        for element in f.readlines():
            print(sorted(element.split(' ')))






print(strsort_file(r'C:\Users\Paul\PycharmProjects\Testing\Exercises\Lorem_ipsum.txt'))