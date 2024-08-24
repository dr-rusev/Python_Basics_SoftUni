from math import floor
number_tournaments = int(input())
initial_score = int(input())
total_score, current_score = 0, 0
number_w, number_f, number_sf = 0, 0, 0
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