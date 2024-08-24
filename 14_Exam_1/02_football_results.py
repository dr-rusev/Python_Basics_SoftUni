# Футболен отбор участва в благотворителен турнир. На този турнир
# отборът играе три мача като домакин. Да се напише програма, която
# изчислява колко победи, равенства и загуби има отборът по време на турнира,
# спрямо резултатите от мачовете.
# *Забележка: Отборът винаги е домакин, следователно първата цифра от
# резултата съответства на головете вкарани от него.


team_win = 0
team_lost = 0
team_draw = 0

for _ in range(3):
    match_stats = input()
    first_team = int(match_stats[0])
    second_team = int(match_stats[-1])

    if first_team > second_team:
        team_win += 1
    elif first_team < second_team:
        team_lost += 1
    elif first_team == second_team:
        team_draw += 1

print(f"Team won {team_win} games.")
print(f"Team lost {team_lost} games.")
print(f"Drawn games: {team_draw}")

# def get_match_result(match_result: str) -> str:
#     """
#     :param match_result: 5:0
#     :return: key for a dictionary
#     """
#     first_team, second_team = [int(x) for x in match_result.split(":")]
#
#     if first_team > second_team:
#         return won_key
#
#     if first_team < second_team:
#         return lost_key
#
#     return draw_key
#
#
# result_first_match = input()
# result_second_match = input()
# result_third_match = input()
#
# won_key = "won"
# lost_key = "lost"
# draw_key = "draw"
# results = {key: 0 for key in (won_key, lost_key, draw_key)}
#
# for match in (result_first_match, result_second_match, result_third_match):
#     key = get_match_result(match)
#     results[key] += 1
#
# print(f"Team won {results[won_key]} games.")
# print(f"Team lost {results[lost_key]} games.")
# print(f"Drawn games: {results[draw_key]}")

# result_first_match = input()
# result_second_match = input()
# result_third_match = input()
#
# team_won = 0
# team_lost = 0
# drawn_games = 0
#
# if int(result_first_match[0]) > int(result_first_match[2]):
#     team_won += 1
#
# elif int(result_first_match[0]) < int(result_first_match[2]):
#     team_lost += 1
#
# elif int(result_first_match[0]) == int(result_first_match[2]):
#     drawn_games += 1
#
# if int(result_second_match[0]) > int(result_second_match[2]):
#     team_won += 1
#
# elif int(result_second_match[0]) < int(result_second_match[2]):
#     team_lost += 1
#
# elif int(result_second_match[0]) == int(result_second_match[2]):
#     drawn_games += 1
#
# if int(result_third_match[0]) > int(result_third_match[2]):
#     team_won += 1
#
# elif int(result_third_match[0]) < int(result_third_match[2]):
#     team_lost += 1
#
# elif int(result_third_match[0]) == int(result_third_match[2]):
#     drawn_games += 1
#
# print(f"Team won {team_won} games.")
# print(f"Team lost {team_lost} games.")
# print(f"Drawn games: {drawn_games}")
