number_of_days = int(input())
number_of_hours = int(input())
price_even_day_odd_hour = 2.50
price_odd_day_even_hour = 1.25
price_other = 1
total_price = 0
for day in range(1, number_of_days + 1):
    current_day_price = 0
    current_price = 0
    for hour in range(1, number_of_hours + 1):

        if hour % 2 != 0 and day % 2 == 0:
            current_price += price_even_day_odd_hour
        elif hour % 2 == 0 and day % 2 != 0:
            current_price += price_odd_day_even_hour
        else:
            current_price += price_other

    current_day_price += current_price

    total_price += current_day_price

    print(f"Day: {day} - {current_day_price:.2f} leva")

print(f"Total: {total_price:.2f} leva")