width = int(input())
lentgh = int (input())
number_pieces = width * lentgh
left_pieces = number_pieces
command = input()

while command != 'STOP':
    pieces = int(command)
    left_pieces -= pieces
    if left_pieces <= 0:
            print(f'No more cake left! You need {abs(left_pieces)} pieces more.')
            break
    command = input()
else:
    print(f'{left_pieces} pieces are left.')