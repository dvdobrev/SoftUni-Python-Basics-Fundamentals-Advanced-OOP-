class countdown_iterator:
    def __init__(self, count):
        self.count = count
        # self.current_count =

    def __iter__(self):
        return self

    def __next__(self):
        current_count = self.count
        self.count -= 1

        if self.count == -2:
            raise StopIteration

        return current_count


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
