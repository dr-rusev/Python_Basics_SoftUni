chicken_number = int(input())
fish_number = int(input())
veget_number = int(input())
meal_price = chicken_number * 10.35 + fish_number * 12.40 + veget_number * 8.15
desert_price = meal_price * 0.2
total_price = meal_price + desert_price
order_price = total_price + 2.50
print(f'{order_price:.2f}')
