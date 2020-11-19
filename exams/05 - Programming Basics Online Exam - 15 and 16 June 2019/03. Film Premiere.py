# Филмова премиера
# За предстояща премиера на три известни продукции, местно кино ви наема да напишете софтуер, който да изчислява
# цената, която клиентите трябва да заплатят, според филма и пакета, който са избрали.
# 	        John Wick	        Star Wars	        Jumanji
# Напитка	12 лв./бр.	        18 лв. /бр.	        9 лв. /бр.
# Пуканки	15 лв. /бр.	        25 лв. /бр.	        11 лв. /бр.
# Меню	    19 лв. /бр.	        30 лв. /бр.	        14 лв. /бр.
# Напишете програма, която изчислява цената, която трябва да се заплати, като имате в предвид следните отстъпки:
# •	При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
# •	При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - прожекция - текст с възможности"John Wick", "Star Wars" или "Jumanji"
# •	Втори ред - пакет за филм - текст  с възможности "Drink", "Popcorn" или "Menu"
# •	Трети ред - брой билети - цяло число в интервала [1… 30]
# Изход
# На конзолата трябва да се отпечата един ред:
# "Your bill is {крайна цена} leva."
# Цената да бъде закръглена до втората цифра след десетичния знак.

prices = {"Drink": {"John Wick": 12, "Star Wars": 18, "Jumanji": 9},
          "Popcorn": {"John Wick": 15, "Star Wars": 25, "Jumanji": 11},
          "Menu": {"John Wick": 19, "Star Wars": 30, "Jumanji": 14}}

movie = input()
purchase = input()
tickets = int(input())

price = prices[purchase][movie] * tickets
if movie == "Star Wars" and tickets >= 4:
    price *= 0.7
elif movie == "Jumanji" and tickets == 2:
    price *= 0.85

print(f"Your bill is {price:.2f} leva.")