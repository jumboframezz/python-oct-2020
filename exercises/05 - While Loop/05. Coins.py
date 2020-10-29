# 5. Монети
# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото, което трябва да се върне и изчислява с колко най-малко монети
# може да стане това.
# монети: 1 2 5 10 20 50 100 200 ст
# обратно:  200 100 50 20 10 5 2 1
# разлика:      100 50 30 10 5 2 1
coin_types = [200, 100, 50, 20, 10, 5, 2, 1]

change = float(input())
cents = int(change * 100)

coins = 0
counter = 0

while cents != 0:
    coins += cents // coin_types[counter]
    cents = cents % coin_types[counter]
    if counter <= 6:
        counter += 1
        
print(int(coins))