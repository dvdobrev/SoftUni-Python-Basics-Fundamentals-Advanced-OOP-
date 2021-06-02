money_needed = int(input())
command = input()
earned_money = 0
people = 1
card_payed = 0
card_people = 0
cahs_payed = 0
cash_people = 0
faild = True

while command != 'End':
    money = int(command)
    if people % 2 == 0:
        if money > 10:
            card_payed += money
            earned_money += money
            card_people += 1
            print('Product sold!')
        else:
            print('Error in transaction!')
    else:
        if money > 100:
            print('Error in transaction!')
        else:
            cahs_payed += money
            earned_money += money
            cash_people += 1
            print('Product sold!')

    if earned_money >= money_needed:
        faild = False
        print(f'Average CS: {(cahs_payed / cash_people):.2f}')
        print(f'Average CC: {(card_payed / card_people):.2f}')
        break
    else:
        people += 1
        command = input()
if faild == True:
    print('Failed to collect required money for charity.')






