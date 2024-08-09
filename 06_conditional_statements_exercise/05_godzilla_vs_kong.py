# дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат нужни
# определен брой статисти, облекло за всеки един статист и декор.
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# От конзолата се четат 3 реда:
# Вход
# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
# •	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

budget = float(input())
statist = int(input())
price_dress_statist = float(input())
price_decor = budget * 0.1
if statist > 150:
    price_dress_statist *= 0.9

costs = price_decor + statist * price_dress_statist
profit = budget - costs
if profit >= 0:
    print("Action!")
    print("Wingard starts filming with " + f'{profit:.2f}' + " leva left.")

else:
    print("Not enough money!")
    print("Wingard needs " + f'{- profit:.2f}' + " leva more.")
