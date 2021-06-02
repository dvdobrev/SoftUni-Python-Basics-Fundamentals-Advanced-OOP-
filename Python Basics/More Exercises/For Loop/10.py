houers = 0
minutes = 0
sekunds = -1

while 0 <= houers < 24:
    houers = houers
    minutes = minutes
    sekunds = sekunds
    if houers <= 22:
        if minutes < 59:
            if sekunds < 59:
                sekunds += 1
                print(f'{houers} : {minutes} : {sekunds} ')
            elif sekunds == 59:
                minutes += 1
                sekunds = 0
                print(f'{houers} : {minutes} : {sekunds} ')
        elif minutes == 59:
            if sekunds < 59:
                sekunds += 1
                print(f'{houers} : {minutes} : {sekunds} ')
            elif sekunds == 59:
                houers += 1
                minutes = 0
                sekunds = 0
                print(f'{houers} : {minutes} : {sekunds} ')
    elif houers == 23:
        if minutes < 59:
            if sekunds < 59:
                sekunds += 1
                print(f'{houers} : {minutes} : {sekunds} ')
            elif sekunds == 59:
                minutes += 1
                sekunds = 0
                print(f'{houers} : {minutes} : {sekunds} ')
        elif minutes == 59:
            if sekunds < 59:
                sekunds += 1
                print(f'{houers} : {minutes} : {sekunds} ')
            elif sekunds == 59:
                break