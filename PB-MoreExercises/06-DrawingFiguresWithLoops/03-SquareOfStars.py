# 3.	Квадрат от звездички
# Напишете програма, която чете число n, въведено от потребителя, и чертае квадрат от n * n звездички.
# Разликата с предходната задача е, че между всеки две звездички има по един интервал.

n = int(input())

for i in range(0, n):
    for ii in range(0, n):
        print("*", end=" ")
    print("")