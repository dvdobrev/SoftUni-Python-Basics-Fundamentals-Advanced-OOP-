visitors = int(input())
back = 0
Chest = 0
Legs = 0
Abs = 0
Protein_shake = 0
Protein_bar = 0

for i in range(1, visitors + 1):
    doing = input()
    if doing == 'Back':
        back += 1
    elif doing == 'Chest':
        Chest += 1
    elif doing == 'Legs':
        Legs += 1
    elif doing == 'Abs':
        Abs += 1
    elif doing == 'Protein shake':
        Protein_shake += 1
    elif doing == 'Protein bar':
        Protein_bar += 1

training = ((back + Chest + Legs + Abs) / visitors) * 100
drinking = ((Protein_bar + Protein_shake) / visitors) * 100

print(f'{back} - back')
print(f'{Chest} - chest')
print(f'{Legs} - legs')
print(f'{Abs} - abs')
print(f'{Protein_shake} - protein shake')
print(f'{Protein_bar} - protein bar')
print(f'{training:.2f}% - work out')
print(f'{drinking:.2f}% - protein')