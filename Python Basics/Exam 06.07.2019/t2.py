word = 'Dobri'
big = False

for l in word:
    if big == False:
        if word[0] == 'D':
            big = True
            print('yes')
    else:
        print('no')