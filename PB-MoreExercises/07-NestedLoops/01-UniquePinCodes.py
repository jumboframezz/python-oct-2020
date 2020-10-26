# Тествайте решенията си в judge системата: https://judge.softuni.bg/Contests/Practice/Index/1381#0
# Уникални PIN кодове
# Да се напише програма, която генерира трицифрени PIN кодове, като цифрите на всеки PIN код са в определен интервал.
# За да бъде валиден един PIN код той трябва да отговаря на следните условия:
# Първата и третата цифра трябва да бъдат четни.
# Втората цифра трябва да бъде просто число в диапазона [2...7].
# Вход
# От конзолата се четат 3 реда:
# Горната граница на първото число - цяло число в диапазона [1...9]
# Горната граница на второто число - цяло число в диапазона [1...9]
# Горната граница на третото число - цяло число в диапазона [1...9]
# Изход
# Да се отпечатат на конзолата всички валидни трицифрени PIN кодове, чиито цифри отговарят на съответните интервали.


def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    else:
        return False


limes1 = int(input())
limes2 = int(input())
limes3 = int(input())

for num1 in range(1, limes1+1):
    if num1 % 2 == 0:
        for num2 in range(1, limes2+1):
            if prime_number(num2):
                for num3 in range(1, limes3+1):
                    if num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")