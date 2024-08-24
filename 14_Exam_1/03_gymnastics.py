country = input()
instrument = input()

difficulty = 0
turn = 0

if instrument == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        turn = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        turn = 9.400
    elif country == "Italy":
        difficulty = 9.200
        turn = 9.500

elif instrument == "hoop":
    if country == "Russia":
        difficulty = 9.300
        turn = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        turn = 9.750
    elif country == "Italy":
        difficulty = 9.450
        turn = 9.350

elif instrument == "rope":
    if country == "Russia":
        difficulty = 9.600
        turn = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        turn = 9.400
    elif country == "Italy":
        difficulty = 9.700
        turn = 9.150

total_score = difficulty + turn
difference_to_max_score = 20 - total_score

print(f"The team of {country} get {total_score:.3f} on {instrument}.")
print(f"{(difference_to_max_score / 20) * 100:.2f}%")
