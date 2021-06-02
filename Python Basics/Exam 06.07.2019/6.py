import sys
import math
word = input()
best_word = ''
best_score = - sys.maxsize
big_letter = False

while word != 'End of words':
    score = 0
    for l in word:

        if big_letter == False:
            if l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U' or l == 'Y':
                big_letter = True
        l = ord(l)
        score += l

    if big_letter == True:
        score = score * len(word)
        if score > best_score:
            best_score = score
            best_word = word
    else:
        score = math.floor(score / len(word))
        if score > best_score:
            best_score = score
            best_word = word

    word = input()

print(f'The most powerful word is {best_word} - {best_score}')