desi_score = 0
opponent_score = 0
win_games, lost_games = 0, 0
tournament_name = ""

while tournament_name != "End of tournaments":
    tournament_name = input()
    if tournament_name == "End of tournaments":
        print(f"{win_games / (win_games + lost_games) * 100:.2f}% matches win")
        print(f"{lost_games / (win_games + lost_games) * 100:.2f}% matches lost")
        break

    matches_number = int(input())

    for game in range(1, matches_number + 1):
        desi_score = int(input())
        opponent_score = int(input())

        if desi_score > opponent_score:
            win_games += 1
            result = "win"

        elif desi_score < opponent_score:
            lost_games += 1
            result = "lost"

        difference = abs(desi_score - opponent_score)
        print(
            f"Game {game} of tournament {tournament_name}: {result} with {difference} points."
        )


# tournament_name = input()
# wins = 0
# loses = 0
#
# while tournament_name != "End of tournaments":
#     number_of_games = int(input())
#
#     for game in range(1, number_of_games + 1):
#         home_team = int(input())
#         away_team = int(input())
#         difference = abs(home_team - away_team)
#
#         if home_team > away_team:
#             wins += 1
#             result = "win"
#
#         elif home_team < away_team:
#             loses += 1
#             result = "lost"
#
#         print(
#             f"Game {game} of tournament {tournament_name}: {result} with {difference} points."
#         )
#
#     tournament_name = input()
#
# print(f"{(wins / (wins + loses)) * 100:.2f}% matches win")
# print(f"{(loses / (wins + loses)) * 100:.2f}% matches lost")
