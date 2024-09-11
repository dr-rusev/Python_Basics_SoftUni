a1 = int(input()) # [65… 89]
a2 = int(input()) # [66… 91]
n = int(input()) # [1… 10]

for symbol1 in range (a1, a2):
    if not symbol1 % 2 != 0:
        continue

    for symbol2 in range(1, n):

        for symbol3 in range(1, n // 2):

            if (symbol2 + symbol3 + symbol1) % 2 != 0:

                print(f"{chr(symbol1)}-{symbol2}{symbol3}{symbol1}")

# a1 = int(input()) # [65… 89]
# a2 = int(input()) # [66… 91]
# n = int(input()) # [1… 10]
#
# for symbol1 in range (a1, a2):
#
#     for symbol2 in range(1, n):
#
#         for symbol3 in range(1, n // 2):
#
#             if symbol1 % 2 != 0 and (symbol2 + symbol3 + symbol1) % 2 != 0:
#
#                 print(f"{chr(symbol1)}-{symbol2}{symbol3}{symbol1}")

number_one = int(input())
number_two = int(input())
number = int(input())

for i in range(number_one, number_two):

    for o in range(1, number):

        for p in range(1, number // 2):

            if i % 2 != 0 and (i + o + p) % 2 != 0:

                print(f"{chr(i)}-{o}{p}{i}")
