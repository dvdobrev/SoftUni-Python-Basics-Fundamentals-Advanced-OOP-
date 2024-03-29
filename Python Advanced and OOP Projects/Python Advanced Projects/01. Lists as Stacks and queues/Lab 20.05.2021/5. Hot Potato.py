from collections import deque

players = input().split()
step = int(input())

q = deque(players)
counter = 0

while len(q) > 1:
    counter += 1
    current_player = q.popleft()

    if not counter == step:
        q.append(current_player)
        
    else:
        print(f"Removed {current_player}")
        counter = 0

print(f"Last is {q.popleft()}")