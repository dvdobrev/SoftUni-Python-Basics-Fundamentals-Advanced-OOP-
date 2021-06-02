money = input().split(", ")
number_of_beggars = int(input())
money_each_beggar = []
beggar = 0

for b in range(1, number_of_beggars +1):
    current_sum = 0
    for cash in range(beggar, len(money), number_of_beggars):
        current_sum += int(money[cash])
    money_each_beggar.append(current_sum)
    beggar += 1
print(money_each_beggar)



