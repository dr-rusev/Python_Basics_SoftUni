# Напишете програма, която чете от конзолата число r и пресмята и отпечатва
# лицето и периметъра на кръг / окръжност с радиус r, като форматирате
# изхода в следния вид: "<calculated area>" "<calculated parameter>".
# Форматирайте изходните данни до втория знак след десетичната запетая.

from math import pi

radius = float(input())

calculated_area = pi * radius ** 2
calculated_perimeter = 2 * pi * radius

print(f'{calculated_area:.2f}')

print(f'{calculated_perimeter:.2f}')
