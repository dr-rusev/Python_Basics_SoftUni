# film_name = ''
# student, standard, kid = 0, 0, 0
#
# while film_name != 'Finish':
#
#     film_name = input()
#     if film_name == 'Finish':
#         break
#
#     free_slots = int(input())
#     total_free_slots = free_slots
#
#     while free_slots:
#         ticket_type = input()
#
#         if ticket_type == 'End':
#             break
#
#         free_slots -= 1
#
#         if ticket_type == 'student':
#             student += 1
#
#         elif ticket_type == 'standard':
#             standard += 1
#
#         elif ticket_type == 'kid':
#             kid += 1
#
#     print(f"{film_name} - {100 - free_slots / total_free_slots * 100:.2f}% full.")
#
# total = student + standard + kid
# print(f"Total tickets: {total}")
# print(f"{student / total * 100:.2f}% student tickets.")
# print(f"{standard / total * 100:.2f}% standard tickets.")
# print(f"{kid / total * 100:.2f}% kids tickets.")

student, standard, kid = 0, 0, 0
film_name = input()

while film_name != 'Finish':

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

    film_name = input()

total = student + standard + kid
print(f"Total tickets: {total}")
print(f"{student / total * 100:.2f}% student tickets.")
print(f"{standard / total * 100:.2f}% standard tickets.")
print(f"{kid / total * 100:.2f}% kids tickets.")

