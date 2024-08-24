tax_per_year = int(input())

sneakers = 0.6 * tax_per_year

equipment = 0.8 * sneakers

ball = 0.25 * equipment

accessories = 0.2 * ball

total_cost = tax_per_year + sneakers + equipment + ball + accessories

print(f"{total_cost:.2f}")
