football_team = input()
matches = int(input())
counter_w, counter_d, counter_l, score = 0, 0, 0, 0

if matches == 0:
    print(f"{football_team} hasn't played any games during this season.")
    exit()
for _ in range(matches):
    result = input()
    if result == "W":
        counter_w += 1
        score += 3
    elif result == "D":
        counter_d += 1
        score += 1
    elif result == "L":
        counter_l += 1

print(f"{football_team} has won {score} points during this season.")
print(f"Total stats:")
print(
    f"## W: {counter_w}\n## D: {counter_d}\n## L: {counter_l}\nWin rate: {counter_w / matches * 100:.2f}%"
)