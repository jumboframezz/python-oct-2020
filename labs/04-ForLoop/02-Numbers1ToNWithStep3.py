
# Числата от 1 до N през 3
# Напишете програма, която чете число n, въведено от потребителя, и отпечатва
# числата от 1 до n през 3 (със стъпка 3).


n = int(input())

for num in range(1, n+1, 3):
    print(num)