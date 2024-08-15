# Курсът "Train the trainers" е към края си и финалното оценяване наближава.
# Вашата задача е да помогнете на журито, което ще оценява презентациите, като напишете програма,
# в която да изчислява средната оценка от представянето на всяка една презентация от даден студент,
# а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата
# "Student's final assessment is {среден успех от всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.
# Вход	Изход	Обяснения
# 2
# While-Loop
# 6.00
# 5.50
# For-Loop
# 5.84
# 5.66
# Finish	While-Loop - 5.75.
# For-Loop - 5.75.
# Student's final assessment is 5.75.	2 – броят на хората в журито следователно ще получаваме по 2 оценки на презентация.
# (6.00 + 5.50) / 2 = 5.75
# (5.84 + 5.66) / 2 = 5.75
# (6.00 + 5.50 + 5.84 + 5.66) / 4 = 5.75
number_of_jury = int(input())
presentation =''
total_score = 0
presentation_counter = 0
while presentation != 'Finish':
    presentation = input()
    if presentation == 'Finish':
        break

    presentation_score = 0
    for i in range(1, number_of_jury + 1):
        i = float(input())
        presentation_score += i
        presentation_counter += 1

    print(f"{presentation} - {presentation_score / number_of_jury:.2f}.")
    total_score += presentation_score

print(f"Student's final assessment is {total_score / presentation_counter:.2f}.")


