price_ratings = [int(el) for el in input().split()] # 1 5 1
entry_index = int(input())  # 1
item_type = input()

left_list = []
right_list = []

if item_type == "cheap":
    for left in range(0, entry_index):
        if price_ratings[left] < price_ratings[entry_index]:
            left_list.append(price_ratings[left])

    for right in range(entry_index + 1, len(price_ratings)):
        if price_ratings[right] < price_ratings[entry_index]:
            right_list.append(price_ratings[right])


else:
    for left in range(0, entry_index):
        if price_ratings[left] >= price_ratings[entry_index]:
            left_list.append(price_ratings[left])

    for right in range(entry_index + 1, len(price_ratings)):
        if price_ratings[right] >= price_ratings[entry_index]:
            right_list.append(price_ratings[right])

damage_left = sum(left_list)
damage_rigth = sum(right_list)

if damage_left >= damage_rigth:
    print(f"Left - {damage_left}")
else:
    print(f"Right - {damage_rigth}")

