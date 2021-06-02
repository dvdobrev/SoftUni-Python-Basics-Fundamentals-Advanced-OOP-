data = input()

contests = {}

while not data == "end of contests":
    contest, password = data.split(":")
    contests[contest] = password

    data = input()

second_data = input()

user_data = {}

while not second_data == "end of submissions":
    contest, password, username, points = second_data.split("=>")
    points = int(points)
    if contest in contests:
        if contests[contest] == password:
            if username not in user_data:
                user_data[username] = {contest: points}
            else:
                if contest in user_data[username]:
                    if user_data[username][contest] < points:
                        user_data[username][contest] = points

                else:
                    user_data[username][contest] = points

    second_data = input()

total_points = 0
best_candidate = ""

for user, contests in user_data.items():
    current_points = 0
    for contest, points in contests.items():
        current_points += points

    if current_points > total_points:
        total_points = current_points
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {total_points} points.")
print("Ranking:")

sorted_users = dict(sorted(user_data.items()))

for user, contests in sorted_users.items():
    sorted_contests = dict(sorted(contests.items(), key=lambda kvp: -kvp[1]))
    print(user)
    for cont, point in sorted_contests.items():
        print(f"#  {cont} -> {point}")