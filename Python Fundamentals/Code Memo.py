happines = [int(el) for el in input().split()]
factor = int(input())
multiplied_hapinnes_by_factor = [num * factor for num in happines]
# multiplied_hapinnes_by_factor = list(map(lambda num: num*factor, happines))
avg_happines = sum(multiplied_hapinnes_by_factor) / len(multiplied_hapinnes_by_factor)

happy_employees = [h for h in multiplied_hapinnes_by_factor if h > avg_happines]

# happy_employees = []
# for h in multiplied_hapinnes_by_factor:
#     if h >=avg_happines:
#         happy_employees.append(h)


items = [a b c]
print(*items) →→→ a b c
print(*itesm, sep=",") →→→ a,b,c