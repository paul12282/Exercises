vocals = "aeiou"


def ubbi_dubbi(word):
    output = [i for i in word]
    for i, j in enumerate(output):
        if j.lower() in vocals:
            output[i] = f'ub{j}'

    return ''.join(output)


print(ubbi_dubbi("BArrow"))

def author_names(article: str, authors: list):
    for author in authors:
        if author in article:
            article = article.replace(author, '_')
    return article


print(author_names('Ion Creanga era un dobitoc', ['Ion', 'Creanga']))
