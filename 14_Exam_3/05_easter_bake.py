cakes = int(input())
flour = 750
sugar = 950
total_flour, total_sugar = 0, 0
max_sugar, max_flour = 0, 0

from math import ceil

for cake in range(cakes):

    current_sugar = int(input())  # цяло число в интервала [1 … 10000]
    total_sugar += current_sugar
    if current_sugar > max_sugar:
        max_sugar = current_sugar

    current_flour = int(input())  # цяло число в интервала [1 … 10000]
    total_flour += current_flour
    if current_flour > max_flour:
        max_flour = current_flour

print(f"Sugar: {ceil(total_sugar / sugar)}")
print(f"Flour: {ceil(total_flour / flour)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
