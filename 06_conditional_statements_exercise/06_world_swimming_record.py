# Иван решава да подобри Световния рекорд по плуване на дълги разстояния.
# На конзолата се въвежда рекордът в секунди, който Иван трябва да подобри,
# разстоянието в метри, което трябва да преплува и времето в секунди,
# за което плува разстояние от 1 м. Да се напише програма, която изчислява дали се е справил със задачата,
# като се има предвид, че: съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
# Когато се изчислява колко пъти Иван ще се забави, в резултат на съпротивлението на водата,
# резултатът трябва да се закръгли надолу до най-близкото цяло число.
# Да се изчисли времето в секунди, за което Иван ще преплува разстоянието и разликата спрямо Световния рекорд.
# Вход
# От конзолата се четат 3 реда:
# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако Иван е подобрил Световния рекорд (времето му е по-малко от рекорда) отпечатваме:
# o	" Yes, he succeeded! The new world record is {времето на Иван} seconds."
# •	Ако НЕ е подобрил рекорда (времето му е по-голямо или равно на рекорда) отпечатваме:
# o	"No, he failed! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
# math.floor()
import math
world_record = float(input())
distance = float(input())
time_per_meter = float(input())

time_Ivan = distance * time_per_meter

if distance >= 15:
    delay = math.floor(distance / 15) * 12.5
    time_Ivan += delay

result = time_Ivan - world_record

if result >= 0:
    print("No, he failed! He was " + f'{result:.2f}' + " seconds slower.")
else:
    print("Yes, he succeeded! The new world record is " + f'{time_Ivan:.2f}' + " seconds.")
