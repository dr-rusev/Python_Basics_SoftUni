# Поканени сте от академията да напишете софтуер, който да пресмята точките
# за актьор/актриса. Академията ще ви даде първоначални точки за актьора.
# След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава се формират от:
# дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне
# и да се отпечата, че дадения актьор е получил номинация.
# Вход
# •	Име на актьора - текст
# •	Точки от академията - реално число в интервала [2.0... 450.5]
# •	Брой оценяващи n - цяло число в интервала[1… 20]
# На следващите n-на брой реда:
# o	Име на оценяващия - текст
# o	Точки от оценяващия - реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако точките са над 1250.5:
# "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
# •	Ако точките не са достатъчни:
# 	"Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!
actor_name = input()
academy_score = float(input())
jury_number = int(input())
jury_total_score = 0
total_score = 0
diff = 0
for i in range(1, jury_number + 1):
    jury_name = input()
    jury_score = float(input())
    jury_total_score += len(jury_name) * jury_score / 2
    if jury_total_score + academy_score > 1250.5:
        total_score = jury_total_score + academy_score
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_score:.1f}!")
        break

diff = 1250.5 - (jury_total_score + academy_score)
if diff > 0:
    diff = f'{diff:.1f}'
    print(f"Sorry, {actor_name} you need {diff} more!")
