# Напишете програма, която чете от конзолата цели числа, докато не се получи
# команда "stop".
# Да се намери сумата на всички въведени прости и сумата на всички въведени непрости числа.
# Тъй като по дефиниция от математиката отрицателните числа не могат да бъдат прости,
# ако на входа се подаде отрицателно число, да се изведе следното съобщение "Number is negative.".
# В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# •	"Sum of all prime numbers is: {prime numbers sum}"
# •	"Sum of all non prime numbers is: {nonprime numbers sum}"
# Syntax:  sympy.isprime()
# Parameter:  n; number to be tested
# Return:  bool value result
# from sympy import *
# n = int(input())
# for i in range(1, n + 1):
#     print(i, end = ' ')
#     print(isprime(i), end = '  ')
# print()
# 1 False  2 True
#
# n = int(input())
# for i in range(1, n + 1):
#     print(i, end = ' ')
# print()
# for i in range(1, n + 1):
#     print(isprime(i), end = ' ')
#
# 1 2
# False True
# import sympy
# command = ''
# sum_primes = sum_non_primes = 0
# while command != 'stop':
#     command = input()
#     if command == 'stop':
#         break
#     number = int(command)
#     if number < 0:
#         print("Number is negative.")
#     elif number == 1:
#         sum_non_primes += number
#     elif number > 1:
#         if sympy.isprime(number):
#             sum_primes += number
#         else:
#             sum_non_primes += number
#
# print(f"Sum of all prime numbers is: {sum_primes}")
# print(f"Sum of all non prime numbers is: {sum_non_primes}")

command = ''
sum_primes = sum_non_primes = 0
while command != 'stop':
    command = input()
    if command == 'stop':
        break
    number = int(command)
    if number < 0:
        print("Number is negative.")
    elif number == 1:
        sum_non_primes += 1
    elif number > 1:
            flag = True
            for i in range(2, number):
                if number % i == 0:
                    sum_non_primes += number
                    flag = False
                    break
            if flag:
                    sum_primes += number

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")

# def is_prime(number):
#     flag = True
#     if number == 0 or number == 1:
#         flag = False
#     elif number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 flag = False
#                 break
#     return flag
#
# command = ''
# sum_primes = sum_non_primes = 0
# while command != 'stop':
#     command = input()
#     if command == 'stop':
#         break
#     number = int(command)
#     if number < 0:
#         print("Number is negative.")
#     elif number == 0:
#          sum_non_primes= sum_non_primes
#     else:
#         if is_prime(number):
#             sum_primes += number
#         else:
#             sum_non_primes += number
#
# print(f"Sum of all prime numbers is: {sum_primes}")
# print(f"Sum of all non prime numbers is: {sum_non_primes}")