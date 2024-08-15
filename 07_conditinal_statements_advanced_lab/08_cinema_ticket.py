# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя
# и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	12	14	14	12	16	16
day = input()
if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    price = 12
elif day == "Wednesday" or day == "Thursday":
    price = 14
else:
    price = 16
print(price)