# Басейн с обем V има две тръби от които се пълни. Всяка тръба има определен дебит
# (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма,
# която изкарва състоянието на басейна, в момента, когато работникът се върне.
# Вход
# От конзолата се четат четири реда:
# •	Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
# •	Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
# •	Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
# •	Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]
# Изход
# Да се отпечата на конзолата едно от двете възможни състояния:
# •	До колко се е запълнил басейна и коя тръба с колко процента е допринесла.
# o	"The pool is {запълненост на басейна в проценти}% full. Pipe 1: {процент вода от първата тръба}%.
# Pipe 2: {процент вода от втората тръба}%."
# Aко басейнът се е препълнил – с колко литра е прелял за даденото време.
# o	"For {часовете, които тръбите са пълнили вода} hours the pool overflows with {литрите вода в повече} liters."

volume = int(input())
debit_p1 = int(input())
debit_p2 = int(input())
hours = float(input())  # [1.0…24.00]

vol_p1 = debit_p1 * hours
vol_p2 = debit_p2 * hours
vol_common = vol_p1 + vol_p2

if vol_common <= volume:
    fill_pool = (vol_common / volume) * 100
    fill_p1 = (vol_p1 / vol_common) * 100
    fill_p2 = (vol_p2 / vol_common) * 100
    print(
        "The pool is " + f'{fill_pool:.2f}' + "% full. Pipe 1: "
        + f'{fill_p1:.2f}' + "%. Pipe 2: " + f'{fill_p2:.2f}' + "%")

else:
    print("For " f'{hours}' + " hours" + " the pool overflows with "
          + f'{vol_common - volume:.2f}' + " liters.")
