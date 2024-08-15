# Напишете програма, която чете цяло число, въведено от потребителя,
# и отпечатва ден от седмицата (на английски език), в граници [1...7]
# или отпечатва "Error" в случай, че въведеното число е невалидно.
# Примерен вход и изход
# Вход	Изход
# 1	Monday
# 2	Tuesday
# 3	Wednesday
# 4	Thursday
# 5	Friday
# 6	Saturday
# 7	Sunday
# -1	Error
week_day = int(input())
if week_day == 1:
    print('Monday')
elif week_day == 2:
    print('Tuesday')
elif week_day == 3:
    print('Wednesday')
elif week_day == 4:
    print('Thursday')
elif week_day == 5:
    print('Friday')
elif week_day == 6:
    print('Saturday')
elif week_day == 7:
    print('Sunday')
else:
    print('Error')


