budget = float(input())
product_name = input()
product_counter = 0
starting_budget = budget

while product_name != "Stop":

    product_price = float(input())
    product_counter += 1

    if product_counter % 3 == 0:
        product_price *= 0.5

    budget -= product_price

    if budget < 0:

        print(f"You don't have enough money!\nYou need {abs(budget):.2f} leva!")

        break

    product_name = input()

else:
    print(f"You bought {product_counter} products for {starting_budget - budget:.2f} leva.")