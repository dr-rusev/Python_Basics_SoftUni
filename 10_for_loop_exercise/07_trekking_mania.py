# Катерачи от цяла България се събират на групи и набелязват следващите върхове за изкачване.
# Според размера на групата, катерачите ще изкачват различни върхове.
# • Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
# Да се напише програма, която изчислява процента на катерачите изкачващи всеки връх.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 5 реда, всеки от които съдържа процент между 0.00% и 100.00%
# с точност до втората цифра след десетичната запетая.
# •	Първи ред - процентът изкачващи Мусала
# •	Втори ред – процентът изкачващи Монблан
# •	Трети ред – процентът изкачващи Килиманджаро
# •	Четвърти ред – процентът изкачващи К2
# •	Пети ред – процентът изкачващи Еверест
groups = int(input())
track_mus = 0
track_mon = 0
track_kil = 0
track_k2 = 0
track_ev = 0
for i in range(1, groups + 1):
    number_people = int(input())
    if 0 <= number_people <= 5:
        track_mus += number_people
    elif 6 <= number_people <= 12:
        track_mon += number_people
    elif 13 <= number_people <= 25:
        track_kil += number_people
    elif 26 <= number_people <= 40:
        track_k2 += number_people
    elif 41 <= number_people:
        track_ev += number_people
total_track = track_mus + track_mon + track_kil + track_k2 + track_ev
per_mus = track_mus/total_track * 100
per_mon = track_mon/total_track * 100
per_kil = track_kil/total_track * 100
per_k2 = track_k2/total_track * 100
per_ev = track_ev/total_track * 100
print(f'{per_mus:.2f}%')
print(f'{per_mon:.2f}%')
print(f'{per_kil:.2f}%')
print(f'{per_k2:.2f}%')
print(f'{per_ev:.2f}%')