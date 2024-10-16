tournament_days = int(input())

total_wins, total_money = 0, 0

for day in range(tournament_days):
    current_day_wins, current_day_money = 0, 0

    sport = input()
    while sport != "Finish":
        game_output = input()
        if game_output == "win":
            current_day_wins += 1
            current_day_money += 20

        elif game_output == "lose":
            current_day_wins -= 1

        sport = input()

    total_wins += current_day_wins
    if current_day_wins > 0:
        current_day_money *= 1.10
    total_money += current_day_money


if total_wins > 0:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")




# tournament_days = int(input())
#
# total_wins, total_money = 0, 0
#
# for day in range(tournament_days):
#     current_day_wins, current_day_money = 0, 0
#
#     while True:
#         sport = input()
#         if sport == "Finish":
#             total_wins += current_day_wins
#             if current_day_wins > 0:
#                 current_day_money *= 1.10
#             total_money += current_day_money
#             break
#         game_output = input()
#
#         if game_output == "win":
#             current_day_wins += 1
#             current_day_money += 20
#         elif game_output == "lose":
#             current_day_wins -= 1
#
# if total_wins > 0:
#     total_money *= 1.20
#     print(f"You won the tournament! Total raised money: {total_money:.2f}")
# else:
#     print(f"You lost the tournament! Total raised money: {total_money:.2f}")
