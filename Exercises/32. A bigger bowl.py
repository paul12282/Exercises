class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor


class Bowl:
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)


class BigBowl(Bowl):
    max_scoops = 5


s1 = Scoop('choco')
s2 = Scoop('cherry')
s3 = Scoop('berry')
s4 = Scoop('vanilla')
s5 = Scoop('mango')

buy = BigBowl()
buy.add_scoops(s1, s2, s3)
buy.add_scoops(s4, s5)
print(buy)