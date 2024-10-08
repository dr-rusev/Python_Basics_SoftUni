# Екипът на СофтУни си организира футболен турнир. Първоначално прочитаме
# от конзолата капацитета на стадиона и броят на всички фенове.
# След това за всеки фен се чете секторът, в който се намира.
# Феновете на първия отбор са в сектор А и Б, а на втория – В и Г.
# Да се напише програма, която изчислява процентите на феновете във всеки сектор,
# спрямо общия брой фенове на стадиона, както и общият процент на феновете
# за двата отбора, спрямо капацитета на стадиона.
# Общият брой на феновете НЕ надвишава капацитета на стадиона.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
#   1. Капацитетът на стадиона – цяло число в интервала [1 … 10000];
#   2. Броят на всички фенове – цяло число в интервала [1 … 10000].
# За всеки един фен, на отделен ред се прочита:
#   1.	Секторът, на който се намира – текст – "A", "B", "V" и "G".
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00%, форматирани до втората цифра след десетичната запетая:
#   1. Процентът на феновете в сектор А
#   2. Процентът на феновете в сектор Б
#   3. Процентът на феновете в сектор В
#   4. Процентът на феновете в сектор Г
#   5. Процентът на всички фенове, спрямо капацитета на стадиона
capacity_stadium = int(input())
all_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0
for fan in range(1, all_fans + 1):
    sector = input()
    if sector == 'A':
        fans_a += 1
    if sector == 'B':
        fans_b += 1
    if sector == 'V':
        fans_v += 1
    if sector == 'G':
        fans_g += 1

print(f"{(fans_a / all_fans * 100):.2f}%")
print(f"{(fans_b / all_fans * 100):.2f}%")
print(f"{(fans_v / all_fans * 100):.2f}%")
print(f"{(fans_g / all_fans * 100):.2f}%")
print(f"{(all_fans / capacity_stadium * 100):.2f}%")