days = int(input())
room_type = input()  # room for one person", "apartment" или "president apartment";
evaluation = input()  # positive"  или "negative".

night = days - 1
room = 18.00
apartment = 25.00
president_apartment = 35.00
price = 0

if days < 10:
    if room_type == 'room for one person':
        price = room * night
    elif room_type == 'apartment':
        price = apartment * night - apartment * night * 0.3
    elif room_type == 'president apartment':
        price = president_apartment * night - president_apartment * night * 0.1

elif 10 <= days <= 15:
    if room_type == 'room for one person':
        price = room * night
    elif room_type == 'apartment':
        price = apartment * night - apartment * night* 0.35
    elif room_type == 'president apartment':
        price = president_apartment * night - president_apartment * night * 0.15

elif days > 15:
    if room_type == 'room for one person':
        price = room * night
    elif room_type == 'apartment':
        price = apartment * night - apartment * night* 0.5
    elif room_type == 'president apartment':
        price = president_apartment * night - president_apartment * night * 0.2

if evaluation == 'positive':
    price += price * 0.25
elif evaluation == 'negative':
    price -= price * 0.1

print(f'{price:.2f}')