# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино.
# От 1 кв.м лозе се изкарват Y килограма грозде. За 1 литър вино са нужни 2,5 кг. грозде.
# Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали
# това количество е достатъчно. Ако е достатъчно, остатъкът се разделя по равно
# между работниците на лозето.
# Вход
# Входът се чете от конзолата и се състои от точно 4 реда:
# •	1ви ред: X кв.м е лозето – цяло число в интервала [10 … 5000]
# •	2ри ред: Y грозде за един кв.м – реално число в интервала [0.00 … 10.00]
# •	3ти ред: Z нужни литри вино – цяло число в интервала [10 … 600]
# •	4ти ред: брой работници – цяло число в интервала [1 … 20]
# Изход
# На конзолата трябва да се отпечата следното:
# •	Ако произведеното вино е по-малко от нужното:
# o	“It will be a tough winter! More {недостигащо вино} liters wine needed.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# •	Ако произведеното вино е колкото или повече от нужното:
# o	“Good harvest this year! Total wine: {общо вино} liters.”
# 	Резултатът трябва да е закръглен към по-ниско цяло число
# o	“{Оставащо вино} liters left -> {вино за 1 работник} liters per person.”
# 	И двата резултата трябва да са закръглени към по-високото цяло число
vineyard = int(input())
grapes = float(input())
liters = int(input())
workers = int(input())
import math
harvest = vineyard * grapes * 0.4
wine = harvest / 2.5
liters_left = abs(wine - liters)
liters_per_person = liters_left / workers

if wine < liters:
    litters_left = math.floor(liters_left)
    print("It will be a tough winter! More " + f'{litters_left}' + " liters wine needed.")
elif wine >= liters:
    wine = math.floor(wine)
    liters_left = math.ceil(liters_left)
    liters_per_person = math.ceil(liters_per_person)
    print("Good harvest this year! Total wine: " + f'{wine}' + " liters.")
    print(f'{liters_left}' + " liters left -> " + f'{liters_per_person}' + " liters per person.")

