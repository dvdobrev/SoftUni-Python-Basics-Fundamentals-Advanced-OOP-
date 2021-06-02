aktor_name = input()
start_points = float(input())
juri_people = int(input())
total_points = start_points
over = False

for i in range(1, juri_people + 1):
    juri_name = input()
    juri_name_points = float(input())
    total_juri_name_points = (((len(juri_name)) * juri_name_points) / 2)
    total_points += total_juri_name_points
    if total_points > 1250.5:
        over = True
        print(f'Congratulations, {aktor_name} got a nominee for leading role with {total_points:.1f}!')
        break
if not over:
    print(f'Sorry, {aktor_name} you need {(1250.5 - total_points):.1f} more!')