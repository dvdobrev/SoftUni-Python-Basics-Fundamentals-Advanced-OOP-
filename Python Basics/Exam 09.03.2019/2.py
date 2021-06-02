min_kontrol = int(input())
sek_kontrol = int(input())
length = float(input())
sek_per_100_meter = int(input())

kontrol_time = (min_kontrol * 60) + sek_kontrol
reduction_sek = (length / 120) * 2.5
player_time = ((length / 100) * sek_per_100_meter) - reduction_sek

if player_time <= kontrol_time:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {player_time:.3f}.')
else:
    print(f'No, Marin failed! He was {abs(kontrol_time - player_time):.3f} second slower.')