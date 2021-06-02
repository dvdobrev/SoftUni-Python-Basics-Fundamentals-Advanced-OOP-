houers = 0
minutes = -1
sekunds = -1

while 0 <= houers < 24:
    houers = houers
    minutes = minutes
    if houers <= 23 and minutes <= 58 and sekunds <= 58:
        if minutes <= 58 and sekunds <= 58:
            sekunds += 1
        elif minutes < 58 and sekunds == 59:
            minutes += 1
            sekunds = 0
        elif minutes == 59 and sekunds == 59:
            houers += 1
            minutes = 0
            sekunds = 0


        print(f'{houers} : {minutes}')
    elif houers < 23 and minutes == 59:
        houers += 1
        minutes = 0
        print(f'{houers} : {minutes}')
    elif houers == 23 and minutes <= 58:
        minutes += 1
        print(f'{houers} : {minutes}')
   # elif houers == 23 and minutes == 59:
        #print(f'{houers} : {minutes}')
    else:
        break