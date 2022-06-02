number_of_adults = 0
number_of_kids = 0
money_for_toys = 0
money_for_sweaters = 0
age_of = input()
while age_of != "Christmas":
    i = int(age_of)

    if i <= 16:
        number_of_kids += 1
        money_for_toys += 5
    elif i > 16:
        number_of_adults += 1
        money_for_sweaters += 15

    else:
        break
    age_of = input()

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")