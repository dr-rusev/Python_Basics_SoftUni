# Напишете програма, която да пресмята статистика на оценки от изпит.
# В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка.
# На края програмата трябва да изпечата процента на студенти с оценка между 2.00 и 2.99,
# между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средният успех на изпита.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.

students = int(input())
sc_23 = 0
sc_34 = 0
sc_45 = 0
sc_56 = 0
total_score = 0
for i in range(1, students + 1):
    score = float(input())
    total_score += score
    if 2 <= score < 3:
        sc_23 += 1
    elif 3 <= score < 4:
        sc_34 += 1
    elif 4 <= score < 5:
        sc_45 += 1
    elif 5 <= score:
        sc_56 += 1

avg_score = total_score / students
ref_23_percent = sc_23 / students * 100
ref_34_percent = sc_34 / students * 100
ref_45_percent = sc_45 / students * 100
ref_56_percent = sc_56 / students * 100

print(f"Top students: {ref_56_percent:.2f}%")
print(f"Between 4.00 and 4.99: {ref_45_percent:.2f}%")
print(f"Between 3.00 and 3.99: {ref_34_percent:.2f}%")
print(f"Fail: {ref_23_percent:.2f}%")
print(f"Average: {avg_score:.2f}")
