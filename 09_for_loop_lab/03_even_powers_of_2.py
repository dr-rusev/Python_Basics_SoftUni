# Да се напише програма, която чете число n,
# въведено от потребителя, и печата четните степени на 2 ≤ 2n: 20, 22, 24, 26, …, 2n.
n = int(input())
num = 1
for i in range(0, n + 1, 2):
    print(num)
    num = 2 * 2 * num
# Да се напише програма, която чете число n,въведено от потребителя,
# и печата нечетните степени на 2 ≤ 2(n+1): 21, 23, 25, 27, …, 2n.
# n = int(input())
# num = 1
# for i in range(0, n + 1):
#     print(num)
#     num = 2 * 2 * 2 * num
# n = int(input())
# for i in range(1, n + 1, 2):
#     print(2 ** i)
# n = int(input())
# num = 2
# for i in range(1, n + 1, 2):
#     print(num)
#     num = 2 * 2 * num