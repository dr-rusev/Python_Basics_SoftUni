visitors = int(input())
counter_back, counter_chest, counter_legs, counter_abs = 0, 0, 0, 0
counter_protein_shake, counter_protein_bar = 0, 0

for _ in range(visitors):
    activity = input()

    if activity == "Back":
        counter_back += 1

    elif activity == "Chest":
        counter_chest += 1

    elif activity == "Legs":
        counter_legs += 1

    elif activity == "Abs":
        counter_abs += 1

    elif activity == "Protein shake":
        counter_protein_shake += 1

    elif activity == "Protein bar":
        counter_protein_bar += 1

print(f"{counter_back} - back")
print(f"{counter_chest} - chest")
print(f"{counter_legs} - legs")
print(f"{counter_abs} - abs")
print(f"{counter_protein_shake} - protein shake")
print(f"{counter_protein_bar} - protein bar")

print(
    f"{(counter_back + counter_chest + counter_legs + counter_abs) / visitors * 100:.2f}% - work out"
)

print(
    f"{(counter_protein_shake + counter_protein_bar) / visitors * 100:.2f}% - protein"
)
