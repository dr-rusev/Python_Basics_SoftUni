player_name = input()
good_shots = 0
bad_shots = 0
initial_score = 301
field = ""

while field != "Retire":  # текст ("Single", "Double" или "Triple")
    field = input()
    if field == "Retire":
        print(f"{player_name} retired after {bad_shots} unsuccessful shots.")
        break

    score = int(input())  # цяло число в интервала [0… 100]

    if field == "Double":
        score *= 2

    elif field == "Triple":
        score *= 3

    if score <= initial_score:
        good_shots += 1
        initial_score -= score

        if initial_score == 0:
            print(f"{player_name} won the leg with {good_shots} shots.")
            break

    else:

        bad_shots += 1

# player_name = input()
# good_shots = 0
# bad_shots = 0
# initial_score = 301
#
# field = input()  # текст ("Single", "Double" или "Triple")
#
# while field != "Retire":
#
#     score = int(input())  # цяло число в интервала [0… 100]
#
#     if field == "Double":
#         score *= 2
#
#     elif field == "Triple":
#         score *= 3
#
#     if score <= initial_score:
#         good_shots += 1
#         initial_score -= score
#
#         if not initial_score:
#             print(f"{player_name} won the leg with {good_shots} shots.")
#             break
#
#     else:
#
#         bad_shots += 1
#
#     field = input()
#
# else:
#     print(f"{player_name} retired after {bad_shots} unsuccessful shots.")
