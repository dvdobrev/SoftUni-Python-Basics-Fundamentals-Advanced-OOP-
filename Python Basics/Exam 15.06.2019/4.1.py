budget = float(input())

aktor_name = input()
aktor_name_length = 0


while aktor_name != 'ACTION':
    aktor_name_length = len(aktor_name)
    if aktor_name_length > 15:
        salery = budget * 0.2
    else:
        salery = float(input())
    budget -= salery
    if budget <= 0:
        break

    aktor_name = input()

if budget <= 0:
    print(f'We need {abs(budget):.2f} leva for our actors.')

else:
    print(f'We are left with {budget:.2f} leva.')
