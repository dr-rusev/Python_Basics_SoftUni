sold_games = int(input())
counter_h, counter_f, counter_o, counter_r = 0, 0, 0, 0
for _ in range(sold_games):
    game_name = input()
    if game_name == "Hearthstone":
        counter_h += 1
    elif game_name == "Fornite":
        counter_f += 1
    elif game_name == "Overwatch":
        counter_o += 1
    else:
        counter_r += 1

print(f"Hearthstone - {counter_h / sold_games * 100:.2f}%")
print(f"Fornite - {counter_f / sold_games * 100:.2f}%")
print(f"Overwatch - {counter_o / sold_games * 100:.2f}%")
print(f"Others - {counter_r / sold_games * 100:.2f}%")