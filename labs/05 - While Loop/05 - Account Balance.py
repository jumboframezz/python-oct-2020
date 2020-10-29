# 5.	Баланс по сметка
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката до получаване на команда “NoMoreMoney”.
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!" и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката закръглена до втория знак
# след десетичната запетая.


in_text = input()
account = 0

while in_text != "NoMoreMoney":

    deposit = float(in_text)

    if deposit < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {deposit:.2f}")
    account += float(deposit)
    in_text = input()

print(f"Total: {account:.2f}")