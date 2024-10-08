# Магазин за плодове през работните дни работи на следните цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	0.85	1.45	2.70	5.50	3.85
# През събота и неделя магазинът работи на по-високи цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	1.25	0.90	1.60	3.00	5.60	4.20
# Напишете програма, която чете от конзолата следните три променливи,
# въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".
fruit = input()
day = input()
quantity = float(input())
price = 0
if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
if price == 0:
    print('error')
else:
    price = price * quantity
    print(f"{price:.2f}")
