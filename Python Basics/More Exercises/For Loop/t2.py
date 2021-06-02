import sys
n = int(input())
couples1 = 0
couples2 = 0
maxdiff = -sys.maxsize

for i in range(1,n + 1):
    if i % 2 != 0:
        number1 = int(input())
        number2 = int(input())
        couples1 = number1 + number2
    elif i % 2 == 0:
        number1 = int(input())
        number2 = int(input())
        couples2 = number1 + number2
    if couples1 > couples2:
        diff = couples1 - couples2
        if diff > maxdiff:
            maxdiff = diff
    else:
        diff = couples2 - couples1
        maxdiff = diff
    if couples2 != 0:
        if diff > maxdiff:
            maxdiff = diff
    elif couples2 == 0 and n == 1:
        couples2 = couples1
if couples1 == couples2:
    print(f'Yes, value={couples1}')
else:
    print(f'No, maxdiff={maxdiff}')
