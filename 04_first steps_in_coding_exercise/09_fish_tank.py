lenght_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent_of_volume_full_dm3 = float(input())
volume_cm3 = lenght_cm * width_cm * height_cm
volume_dm3 = volume_cm3 * 0.001
free_volume_tank_dm3 = volume_dm3 * (100 - percent_of_volume_full_dm3)/100
print(free_volume_tank_dm3)
