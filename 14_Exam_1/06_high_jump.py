goal = int(input())

initial_goal = goal - 30
bad_jump, total_jump = 0, 0

while initial_goal <= goal:

    jump = int(input())
    total_jump += 1

    if jump > initial_goal:
        initial_goal += 5
        bad_jump = 0
    else:
        bad_jump += 1

        if bad_jump == 3:
            print(f"Tihomir failed at {initial_goal}cm after {total_jump} jumps.")
            break

    if initial_goal > goal:
        print(f"Tihomir succeeded, he jumped over {goal}cm after {total_jump} jumps.")
        break