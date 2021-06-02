exam_hour = int(input())  # цяло число от 0 до 23;
exam_minute = int(input())  # цяло число от 0 до 59.
arrival_hour = int(input())  # цяло число от 0 до 23;
arrival_minute = int(input())  # цяло число от 0 до 59.

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
diff = arrival_time - exam_time

hh = abs(diff) // 60
mm = abs(diff) % 60


if diff < -30:
    print('Early')
    if hh > 0:
        print(f"{hh}:{mm:02d} hours before the start")
    else:
        print(f'{mm} minutes before the start')

elif diff <= 0:
    print('On time')
    if not diff == 0:
        if hh > 0:
            print(f"{hh}:{mm:02d} hours before the start")
        else:
            print(f'{mm} minutes before the start')
else:
    print('Late')
    if hh > 0:
        print(f"{hh}:{mm:02d} hours after the start")
    else:
        print(f'{mm} minutes after the start')

