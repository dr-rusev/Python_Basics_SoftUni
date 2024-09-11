budget = float(input())
series = int(input())
total_price = 0

for _ in range(series):

    name = input()
    price = float(input())
    if name == "Thrones":
        price *= 0.5
    elif name == "Lucifer":
        price *= 0.6
    elif name == "Protector":
        price *= 0.7
    elif name == "TotalDrama":
        price *= 0.8
    elif name == "Area":
        price *= 0.9

    total_price += price

if budget >= total_price:
    print(f"You bought all the series and left with {budget - total_price:.2f} lv.")

else:
    print(f"You need {total_price - budget:.2f} lv. more to buy the series!")
