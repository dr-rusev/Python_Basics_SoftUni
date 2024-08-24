first_player_name = input()
second_player_name = input()
first_player_score = second_player_score = 0
first_player_card = second_player_card = ""

while first_player_card != "End of game":
    first_player_card = input()
    if first_player_card == "End of game":
        print(f"{first_player_name} has {first_player_score} points")
        print(f"{second_player_name} has {second_player_score} points")
        break

    first_player_card = int(first_player_card)  # цяло число в интервала [2…9]
    second_player_card = int(input())  # цяло число в интервала [2…9]

    if first_player_card > second_player_card:
        first_player_score += first_player_card - second_player_card

    elif first_player_card < second_player_card:
        second_player_score += second_player_card - first_player_card

    elif first_player_card == second_player_card:
        first_player_card = int(input())
        second_player_card = int(input())

        print(f"Number wars!")

        if first_player_card > second_player_card:
            print(f"{first_player_name} is winner with {first_player_score} points")

        elif first_player_card < second_player_card:
            print(f"{second_player_name} is winner with {second_player_score} points")

        break

# first_player_name = input()
# second_player_name = input()
# first_player_score, second_player_score = 0, 0
# second_player_card = ""
#
# first_player_card = input()
# while first_player_card != "End of game":
#     first_player_card = int(first_player_card)  # цяло число в интервала [2…9]
#     second_player_card = int(input())  # цяло число в интервала [2…9]
#
#     if first_player_card > second_player_card:
#         first_player_score += first_player_card - second_player_card
#
#     elif first_player_card < second_player_card:
#         second_player_score += second_player_card - first_player_card
#
#     elif first_player_card == second_player_card:
#         first_player_card = int(input())
#         second_player_card = int(input())
#
#         print(f"Number wars!")
#
#         if first_player_card > second_player_card:
#             print(f"{first_player_name} is winner with {first_player_score} points")
#
#         elif first_player_card < second_player_card:
#             print(f"{second_player_name} is winner with {second_player_score} points")
#
#         break
#
#     first_player_card = input()
#
# else:
#     print(f"{first_player_name} has {first_player_score} points")
#     print(f"{second_player_name} has {second_player_score} points")

# first_player_name = input()
# second_player_name = input()
# first_player_score, second_player_score = 0, 0
# second_player_card = ""
#
# first_player_card = input()
# while first_player_card != "End of game":
#     first_player_card = int(first_player_card)  # цяло число в интервала [2…9]
#     second_player_card = int(input())  # цяло число в интервала [2…9]
#
#     if first_player_card > second_player_card:
#         first_player_score += first_player_card - second_player_card
#
#     elif first_player_card < second_player_card:
#         second_player_score += second_player_card - first_player_card
#
#     elif first_player_card == second_player_card:
#         first_player_card = int(input())
#         second_player_card = int(input())
#
#         print(f"Number wars!")
#
#         if first_player_card > second_player_card:
#             print(f"{first_player_name} is winner with {first_player_score} points")
#
#         elif first_player_card < second_player_card:
#             print(f"{second_player_name} is winner with {second_player_score} points")
#
#         exit()
#
#     first_player_card = input()
#
#
# print(f"{first_player_name} has {first_player_score} points")
# print(f"{second_player_name} has {second_player_score} points")
