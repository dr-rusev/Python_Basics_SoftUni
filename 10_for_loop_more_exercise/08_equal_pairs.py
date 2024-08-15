# Дадени са 2*n-на брой числа. Първото и второто формират двойка,
# третото и четвъртото също и т.н. Всяка двойка има стойност –
# сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност
# или печата максималната разлика между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте
# "Yes, value={Value}" + стойността.
# В противен случай отпечатайте "No, maxdiff={Difference}" + максималната разлика.

pairs = int(input())
previous_sum = int(input()) + int(input())
max_diff = 0

for i in range(1, pairs):
    current_sum = int(input()) + int(input())
    if abs(previous_sum - current_sum) > max_diff:
        max_diff = abs(previous_sum - current_sum)

    previous_sum = current_sum

if max_diff == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_diff}")

count = int(input())
previousSum = int(input()) + int(input())
maxDifference = 0

for i in range(count - 1):
    currentSum = int(input()) + int(input())

    if abs(previousSum - currentSum) > maxDifference:
        maxDifference = abs(previousSum - currentSum)

    previousSum = currentSum

if maxDifference == 0:
    print(f"Yes, value={previousSum}")
else:
    print(f"No, maxdiff={maxDifference}")