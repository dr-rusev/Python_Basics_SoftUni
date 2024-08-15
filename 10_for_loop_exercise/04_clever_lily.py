# Лили вече е на N години. За всеки свой рожден ден тя получава подарък.
# •	За нечетните рождени дни (1, 3, 5...n) получава играчки.
# •	За четните рождени дни (2, 4, 6...n) получава пари.
# За втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв.,
# за всеки следващ четен рожден ден (2 -> 10, 4 -> 20, 6 -> 30...и т.н.).
# През годините Лили тайно е спестявала парите. Братът на Лили, в годините, които тя получава пари,
# взима по 1.00 лев от тях. Лили продала играчките получени през годините, всяка за P лева
# и добавила сумата към спестените пари. С парите искала да си купи пералня за X лева.
# Напишете програма, която да пресмята, колко пари е събрала и дали ѝ стигат да си купи пералня.
# Вход
# Програмата прочита 3 числа, въведени от потребителя, на отделни редове:
# •	Възрастта на Лили - цяло число в интервала [1...77]
# •	Цената на пералнята - число в интервала [1.00...10 000.00]
# •	Единична цена на играчка - цяло число в интервала [0...40]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако парите на Лили са достатъчни:
# o	"Yes! {N}" - където N е остатъка пари след покупката
# •	Ако парите не са достатъчни:
# o	"No! {М}" - където M е сумата, която не достига
# Числата N и M трябва да за форматирани до вторият знак след десетичната запетая.
age_Lily = int(input())
price_wm = float(input())
price_toy = int(input())
money_bd = 0
quantity_toys = 0
for i in range(1, age_Lily + 1):
    if i % 2 == 0:
        money_bd += i * 5 -1
    else:
        quantity_toys += 1

total_savings = money_bd + quantity_toys * price_toy

diff = abs(total_savings - price_wm)
diff = f'{diff:.2f}'
if total_savings >= price_wm:
    print(f"Yes! {diff}")
else:
    print(f"No! {diff}")

