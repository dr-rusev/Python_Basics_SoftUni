# Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN).
# Използвайте фиксиран курс между долар и лев: 1 USD = 1.79549 BGN.
# Примерен вход и изход
# вход	изход		    вход	    изход		    вход	    изход
# 22	39.50078 		100	        179.549		    12.5	    22.443625
usd = float(input())
bgn = usd * 1.79549
print(bgn)