class Average():
    def __init__(self):
        self.output = []

    def calc_average(self, *numbers):
        for number in numbers:
            self.output.append(number)
        return sum(self.output) // len(self.output)


some_math = Average()
print(some_math.calc_average(1, 2, 3, 44, 31))
