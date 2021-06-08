try:

    with open("test.txt") as file:
        print("File found!")
        print(file.readlines())


except FileNotFoundError:
    print("File NOT found")