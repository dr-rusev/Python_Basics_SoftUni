# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя,
# и проверява дали сумата на първите n числа (лява сума) е равна
# на сумата на вторите n числа (дясна сума). При равенство печата "Yes, sum = " + сумата;
# иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).
# for i in range(2 * n):
#     num = int(input())
#     if i < n:
#         sum_left += num
#     else:
#         sum_right += num
# if sum_left == sum_right:
#     print(f'Yes, sum = {sum_left}')
# else:
#     print(f'No, diff = {abs(sum_left - sum_right)}')
n = int(input())
left_sum = 0
for i in range(n):
    left_sum = left_sum + int(input())
right_sum = 0
for i in range(n):
    right_sum = right_sum + int(input())

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(right_sum - left_sum)
    print(f"No, diff = {diff}")





