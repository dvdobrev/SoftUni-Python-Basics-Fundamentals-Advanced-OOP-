class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.number_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number_counter == self.number:
            raise StopIteration

        if self.counter == len(self.sequence):
            self.counter = 0

        current_char = self.sequence[self.counter]
        self.counter += 1
        self.number_counter += 1

        return current_char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
