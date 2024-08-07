naylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())
naylon_exp = (naylon + 2) * 1.5
paint_exp = (paint * 1.1) * 14.50
thinner_exp = thinner * 5.00
bags_exp = 0.4
materials_exp = naylon_exp + paint_exp + thinner_exp + bags_exp
labor_exp = materials_exp * 0.3 * work_hours
total_expense = materials_exp + labor_exp
print(f'{total_expense:.2f}')
