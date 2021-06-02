def loading_bar(num):
    loading_bar_count = []
    for n in range(10, num+1, 10):
        loading_bar_count.insert(0, "%")
    for n1 in range(num, 100, 10):
        loading_bar_count.append(".")
    ",".join(loading_bar_count)
    return loading_bar_count


number = int(input())
result = loading_bar(number)
result = "".join(result)
if number == 100:
    print(f"100% Complete!")
    print(f"[{result}]")
else:
    print(f"{number}%", end=" ")
    print(f"[{result}]")
    print("Still loading...")

print()