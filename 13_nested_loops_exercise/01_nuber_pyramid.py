# Напишете програма, която чете цяло число n,
# въведено от потребителя, и отпечатва пирамида от числа като в примерите:
# вход	        изход
# 7	            1
#               2 3
#               4 5 6
#               7
# 10	        1
#               2 3
#               4 5 6
#               7 8 9 10
current = 1
is_current_bigger_than_n = False
n = int(input())
for row in range(1, n +1):
    for col in range(1, row +1):
        if current > n:
            break
        print(current, end =' ')
        current += 1
    print()

# current = 1
# is_current_bigger_than_n = False
# n= int(input())
# for i in range(n + 1):
#     for j in range(i):
#         if current > n:
#             break
#         print(current, end = ' ')
#         current += 1
#     print()
#
# current = 1
# is_current_bigger_than_n = False
# n = int(input())
# for row in range(1, n +1):
#     for col in range(1, row +1):
#         if current > n:
#             # is_current_bigger_than_n = True
#             break
#         print(current, end =' ')
#         current += 1
#     print()
#     if is_current_bigger_than_n:
#     break
# n = int(input())
# current = 1
# current_numnber
#
# for row in range(1, n + 1)