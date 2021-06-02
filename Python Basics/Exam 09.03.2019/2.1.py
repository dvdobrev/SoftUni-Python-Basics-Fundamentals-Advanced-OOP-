r1 = input()
r2 = input()
r3 = input()

won = 0
lost = 0
drawn = 0

if r1 == '0:0' or r1 == '1:1' or r1 == '2:2' or r1 == '3:3' or r1 == '4:4':
    drawn += 1
elif r1 == '1:0' or r1 == '2:0' or r1 == '2:1' or r1 == '3:0' or r1 == '3:1' or r1 == '3:2' or r1 == '4:0' or r1 == '4:1' or r1 == '4:2' or r1 == '4:3' or r1 == '5:0' or r1 == '5:1' or r1 == '5:2' or r1 == '5:3' or r1 == '5:4':
    won += 1
else:
    lost += 1

if r2 == '0:0' or r2 == '1:1' or r2 == '2:2' or r2 == '3:3' or r2 == '4:4':
    drawn += 1
elif r2 == '1:0' or r2 == '2:0' or r2 == '2:1' or r2 == '3:0' or r2 == '3:1' or r2 == '3:2' or r2 == '4:0' or r2 == '4:1' or r2 == '4:2' or r2 == '4:3' or r2 == '5:0' or r2 == '5:1' or r2 == '5:2' or r2 == '5:3' or r2 == '5:4':
    won += 1
else:
    lost += 1

if r3 == '0:0' or r3 == '1:1' or r3 == '2:2' or r3 == '3:3' or r3 == '4:4':
    drawn += 1
elif r3 == '1:0' or r3 == '2:0' or r3 == '2:1' or r3 == '3:0' or r3 == '3:1' or r3 == '3:2' or r3 == '4:0' or r3 == '4:1' or r3 == '4:2' or r3 == '4:3' or r3 == '5:0' or r3 == '5:1' or r3 == '5:2' or r3 == '5:3' or r3 == '5:4':
    won += 1
else:
    lost += 1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {drawn}')