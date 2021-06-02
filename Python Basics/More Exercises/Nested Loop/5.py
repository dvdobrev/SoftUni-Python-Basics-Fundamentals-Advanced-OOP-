male = int(input())
female = int(input())
tables = int(input())
full = False
counter = 0


for m in range(1, male + 1):
    if full == True:
        break
    for f in range(1, female + 1):
        if counter == tables:
            full == True
            break
        else:
            print(f'({m} <-> {f})', end=' ')
            counter += 1

