numbers = [int(el) for el in input().split(", ")]

current_group = 10
current_list = []
current_num = ()

for each_group in range(len(numbers)):
    while len(numbers) > 0:
        index = 0
        current_num = numbers[index]
        for num in range(len(numbers)):
            if numbers[num] <= current_group:
                current_list.append(numbers[num])

        for remove in range(len(current_list)):
            numbers.remove(current_list[remove])
        print(f"Group of {current_group}'s: {current_list}")
        current_group += 10
        current_list = []

