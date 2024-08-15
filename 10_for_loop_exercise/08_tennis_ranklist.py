# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки,
# които зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели
# от всички изиграни турнири и колко процента от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу,
# а процентът да се форматира до втората цифра след десетичния знак.

from math import floor
number_tournaments = int(input())
initial_score = int(input())
total_score = 0
current_score = 0
number_w = 0
number_f = 0
number_sf = 0
score_w = 2000
score_f = 1200
score_sf = 720

for i in range(1, number_tournaments + 1):
    tournament_stage = input()
    if tournament_stage == 'W':
        number_w += 1
        current_score += current_score + score_w
    if tournament_stage == 'F':
        number_f += 1
        current_score += current_score + score_f
    if tournament_stage == 'SF':
        number_sf += 1
        current_score += current_score + score_sf

per_w_tourn = number_w / number_tournaments * 100
avg_tourn_score = (number_w * score_w + number_f * score_f + number_sf * score_sf) / number_tournaments
avg_tourn_score = floor(avg_tourn_score)
total_score = initial_score + number_w * score_w + number_f * score_f + number_sf * score_sf
print(f"Final points: {total_score}")
print(f"Average points: {avg_tourn_score}")
print(f"{per_w_tourn:.2f}%")

