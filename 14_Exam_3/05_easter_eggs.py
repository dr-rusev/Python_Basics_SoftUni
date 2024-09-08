number_of_eggs = int(input())
red_total, orange_total = 0, 0
blue_total, green_total = 0, 0

for egg in range(number_of_eggs):
    egg_colour = input()

    if egg_colour == "red":
        red_total += 1

    elif egg_colour == "orange":
        orange_total += 1

    elif egg_colour == "blue":
        blue_total += 1

    elif egg_colour == "green":
        green_total += 1

eggs_colour_total = red_total
eggs_colour_name = "red"

if orange_total > eggs_colour_total:
    eggs_colour_total = orange_total
    eggs_colour_name = "orange"

if blue_total > eggs_colour_total:
    eggs_colour_total = blue_total
    eggs_colour_name = "blue"

if green_total > eggs_colour_total:
    eggs_colour_total = green_total
    eggs_colour_name = "green"

print(f"Red eggs: {red_total}")
print(f"Orange eggs: {orange_total}")
print(f"Blue eggs: {blue_total}")
print(f"Green eggs: {green_total}")
print(f"Max eggs: {eggs_colour_total} -> {eggs_colour_name}")

# egg_colored_numbers = int(input())
#
# red = 0
# orange = 0
# blue = 0
# green = 0
#
# for egg in range(egg_colored_numbers):
#
#     color = input()
#
#     if color == 'red':
#         red += 1
#
#     elif color == 'orange':
#         orange += 1
#
#     elif color == 'blue':
#         blue += 1
#
#     elif color == 'green':
#         green += 1
#
# max_color = 'orange'
# max_number = orange
#
# if red > max_number:
#     max_number = red
#     max_color = 'red'
#
# if green > max_number:
#     max_number = green
#     max_color = 'green'
#
# if blue > max_number:
#     max_number = blue
#     max_color = 'blue'
#
# print(f'Red eggs: {red}')
# print(f'Orange eggs: {orange}')
# print(f'Blue eggs: {blue}')
# print(f'Green eggs: {green}')
# print(f'Max eggs: {max_number} -> {max_color}')
