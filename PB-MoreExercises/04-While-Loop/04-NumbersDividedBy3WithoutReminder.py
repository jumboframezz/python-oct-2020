# Напишете програма, която печата всички числа в интервала от 1 до 100, който се
# делят на 3 без остатък, по едно на ред.


for cnt in range (1,101):
    if cnt % 3 == 0:
        print(cnt)