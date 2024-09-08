cakes = int(input())
baker_best_score = 0
baker_best_name = ""

for cake in range(cakes):
    baker_name = input()

    score = input()
    current_baker_score = 0
    while score != "Stop":

        score = int(score)
        current_baker_score += score
        score = input()

    print(f"{baker_name} has {current_baker_score} points.")
    if current_baker_score > baker_best_score:
        baker_best_score = current_baker_score
        baker_best_name = baker_name
        print(f"{baker_best_name} is the new number 1!")

print(f"{baker_best_name} won competition with {baker_best_score} points!")