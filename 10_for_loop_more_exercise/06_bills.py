# Напишете програма която да пресмята средният разход за месец на семейство
# за даден период време. За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Изход
# Да се отпечата на конзолата 5 реда:
# •	1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# •	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до втория знак след запетаята.
water_bill = 20
internet_bill = 15
water_bill_all = 0
internet_bill_all = 0
electricity_bll_all = 0
other_bills_all = 0

months = int(input())
for i in range(1, months + 1):
    electricity_bill = float(input())
    electricity_bll_all += electricity_bill
    other_bills_all += (electricity_bill + water_bill + internet_bill) * 1.2
    water_bill_all += 20
    internet_bill_all += 15

average_bills = (water_bill_all + internet_bill_all + electricity_bll_all + other_bills_all) / months
print(f"Electricity: {electricity_bll_all:.2f} lv")
print(f"Water: {water_bill_all:.2f} lv")
print(f"Internet: {internet_bill_all:.2f} lv")
print(f"Other: {other_bills_all:.2f} lv")
print(f"Average: {average_bills:.2f} lv")

