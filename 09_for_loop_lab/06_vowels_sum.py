# Да се напише програма, която чете текст (стринг), въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:
# буква	    a	e	i	o	u
# стойност	1	2	3	4	5
word = input()
sum = 0
for char in word:
    if char == 'a':
        sum += 1
    elif char == 'e':
        sum += 2
    elif char == 'i':
        sum += 3
    elif char == 'o':
        sum += 4
    elif char == 'u':
        sum += 5
print(sum)