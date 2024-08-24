from math import floor, ceil

tennis_racket_price = float(input())
tennis_racket_number = int(input())
pair_of_sneakers_number = int(input())

pair_of_sneakers_price = 1 / 6 * tennis_racket_price
other_equipment_price = 0.2 * (
    tennis_racket_price * tennis_racket_number
    + pair_of_sneakers_price * pair_of_sneakers_number
)

total_price = (
    tennis_racket_price * tennis_racket_number
    + pair_of_sneakers_price * pair_of_sneakers_number
    + other_equipment_price
)

djokovic_price = floor(1 / 8 * total_price)
sponsors_price = ceil(7 / 8 * total_price)

print(f"Price to be paid by Djokovic {djokovic_price}")
print(f"Price to be paid by sponsors {sponsors_price}")

# test
