contest_data = input()
contest_dict = {}
while not contest_data == "end of contests":
    contest_name, password_for_contest = contest_data.split(":")
    contest_dict[contest_name] = password_for_contest
    contest_data = input()
contest_submissions = input()
while not contest_submissions == "end of submissions":
    contest, password, username, points = contest_submissions.split("=>")
    username_points = {}
    contest_and_user = {}
    contest_and_user[contest] = {}

    if contest in contest_dict:
        contest_passowrd_check = {}
        contest_passowrd_check[contest] = password

        for key, value in contest_dict.items():
            curent_dict = {}
            curent_dict[key] = value
            if contest_passowrd_check == curent_dict:
                if contest in contest_and_user:
                    current_poinst =
                    if points >
                    contest_and_user[contest][username] = points
                    print(contest_and_user)


                if username not in username_points:
                    username_points[username] = points
                else:
                    username_points[username] += points





    contest_submissions = input()

