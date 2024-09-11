player_name = input()
best_score = 0
player_counter = 0
best_name = ""
while player_name != "Stop":
    score = 0
    player_counter += 1
    for i in range(len(player_name)):
        number = int(input())
        if ord(player_name[i]) == number:
            score += 10
        else:
            score += 2
    if score >= best_score:
        best_score = score
        best_name = player_name

    player_name = input()

else:
    print(f"The winner is {best_name} with {best_score} points!")