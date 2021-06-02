def print_result(result):
    for k, v in result.items():
        print(f"{k} -> {v}")

country = input().split(", ")
capital = input().split(", ")

result = {country[index]: capital[index] for index in range(len(country))}
print_result(result)

# for k, v in result.items():
#     print(f"{k} -> {v}")