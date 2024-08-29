# voucher = int(input())
# tickets, products, ticket_price = 0, 0, 0
# purchase = input()
# while purchase != "End":
#     if len(purchase) > 8:
#         ticket_price = ord(purchase[0]) + ord(purchase[1])
#         if ticket_price <= voucher:
#             tickets += 1
#             voucher -= ticket_price
#         else:
#             break
#
#     elif len(purchase) <= 8:
#         product_price = ord(purchase[0])
#         if product_price <= voucher:
#             products += 1
#             voucher -= product_price
#         else:
#             break
#
#     purchase = input()
#
# print(f"{tickets}")
# print(f"{products}")

voucher = int(input())
tickets, products = 0, 0

purchase = input()
while purchase != "End":
    if len(purchase) > 8:
        voucher -= ord(purchase[0]) + ord(purchase[1])
        if voucher < 0:
            break

        tickets += 1

    elif len(purchase) <= 8:
        voucher -= ord(purchase[0])
        if voucher < 0:
            break

        products += 1

    purchase = input()

print(f"{tickets}")
print(f"{products}")

# voucher = int(input())
# tickets, products = 0, 0
# purchase = ''
#
# while purchase != "End":
#     purchase = input()
#     if purchase == "End":
#         break
#
#     elif len(purchase) > 8:
#         voucher -= ord(purchase[0]) + ord(purchase[1])
#         if voucher < 0:
#             break
#
#         tickets += 1
#
#     elif len(purchase) <= 8:
#         voucher -= ord(purchase[0])
#         if voucher < 0:
#             break
#
#         products += 1
#
# print(f"{tickets}")
# print(f"{products}")