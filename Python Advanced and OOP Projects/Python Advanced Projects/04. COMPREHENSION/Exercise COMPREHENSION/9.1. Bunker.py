categories = {category: [] for category in input().split(", ")}
n = int(input())
quantity = 0
quality = 0

for _ in range(n):
    data = input().split(" - ")
    categories[data[0]].append(data[1])

    info_data = data[2].split(";")
    quantity += int(info_data[0].split(":")[1])
    quality += int(info_data[1].split(":")[1])
    
print(f"Count of items: {quantity}")
print(f"Average quality: {quality / len(categories):.2f}")
[print(f"{category} -> {', '.join(items)}") for category, items in categories.items()]