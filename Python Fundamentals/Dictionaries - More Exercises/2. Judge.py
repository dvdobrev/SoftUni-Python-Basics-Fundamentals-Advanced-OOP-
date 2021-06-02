data = input()

results = {}
total_points = {}

while not data == "no more time":
    user, contest, points = data.split(" -> ")
    points = int(points)
    if contest not in results:
        results[contest] = {}

    if user not in results[contest]:
        results[contest][user] = points
    else:
        if results[contest][user] < points:
            results[contest][user] = points
            total_points[user] = points
            data = input()
            continue
        else:
            data = input()
            continue

    if user not in total_points:
        total_points[user] = points
    else:
        total_points[user] += points

    data = input()

for contests, users in results.items():
    print(f"{contests}: {len(users)} participants")
    sorted_users = dict(sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    position = 1
    for each_user, each_points in sorted_users.items():
        print(f"{position}. {each_user} <::> {each_points}")
        position += 1

print(f"Individual standings:")

sorted_total_points = dict(sorted(total_points.items(), key=lambda kvp: (-kvp[1], kvp[0])))
position = 1
for user, points in sorted_total_points.items():
    print(f"{position}. {user} -> {points}")
    position += 1