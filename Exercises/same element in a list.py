a_list = [1, 2, 3, 3, 5, 1, 11, 10, 22, 5]

seen = set()
dupes = []

for number in a_list:
    if number in seen:
        dupes.append(number)
    else:
        seen.add(number)

print(dupes)


def common_elements(seq: iter):
    return set(i for i in seq if seq.count(i) > 1)


print(common_elements(a_list))