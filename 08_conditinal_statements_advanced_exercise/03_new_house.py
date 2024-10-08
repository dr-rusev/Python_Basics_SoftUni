# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята,
# че Ви убеждава да напишете програма, която да изчисли колко  ще им струва,
# за да засадят определен брой цветя и дали наличният # бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете	                Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	    3.80	2.80	3	    2.50
# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума}
# leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.
flower = input()
quantity = int(input())
budget = int(input())
if flower == 'Roses':
    cost = quantity * 5
    if quantity > 80:
        cost = cost * 0.9
elif flower == 'Dahlias':
    cost = quantity * 3.8
    if quantity > 90:
        cost = cost * 0.85
elif flower == 'Tulips':
    cost = quantity * 2.8
    if quantity > 80:
        cost = cost * 0.85
elif flower == 'Narcissus':
    cost = quantity * 3
    if quantity < 120:
        cost = cost * 1.15
elif flower == 'Gladiolus':
    cost = quantity * 2.5
    if quantity < 80:
        cost = cost * 1.20
rest = budget - cost
if rest >= 0:
    rest = f'{rest:.2f}'
    print(f"Hey, you have a great garden with {quantity} {flower} and {rest} leva left.")
else:
    rest = -rest
    rest = f'{rest:.2f}'
    print(f"Not enough money, you need {rest} leva more.")