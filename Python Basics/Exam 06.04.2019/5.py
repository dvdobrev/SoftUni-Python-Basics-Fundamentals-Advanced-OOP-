import sys

films_quantity = int(input())
best_film = ''
highest = -sys.maxsize
lowest = sys.maxsize
baddest_film = ''
total_raiting = 0

for i in range(1, films_quantity + 1):
    film_name = input()
    film_raiting = float(input())
    total_raiting += film_raiting
    if film_raiting > highest:
        highest = film_raiting
        best_film = film_name
    if film_raiting < lowest:
        lowest = film_raiting
        baddest_film = film_name

print(f'{best_film} is with highest rating: {highest:.1f}')
print(f'{baddest_film} is with lowest rating: {lowest:.1f}')
print(f'Average rating: {(total_raiting / films_quantity):.1f}')



