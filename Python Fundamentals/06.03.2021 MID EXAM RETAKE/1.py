journey_cost = float(input())
months_to_collect = int(input())
saved_money = 0


for month in range(1, months_to_collect + 1):
    if not month  == 1 and not month % 2 == 0:
        saved_money -= saved_money * 0.16
    if month % 4 == 0:
        saved_money += saved_money * 0.25
    saved_money += journey_cost * 0.25

diff = abs(saved_money - journey_cost)
if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {diff:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {diff:.2f}lv. more.")