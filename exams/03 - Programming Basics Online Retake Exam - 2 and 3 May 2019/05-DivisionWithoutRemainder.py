# Задача 4. Деление без остатък
# Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 се делят без остатък на 2, друг
# процент p2 се делят без остатък на 3, друг процент p3 се делят без остатък на 4. Да се напише програма,
# която изчислява и отпечатва процентите p1, p2 и p3.
# Пример: имаме n = 10 числа: 680, 2, 600, 200, 800, 799, 199, 46, 128, 65. Получаваме следното разпределение
# и визуализация:
#
# Деление без
# остатък на:       Числа в диапазона                Брой числа     Процент
#
# 2                  680, 2, 600, 200, 800, 46, 128           7     p1 = 7.0 / 10 * 100 = 70.00%
# 3                 600                                       1     p2 = 1 / 10 * 100 = 10.00%
# 4                 680, 600, 200, 800, 128                   5     p3 = 5 / 10 * 100 = 50.00%
# Вход
# На първия ред от входа стои цялото число n (1 ≤ n ≤ 1000) – брой числа.
# На следващите n-на брой реда стои по едно цяло число в интервала [1…1000] – числата които да бъдат
# проверени на колко се делят.
# Изход
# Да се отпечатат на конзолата 3 реда, всеки от които съдържа процент между 0% и 100%, с точност две цифри
# след десетичната точка, например 25.00%, 66.67%, 57.14%.
# • На първият ред – процентът на числата които се делят на 2
# • На вторият ред – процентът на числата които се делят на 3
# • На третият ред – процентът на числата които се делят на 4

def percentage(part, whole):
    return 100 * float(part) / float(whole)


div2 = 0
div3 = 0
div4 = 0

nums = int(input())
for num in range(nums):
    entry = int(input())
    if entry % 2 == 0:
        div2 += 1
    if entry % 3 == 0:
        div3 += 1
    if entry % 4 == 0:
        div4 += 1

print(f"{percentage(div2, nums):.2f}%")
print(f"{percentage(div3, nums):.2f}%")
print(f"{percentage(div4, nums):.2f}%")