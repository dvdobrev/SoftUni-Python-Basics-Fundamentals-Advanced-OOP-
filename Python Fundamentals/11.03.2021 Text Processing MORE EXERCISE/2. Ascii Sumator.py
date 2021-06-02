char1 = ord(input())
char2 = ord(input())
text = [ord(el) for el in input()]
num_sum = 0

for number in range(len(text)):
    if char1 < text[number] < char2:
        num_sum += text[number]

print(num_sum)

