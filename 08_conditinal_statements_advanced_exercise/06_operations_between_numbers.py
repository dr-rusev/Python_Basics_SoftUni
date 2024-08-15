# Напишете програма, която чете две цели числа (N1 и N2) и оператор,
# с който да се извърши дадена математическа операция. Възможните операции са: Събиране(+),
# Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%). При събиране, изваждане и умножение
# на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен.
# При обикновеното деление - резултата. При модулното деление - остатъка.
# Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на нула не се дели.
# В този случай трябва да се отпечата специално съобщениe.
# Вход
# От конзолата се прочитат 3 реда, въведени от потребителя:
# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако операцията е събиране, изваждане или умножение:
# o	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# •	Ако операцията е деление:
# o	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# •	Ако операцията е модулно деление:
# o	"{N1} % {N2} = {остатък}"
# •	В случай на деление с 0 (нула):
# o	"Cannot divide {N1} by zero"
# n1 = int(input())
# n2 = int(input())
# operator = input() # "+", "-", "*", "/", "%"
# if operator == '+':
#     sbor = n1 + n2
#     if sbor % 2 == 0: print(f"{n1} + {n2} = {sbor} - even")
#     else: print(f"{n1} + {n2} = {sbor} - odd")
# if operator == '-':
#     diff = n1 - n2
#     if diff % 2 == 0: print(f"{n1} - {n2} = {diff} - even")
#     else: print(f"{n1} - {n2} = {diff} - odd")
# if operator == '*':
#     mult = n1 * n2
#     if mult % 2 ==0: print(f"{n1} * {n2} = {mult} - even")
#     else: print(f"{n1} * {n2} = {mult} - odd")
# if operator == '/':
#     if n2 == 0:
#         print(f"Cannot divide {n1} by zero")
#     else:
#         div = n1 / n2
#         div = f'{div:.2f}'
#         print(f"{n1} / {n2} = {div}")
# if operator == '%':
#     if n2 == 0:
#         print(f"Cannot divide {n1} by zero")
#     else:
#         mod = n1 % n2
#         print(f"{n1} % {n2} = {mod}")

n1 = int(input())
n2 = int(input())
result = 0
even_or_odd = "even"
operator = input() # "+", "-", "*", "/", "%"

if operator == '+':
    result = n1 + n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} + {n2} = {result} - {even_or_odd}")

elif operator == '-':
    result = n1 - n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} - {n2} = {result} - {even_or_odd}")

elif operator == '*':
    result = n1 * n2
    if result % 2 != 0:
        even_or_odd = "odd"
    print(f"{n1} * {n2} = {result} - {even_or_odd}")

elif (operator == '/' or operator == '%') and n2 == 0:
    print(f"Cannot divide {n1} by zero")

elif operator == '/':
    result = n1 / n2
    print(f"{n1} / {n2} = {result:.2f}")

elif operator == '%':
    result = n1 % n2
    print(f"{n1} % {n2} = {result}")
