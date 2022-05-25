def pl_sentence(sentence):
    output = []
    for i in sentence.split(' '):
        if i[0] in 'aeiou':
            output.append(f'{i}way')
        else:
            output.append(f'{i[1:]}{i[0]}ay')
    return ' '.join(output).lower()


print(pl_sentence("Lion are just big cats"))