# Oт конзолата се въвеждат цените в лева на скумрията и цацата.
# Също количеството на паламуд, сафрид и миди в килограми.
# Колко пари ще са му необходими, за да плати сметката си, ако цените на борсата са:
# •	Паламуд – 60% по-скъп от скумрията
# •	Сафрид – 80% по-скъп от цацата
# •	Миди – 7.50 лв. за килограм
# От конзолата се четат 5 числа:
# •	Първи ред – цена на скумрията на килограм. Реално число в интервала [0.00…40.00]
# •	Втори ред – цена на цацата на килограм. Реално число в интервала [0.00…30.00]
# •	Трети ред – килограма паламуд. Реално число в интервала [0.00…50.00]
# •	Четвърти ред – килограма сафрид. Реално число в интервала [0.00… 70.00]
# •	Пети ред – килограма миди. Цяло число в интервала [0 ... 100]
# Да се отпечата на конзолата едно число с плаваща запетая: колко пари ще са нужни на Георги,
# за да си плати сметката.
# Числото трябва да е форматирано до вторият знак след десетичната запетая (1.2457 -> 1.25).
price_skumriq_kg = float(input())
price_caca_kg = float(input())
quantity_palamud_kg = float(input())
quantity_safrid_kg = float(input())
quantity_midi_kg = int(input())
# calculations
price_palamud_kg = price_skumriq_kg * 1.6
price_safrid_kg = price_caca_kg * 1.8
price_midi_kg = 7.50

total_cost = quantity_palamud_kg * price_palamud_kg + quantity_safrid_kg * price_safrid_kg + quantity_midi_kg * price_midi_kg

print(f'{total_cost:.2f}')