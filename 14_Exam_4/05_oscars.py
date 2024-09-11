actor_name = input()
academy_score = float(input())
jury_number = int(input())
jury_total_score = 0
total_score = 0
diff = 0
for i in range(1, jury_number + 1):
    jury_name = input()
    jury_score = float(input())
    jury_total_score += len(jury_name) * jury_score / 2
    if jury_total_score + academy_score > 1250.5:
        total_score = jury_total_score + academy_score
        print(
            f"Congratulations, {actor_name} got a nominee for leading role with {total_score:.1f}!"
        )
        break
else:
    diff = 1250.5 - (jury_total_score + academy_score)
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")