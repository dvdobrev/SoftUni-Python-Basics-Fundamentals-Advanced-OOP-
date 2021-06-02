text = input().split()
first_string = text[0]
second_string = text[1]
short_string = ""
longer_string = ""
total_sum = 0

if not len(first_string) == len(second_string):
    short_string = min(text, key=len)
    longer_string = max(text, key=len)
else:
    short_string = text[0]
    longer_string = text[1]


if first_string.isalpha():
    if not len(first_string) == len(second_string):
        for dif in range(-len(short_string), -len(longer_string), - 1):
            total_sum += ord(longer_string[dif])
    for char in range(len(short_string)):
       total_sum += ord(short_string[char]) * ord(longer_string[char])

else:
    if not len(first_string) == len(second_string):
        total_sum += longer_string[-1]
    for digit in range(len(short_string)):
        total_sum += int(short_string[digit]) * int(longer_string[digit])

print(total_sum)




