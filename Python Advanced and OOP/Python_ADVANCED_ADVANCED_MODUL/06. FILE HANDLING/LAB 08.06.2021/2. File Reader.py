with open("nums.txt") as file:
    print(sum([int(el[:-1]) for el in file.readlines()]))

    #print(sum([int(el.strip("\n")) for el in file.readlines()]))