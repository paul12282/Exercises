import string

GEMATRIA = {index: letter
            for letter, index in enumerate(string.ascii_lowercase, 1)}


def gematria_for(word):
    return sum(GEMATRIA.get(one_letter, 0)
               for one_letter in word)


def gematria_equal_words(input_word):
    our_score = gematria_for(input_word.lower())
    return [one_word.strip()
            for one_word in
            open('/usr/share/dict/words')
            if gematria_for(one_word.lower()) ==
            our_score]


print(gematria_for('cat'))
