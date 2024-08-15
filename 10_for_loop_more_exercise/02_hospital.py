# За даден период от време, всеки ден в болницата пристигат пациенти за преглед.
# Тя разполага първоначално със 7 лекари. Всеки лекар може да преглежда
# само по един пациент на ден, но понякога има недостиг на лекари,
# затова останалите пациенти се изпращат в други болници. Всеки трети ден,
# болницата прави изчисления и ако броят на непрегледаните пациенти е по-голям
# от броя на прегледаните, се назначава още един лекар. Като назначаването става
# преди да започне приемът на пациенти за деня.
# Напишете програма, която изчислява за дадения период броя на прегледаните и непрегледаните пациенти.
# Вход
# Входът се чете от конзолата и съдържа:
# •	На първия ред – периода, за който трябва да направите изчисления. Цяло число в интервала [1 ... 1000]
# •	На следващите редове(равни на броят на дните) – броя пациенти,
# които пристигат за преглед за текущия ден. Цяло число в интервала [0…10 000]
# Изход
# Да се отпечатат на конзолата 2 реда :
# •	На първия ред: "Treated patients: {брой прегледани пациенти}."
# •	На втория ред: "Untreated patients: {брой непрегледани пациенти}."
# treated_patients = 0
# untreated_patients = 0
# doctors = 7
# days = int(input())
# for day in range(1, days + 1):
#     patients_per_day = int(input())
#     if day % 3 == 0:
#         if untreated_patients > treated_patients:
#             doctors += 1
#
#     if patients_per_day <= doctors:
#         treated_patients += patients_per_day
#     else:
#         treated_patients += doctors
#         untreated_patients += (patients_per_day - doctors)
#
# print(f'Treated patients: {treated_patients}.')
# print(f'Untreated patients: {untreated_patients}.')
period = int(input())
docs = 7
yes = 0
no = 0
if period == 0:
    exit()
for day in range(1, period + 1):
    people = int(input())
    if day % 3 == 0:
        if no > yes:
            docs += 1
    if docs >= people:
        yes += people
    else:
        yes += docs
        no += people - docs
print(f"Treated patients: {yes}.")
print(f"Untreated patients: {no}.")