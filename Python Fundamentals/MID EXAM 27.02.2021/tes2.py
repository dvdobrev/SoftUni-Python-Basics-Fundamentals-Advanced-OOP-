price_ratings = input().split()
entry_index = int(input())
item_type = input()

left_list = []
right_list = []

if item_type == "cheap":
    for left in range(0, entry_index):
        if left < entry_index:
            left_list.append()

    for rigtht in range(entry_index, len(price_ratings) + 1):
        if rigtht < entry_index:
            right_list.append(rigtht)


else:
    for left in range(1, entry_index):
        if left >= entry_index:
            left_list.append(left)

    for rigtht in range(entry_index, len(price_ratings) + 1):
        if rigtht >= entry_index:
            right_list.append(rigtht)

damage_left = sum(left_list)
damage_rigth = sum(right_list)

if damage_left >= damage_rigth:
    print(f"Left - {damage_left}")
else:
    print(f"Right - {damage_rigth}")

