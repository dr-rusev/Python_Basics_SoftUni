# Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.
import sys
smallest = sys.maxsize
biggest = -sys.maxsize
n = int(input())
for i in range(n):
    num = int(input())
    if num < smallest:
      smallest = num
    if num > biggest:
      biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
