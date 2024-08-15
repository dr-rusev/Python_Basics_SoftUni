# Предстои Вело състезание за благотворителност в което участниците са разпределени
# в младша("juniors") и старша("seniors") група. Парите се набавят от таксата за участие
# на велосипедистите. Според възрастовата група и вида на трасето на което ще се провежда
# състезанието, таксата е различна:
# Група	        trail	        cross-country	        downhill	        road
# juniors	    5.50	        8	                    12.25	            20
# seniors	    7	            9.50	                13.75	            21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши),
# таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.
number_juniors = int(input())
number_seniors = int(input())
route = input()
income = 0
if route == 'trail':
    income = number_juniors * 5.50 + number_seniors * 7
elif route == 'cross-country':
    income = number_juniors * 8 + number_seniors * 9.50
elif route == 'downhill':
    income = number_juniors * 12.25 + number_seniors * 13.75
elif route == 'road':
    income = number_juniors * 20 + number_seniors * 21.50
if route == 'cross-country' and number_juniors + number_seniors >=50:
    income *= 0.75
final_income = income * 0.95
print(f"{final_income:.2f}")