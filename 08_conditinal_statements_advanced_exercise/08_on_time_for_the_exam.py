# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или
# до половин час преди това. Ако е пристигнал по-рано повече от 30 минути, той е подранил.
# Ако е дошъл след часа на изпита, той е закъснял. Напишете програма, която прочита време
# на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# На първия ред отпечатайте:
# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.
# 11:30 - 12:29 -> || diff_hors // 60, diff_min % 60
# exam_hours = int(input())
# exam_minutes = int(input())
# arrival_hours = int(input())
# arrival_minutes = int(input())
#
# total_exam_min = exam_hours * 60 + exam_minutes
# total_arrival_min = arrival_hours * 60 + arrival_minutes
# hours_left = 0
# min_left = 0
#
# diff = abs(total_exam_min - total_arrival_min)
#
# if total_arrival_min > total_exam_min:
#     print("Late")
#     if diff >= 60:
#         hours_left = diff // 60
#         min_left = diff % 60
#         if min_left < 10:
#             print(f"{hours_left}:0{min_left} hours after the start")
#         else:
#             print(f"{hours_left}:{min_left} hours after the start")
#     else:
#         print(f"{diff} minutes after the start")
# elif total_arrival_min == total_exam_min:
#     print("On time")
#
# elif total_arrival_min < total_exam_min:
#     if diff <= 30:
#         print("On time")
#         print(f"{diff} minutes before the start")
#     else:
#         if diff >= 60:
#             hours_left = diff // 60
#             min_left = diff % 60
#             if min_left < 10:
#                 print("Early")
#                 print(f"{hours_left}:0{min_left} hours before the start")
#             else:
#                 print("Early")
#                 print(f"{hours_left}:{min_left} hours before the start")
#         else:
#             print("Early")
#             print(f"{diff} minutes before the start")

hour_exam = int(input())
minute_exam = int(input())

hour_arrival = int(input())
minute_arrival = int(input())

total_min_exam = hour_exam * 60 + minute_exam
total_min_arrival = hour_arrival * 60 + minute_arrival

diff = abs(total_min_exam - total_min_arrival)

hrs = diff // 60
mins = diff % 60

status = ""
when = "before the start"
time = f"{hrs}:{mins:02d} hours"

if 0 <= total_min_exam - total_min_arrival <= 30:
    status = "On time"

elif total_min_arrival < total_min_exam:
    status = "Early"

elif total_min_arrival > total_min_exam:
    status = "Late"
    when = "after the start"


if diff < 60:
    time = f"{diff} minutes"

print(status)
if diff:
    result = f"{time} {when}"
    print(result)