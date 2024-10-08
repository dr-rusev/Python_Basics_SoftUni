# Отговаряте за логистиката на различни товари. В зависимост от теглото на товара
# е нужно различно превозно средство. Цената на тон, за която се превозва товара е различна
# за всяко превозно средство:
# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар,
# както и процента на тоновете  превозвани с всяко превозно средство,
# спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).
number_loads = int(input())
weight_bus = 0
weight_truck = 0
weight_train = 0
total_load = 0
price = 0
for load in range(1, number_loads + 1):
    weight = int(input())
    if 0 <= weight <= 3:
        weight_bus += weight
        price += weight * 200

    elif 4 <= weight <= 11:
        weight_truck += weight
        price += weight * 175

    elif 12 <= weight:
        weight_train += weight
        price += weight * 120

total_loads = weight_bus + weight_truck + weight_train
avg_price = price / total_loads
bus_percent = weight_bus / total_loads * 100
truck_percent = weight_truck / total_loads * 100
train_percent = weight_train / total_loads * 100

print(f'{avg_price:.2f}')
print(f'{bus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')