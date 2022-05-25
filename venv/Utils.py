def find_max(list):
    high = list[0]
    for i in list:
        if i > high:
            high = i
    print(high)