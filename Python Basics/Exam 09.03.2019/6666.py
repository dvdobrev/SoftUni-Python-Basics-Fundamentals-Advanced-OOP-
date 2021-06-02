target = int(input())
start_high = target - 30
faild_jumps = 0
total_jumps = 0
jumped_high = int(input())
yes = True

while start_high <= target:

    if jumped_high > start_high:
        start_high += 5
        total_jumps += 1
        faild_jumps = 0
    else:
        faild_jumps += 1
        total_jumps += 1

    if faild_jumps == 3:
        yes = False
        print(f'Tihomir failed at {start_high}cm after {total_jumps} jumps.')
        break

    jumped_high = int(input())

    if jumped_high > target:
        total_jumps += 1
        print(f'Tihomir succeeded, he jumped over {start_high}cm after {total_jumps} jumps.')
        yes = False
        break

if yes:
    total_jumps += 1
    print(f'Tihomir succeeded, he jumped over {start_high}cm after {total_jumps} jumps.')