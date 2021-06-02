import math

videocard_price = int(input())
prehodnik = int(input())
elktricity_price_per_card_per_day = float(input())
earnd_money_per_card_per_day = float(input()) - elktricity_price_per_card_per_day
total_ernd_money_per_day = 13 * earnd_money_per_card_per_day



total_investition = 1000 + (13 * videocard_price) + (13 * prehodnik)
time_to_recover_investition = math.ceil(total_investition / total_ernd_money_per_day
)
print(total_investition)
print(time_to_recover_investition)