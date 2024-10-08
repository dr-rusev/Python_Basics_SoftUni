# Напишете програма, която чете от конзолата две шестцифрени цели числа.
# Винаги първото въведено число ще бъде по-малко от второто.
# На конзолата да се отпечатат на 1, ред разделени с интервал, всички числа,
# които се намират между двете, прочетени от конзолата числа и отговарят
# на условието сумата от цифрите на четни и нечетни позиции да са равни.
# Ако няма числа, отговарящи на условието на конзолата не се извежда резултат.
# Примерен вход и изход
# Вход          Изход
# 100000        100001 100012
# 100050        100023 100034

# Обяснения
# Първото число, което генерираме е числото 100000. Сумата от цифрите на четни позиции (жълто) е 0+0+0=0.
# Сумата от цифрите на нечетни позиции (зелено) е 0+0+1=1.
# Тъй като двете суми са различни числото не се отпечатва.
# Следващото, число е 100001. Сумата на четни позиции е  1+0+0=1, а на нечетни 0+0+1=1.
# Двете суми са равни и числото се отпечатва.
# Следващото число за проверка е 100002. То не отговаря на условието и не се отпечатва.
# ……
# При числото 100045 сумата от четните позиции е 5+0+0=5, а на нечетни 4+0+1=5.
# Двете суми са равни числото се отпечатва. И т.н.
#
# a = 'abcdef'
# for digit in enumerate(a):
#     print(digit)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')

# a = 'abcdef'
# for index in enumerate(a):
#     print(index)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')

# a = 'abcdef'
# for index, digit in enumerate(a):
#     print(index, digit)
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f

first_num = int(input())
second_num = int(input())
for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end = ' ')

#

