# Вашата задача е да напишете програма, която да изчислява процента
# на билетите за всеки тип от продадените билети: студентски(student),
# стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Входът е поредица от цели числа и текст:
#   • На първия ред до получаване на командата "Finish" - име на филма – текст
#   • На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
#   • За всеки филм, се чете по един ред до изчерпване на свободните места в залата
#     или до получаване на командата "End":
#       o Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
#   • След всеки филм да се отпечата, колко процента от кино залата е пълна
#       "{името на филма} - {процент запълненост на залата}% full."
#   • При получаване на командата "Finish" да се отпечатат четири реда:
#       o "Total tickets: {общият брой закупени билети за всички филми}"
#       o "{процент на студентските билети}% student tickets."
#       o "{процент на стандартните билети}% standard tickets."
#       o "{процент на детските билети}% kids tickets."
# film_name = ''
# total_student_tickets = 0
# total_standard_tickets = 0
# total_kid_tickets = 0
# total_tickets = 0
# free_slots = 0
# while film_name != 'Finish':
#     film_name = input()
#     if film_name == 'Finish':
#         break
#
#     free_slots = int(input())
#     free_slots_counter = free_slots
#     student_tickets = 0
#     standard_tickets = 0
#     kid_tickets = 0
#     ticket_type = ''
#     while ticket_type != 'End' and free_slots_counter > 0:
#         ticket_type = input()
#         if ticket_type == 'End':
#             break
#         free_slots_counter -= 1
#         if free_slots_counter < 0:
#             break
#
#         if ticket_type == 'student':
#             student_tickets += 1
#             total_student_tickets += 1
#
#         elif ticket_type == 'standard':
#             standard_tickets += 1
#             total_standard_tickets += 1
#
#         elif ticket_type == 'kid':
#             kid_tickets += 1
#             total_kid_tickets += 1
#
#     film_occupancy = (student_tickets + standard_tickets + kid_tickets) / free_slots * 100
#     print(f"{film_name} - {film_occupancy:.2f}% full.")
#
# total_tickets = total_student_tickets + total_standard_tickets + total_kid_tickets
# student_occupancy = total_student_tickets / total_tickets * 100
# standard_occupancy = total_standard_tickets / total_tickets * 100
# kid_occupancy = total_kid_tickets / total_tickets * 100
#
# print(f"Total tickets: {total_tickets}")
# print(f"{student_occupancy:.2f}% student tickets.")
# print(f"{standard_occupancy:.2f}% standard tickets.")
# print(f"{kid_occupancy:.2f}% kids tickets.")


film_name = ''
student, standard, kid = 0, 0, 0

while film_name != 'Finish':

    film_name = input()
    if film_name == 'Finish':
        break

    free_slots = int(input())
    total_free_slots = free_slots

    while free_slots:
        ticket_type = input()

        if ticket_type == 'End':
            break

        free_slots -= 1

        if ticket_type == 'student':
            student += 1

        elif ticket_type == 'standard':
            standard += 1

        elif ticket_type == 'kid':
            kid += 1

    print(f"{film_name} - {100 - free_slots / total_free_slots * 100:.2f}% full.")

total = student + standard + kid
print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kids tickets.")

