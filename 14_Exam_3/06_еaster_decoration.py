customers = int(input())

basket_price = 1.5
wreath_price = 3.80
chocolate_bunny = 7

total_revenue = 0

for customer in range(customers):
    product = input()
    current_items = 0
    current_bill = 0

    while product != "Finish":
        current_items += 1
        price = 0

        if product == "basket":
            price = 1.5

        elif product == "wreath":
            price = 3.80

        elif product == "chocolate bunny":
            price = 7

        current_bill += price
        product = input()

    if current_items % 2 == 0:
        current_bill *= 0.8

    total_revenue += current_bill
    print(f"You purchased {current_items} items for {current_bill:.2f} leva.")

print(f"Average bill per client is: {total_revenue / customers:.2f} leva.")

# customers = int(input())
# total_revenue = 0
#
# for customer in range(customers):
#     current_items = 0
#     current_bill = 0
#     product = ""
#
#     while product != "Finish":
#         product = input()
#
#         if product == "Finish":
#             if current_items % 2 == 0:
#                 current_bill *= 0.8
#             print(f"You purchased {current_items} items for {current_bill:.2f} leva.")
#             break
#
#         current_items += 1
#         price = 0
#
#         if product == "basket":
#             price = 1.5
#
#         elif product == "wreath":
#             price = 3.80
#
#         elif product == "chocolate bunny":
#             price = 7
#
#         current_bill += price
#
#     total_revenue += current_bill
#
# print(f"Average bill per client is: {total_revenue / customers:.2f} leva.")
