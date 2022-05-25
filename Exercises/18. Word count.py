def wordcount(file):
    counts = {'characters': 0, 'words': 0, 'lines': 0}
    unique_words = set()
    with open(file, 'r') as f:
        for one_line in f:
            counts['lines'] += 1
            counts['characters'] += len(one_line)
            counts['words'] += len(one_line.split())
            unique_words.update(one_line.split())
        counts['unique_words'] = len(unique_words)
        for key, value in counts.items():
            print(f'{key}: {value}')


wordcount(r'C:\Users\Paul\Desktop\wcfile.txt')