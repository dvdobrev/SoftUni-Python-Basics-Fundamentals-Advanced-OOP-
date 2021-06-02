location_quantity = int(input())
total_gold = 0
average_gold = 0

for location in range(1, location_quantity +1):
    expekted_gold_per_day = float(input())
    days = int(input())
    total_gold_per_day = 0
    average_gold_per_day = 0
    for day in range(1, days + 1):
        earned_gold = float(input())
        total_gold_per_day += earned_gold

    average_gold_per_day = total_gold_per_day / days


    if average_gold_per_day >= expekted_gold_per_day:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        print(f'You need {(expekted_gold_per_day - average_gold_per_day):.2f} gold.')