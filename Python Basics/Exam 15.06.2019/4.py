seats_quantity = int(input())
entering_people = input()
tickets_price = 0
entered_people = 0

full = False

while entering_people != 'Movie time!':
    entering_people = int(entering_people)
    entered_people += entering_people

    if seats_quantity < entered_people:
        full = True
        print('The cinema is full.')
        break
    if seats_quantity == entered_people:
        #full = True
        tickets_price += 5 * entering_people
        print('The cinema is full.')
        break

    tickets_price += 5 * entering_people

    if entering_people % 3 == 0:
        tickets_price -= 5

    entering_people = input()

if not full:
    print(f'There are {seats_quantity - entered_people} seats left in the cinema.')

print(f'Cinema income - {tickets_price} lv.')
