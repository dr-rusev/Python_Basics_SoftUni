# number = int(input())
# if number == 0 or number == 1:
#     print(f"{number} is not a prime number")
# elif number > 1:
#     flag = True
#     for i in range(2, number):
#         if number % i == 0:
#             flag = False
#             break
#     if flag:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is not a prime number")
#
# #num = int(input("Enter a number: "))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
#
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
# number = int(input())
# if number == 1:
#     print(f"{number} is not prime")
# elif number > 1:
#     flag = True
#     for i in range(2, number):
#         if number % i == 0:
#             print(f"{number} is not prime")
#             flag = False
#             break
#     if flag:
#         print(f"{number} is prime")

# How to print first n in number prime
# number = int(input())
# x = 0
# i = 2
# while x < number:
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         print(i, end = ' ')
#         x += 1
#     i += 1

# How to print primes from 1 to number
# number = int(input())
# for i in range(2, number + 1):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             break
#     if flag:
#         print(i, end=' ')

