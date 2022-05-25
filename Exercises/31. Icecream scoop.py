class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


def create_scoop():
    scoops = [Scoop('chocolate'), Scoop('vanilla'), Scoop('persimmon')]
    for scoop in scoops:
        print(scoop.flavor)


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
print(b)

class Beverage:
    def __init__(self, name, temperature):
        self.name = name
        self.temperature = temperature


beer = Beverage('beer', 3)
wine = Beverage('wine', 20)
whisky = Beverage('whisky', 22)

drinks = {
    beer.name: beer.temperature,
    wine.name: wine.temperature,
    whisky.name: whisky.temperature
}


def check_temperature(temp_list):
    if temp_list['beer'] in range(5):
        print(f'Beer temp is passing')


# check_temperature(drinks)