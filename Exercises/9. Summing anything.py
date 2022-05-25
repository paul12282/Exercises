def sum_everything(*items):
    if not items:
        return items
    output = items[0]
    for item in items[1:]:
        output += item
    return output


print(sum_everything('Lego', 'Nice'))




