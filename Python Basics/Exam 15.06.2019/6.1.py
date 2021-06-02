import sys

film_name = input()
small_letter = 0
big_letter = 0
film_length = 0
counter = 0
max_score = -sys.maxsize
best_film = ''

while film_name != 'STOP':
    score = 0
    film_length = len(film_name)
    for i in film_name:
        i = ord(i)
        if 97 <= i <= 122:
            score += i - (2 * film_length)
        elif 65 <= i <= 90:
            score += i - film_length
        else:
            score += i
        if score > max_score:
            max_score = score
            best_film = film_name

    counter += 1
    if counter == 7:
        break
    film_name = input()

if counter == 7:
    print('The limit is reached.')
    print(f'The best movie for you is {best_film} with {max_score} ASCII sum.')
if film_name == 'STOP':
    print(f'The best movie for you is {best_film} with {max_score} ASCII sum.')
