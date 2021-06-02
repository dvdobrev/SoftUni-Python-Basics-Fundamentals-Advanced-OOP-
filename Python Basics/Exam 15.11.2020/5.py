baught_food = int(input()) * 1000
eated_food = input()

while eated_food != 'Adopted':
    eated_food = int(eated_food)
    baught_food -= eated_food
    eated_food = input()

if baught_food >= 0:
        print(f'Food is enough! Leftovers: {(baught_food)} grams.')
else:
        print(f'Food is not enough. You need {abs(baught_food)} grams more.')
