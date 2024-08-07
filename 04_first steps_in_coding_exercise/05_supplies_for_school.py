cleaner_price_per_litter = 1.20
pen_quantity = int(input())
marker_quantity = int(input())
cleaner_quantity_litters = int(input())
discount_percents = int(input())
total = float((pen_quantity * 5.80 + marker_quantity * 7.20 + cleaner_quantity_litters * 1.2) * (1 - discount_percents / 100))
print(f'{total:.2f}')