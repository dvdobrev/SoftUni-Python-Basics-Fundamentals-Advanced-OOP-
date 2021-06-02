film_name = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
kino_percent = int(input())

profit = (days * tickets * ticket_price) - ((days * tickets * ticket_price) * (kino_percent / 100))

print(f'The profit from the movie {film_name} is {profit:.2f} lv.')