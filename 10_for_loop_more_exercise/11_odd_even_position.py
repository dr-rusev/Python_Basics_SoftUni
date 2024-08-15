# Напишете програма, която чете n-на брой числа, въведени от потребителя,
# и пресмята сумата, минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.
import sys
odd_sum = 0
even_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_min = sys.maxsize
even_max = - sys.maxsize

numbers = int(input())

if numbers == 0:
    print("OddSum=0.00,")
    print("OddMin=No,")
    print("OddMax=No,")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")

elif numbers == 1:
    number = int(input())

    print(f"OddSum={number:.2f},")
    print(f"OddMin={number:.2f},")
    print(f"OddMax={number:.2f},")
    print("EvenSum=0.00,")
    print("EvenMin=No,")
    print("EvenMax=No")

else:
    for i in range(1, numbers + 1):
        number = float(input())
        if i % 2 == 0:
            even_sum += number
            if number < even_min:
               even_min = number
            if number >= even_max:
                even_max = number
        else:
            odd_sum += number
            if number < odd_min:
                odd_min = number
            if number >= odd_max:
                odd_max = number

    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")

