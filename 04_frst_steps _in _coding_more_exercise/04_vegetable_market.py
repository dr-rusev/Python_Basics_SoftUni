# Градинар продавал реколтата от градината си на зеленчуковата борса.
# Продава зеленчуци за N лева на килограм и плодове за M лева за килограм.
# Напишете програма, която да пресмята приходите от реколтата в евро
# ( ако приемем, че едно евро е равно на 1.94лв).
# От конзолата се четат 4 числа, по едно на ред:
# •	Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
# •	Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
# •	Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
# •	Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]
# Да се отпечата на конзолата едно число: приходите от всички плодове и зеленчуци в евро.
# Резултата да се форматира до втория знак след десетичния разделител.
price_veg = float(input())
price_fru = float(input())
quantity_veg = int(input())
quantity_fru = int(input())
total_veg = price_veg * quantity_veg
total_fru = price_fru * quantity_fru
total_euro = (total_veg + total_fru) / 1.94
print(f'{total_euro:.2f}')