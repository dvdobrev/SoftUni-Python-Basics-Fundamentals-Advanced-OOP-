class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        while self.count > 0:
            number = self.number
            self.number += self.step
            self.count -= 1

            return number

        raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print()

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
