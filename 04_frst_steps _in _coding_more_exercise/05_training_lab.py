# Using // operator
# От конзолата се четат 2 числа, по едно на ред: w (дължина в метри) и h (широчина в метри).
# Ограничения: 3 ≤ h ≤ w ≤ 100
# 2 работни места се губят от катедрата и едно от входната врата
# Едно работно място заема 70 на 120 cm (маса с размер 70 на 40 cm
# + място за стол и преминаване с размер 70 на 80 cm). Коридорът е широк поне 100 cm.
# Да се отпечата на конзолата едно цяло число: броят места в учебната зала.
w_lenght = float(input()) * 100
h_width = float(input()) * 100
usage_width = h_width - 100
number_desks = usage_width // 70
number_rows = w_lenght // 120
number_seats = number_rows * number_desks - 3

print(int(number_seats))

