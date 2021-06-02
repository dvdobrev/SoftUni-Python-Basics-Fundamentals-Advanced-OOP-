import math

name = input()
season_quantity = int(input())
episode_quantity = int(input())
duration_non_com = float(input())
total_episode_duration = duration_non_com + (duration_non_com * 0.2)
season_time = ((total_episode_duration * episode_quantity) + 10)
total_season_time = season_time * season_quantity

print(f'Total time needed to watch the {name} series is {math.floor(total_season_time)} minutes.')
