def read_next(*args):
    for row in args:
        for col in row:
            yield col


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
