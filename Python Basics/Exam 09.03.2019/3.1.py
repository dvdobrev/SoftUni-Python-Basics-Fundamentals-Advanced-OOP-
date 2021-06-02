country = input()
toy = input()
score =0

if country == 'Russia':
    if toy == 'ribbon':
        score = 9.1 + 9.4
    elif toy == 'hoop':
        score = 9.3 + 9.8
    elif toy == 'rope':
        score = 9.6 + 9
elif country == 'Bulgaria':
    if toy == 'ribbon':
        score = 9.6 + 9.4
    elif toy == 'hoop':
        score = 9.55 + 9.75
    elif toy == 'rope':
        score = 9.5 + 9.4
elif country == 'Italy':
    if toy == 'ribbon':
        score = 9.2 + 9.5
    elif toy == 'hoop':
        score = 9.45 + 9.35
    elif toy == 'rope':
        score = 9.7 + 9.15

percent = 100 - ((score / 20) * 100)

print(f'The team of {country} get {score:.3f} on {toy}.')
print(f'{percent:.2f}%')