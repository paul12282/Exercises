import string

gematria_dict = {index: letter
                 for letter, index in enumerate(string.ascii_lowercase, 1)}

print(gematria_dict)