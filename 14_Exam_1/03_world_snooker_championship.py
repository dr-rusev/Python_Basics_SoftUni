# Задача 3. Билети за снукър
# С наближаването на световното първенство по снукър в театъра Крусибъл в Шефилд, Англия, феновете нямат търпение да се сдобият с ценните билети. Заради големия наплив от хора, организаторите ви молят да напишете програма за продаване на билети, като се има предвид следния ценоразпис:
#     Четвъртфинал    Полуфинал    Финал
# Стандартен    55.50 £/бр.    75.88 £/бр.    110.10 £/бр.
# Премиум    105.20 £/бр.    125.22 £/бр.    160.66 £/бр.
# ВИП    118.90 £/бр.    300.40 £/бр.    400 £/бр.
# При закупуване на билет, зрителят може да избере опция, снимка с трофея, на цена 40 лири.
# При достигане на определена сума има отстъпки:
# •    Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана, таксата от 40 лири за билет не се включва)
# •    Над 2500 лири има 10% отстъпка
# При избрана опция за снимки с трофея, цената се начислява след изчисляването на отстъпките.
# Вход
# От конзолата се четат 4 реда:
# Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# Вид на билета – текст - “Standard”, “Premium” или “VIP”
# Брой билети – цяло число в интервала [1 … 30]
# Снимка с трофея – символ – 'Y' (да) или 'N' (не)
# Изход
# На конзолата се отпечатва 1 ред:
# •    "Цената, която трябва да се заплати, форматирана до втората цифра след десетичния знак"

stage = input()  # “Quarter final ”, “Semi final” или “Final”
ticket_type = input()  # “Standard”, “Premium” или “VIP”
ticket_number = int(input())
trophy_picture = input()  # 'Y' (да) или 'N' (не)
ticket_price = 0

if ticket_type == "Standard":
    if stage == "Quarter final":
        ticket_price = 55.50
    elif stage == "Semi final":
        ticket_price = 75.88
    elif stage == "Final":
        ticket_price = 110.10

elif ticket_type == "Premium":
    if stage == "Quarter final":
        ticket_price = 105.20
    elif stage == "Semi final":
        ticket_price = 125.22
    elif stage == "Final":
        ticket_price = 160.66

elif ticket_type == "VIP":
    if stage == "Quarter final":
        ticket_price = 118.90
    elif stage == "Semi final":
        ticket_price = 300.40
    elif stage == "Final":
        ticket_price = 400

total_price = ticket_number * ticket_price

if total_price > 4_000:
    total_price *= 0.75

elif total_price > 2_500:
    total_price *= 0.9

if total_price <= 4_000 and trophy_picture == "Y":
    total_price += 40 * ticket_number

print(f"{total_price:.2f}")

#stage = input()  # “Quarter final ”, “Semi final” или “Final”
# ticket_type = input()  # “Standard”, “Premium” или “VIP”
# ticket_number = int(input())
# trophy_picture = input()  # 'Y' (да) или 'N' (не)
#
# tickets_info = {
#     "Standard": {
#         "Quarter final": 55.5,
#         "Semi final": 75.88,
#         "Final": 110.10
#     },
#     "Premium": {
#         "Quarter final": 105.2,
#         "Semi final": 125.22,
#         "Final": 160.66
#     },
#     "VIP": {
#         "Quarter final": 118.9,
#         "Semi final": 300.4,
#         "Final": 400
#     },
# }
#
# # will be 0 if you pass something that is not in the dictionary
# ticket_price = tickets_info.get(ticket_type, {}).get(stage, 0)
# # will multiply by 0 if we get non-existent dictionary key
# total_price = ticket_number * ticket_price
#
# # you can check here if the price is 0 before doing anything else
#
# #
#
# if total_price > 4_000:
#     total_price *= 0.75
# elif total_price > 2_500:
#     total_price *= 0.9
#
# if total_price <= 4_000 and trophy_picture == "Y":
#     total_price += 40 * ticket_number
#
# print(f"{total_price:.2f}")