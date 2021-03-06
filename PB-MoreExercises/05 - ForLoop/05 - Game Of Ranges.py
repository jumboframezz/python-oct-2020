# 5. Игра на интервали
# Напишете програма, която да пресмята резултата от игра.Първо получавате число, което показва колко хода ще продължи
# играта.После за всеки ход на играта ще получавате по едно ново число.Според интервала в който попада числото се
# прибавят точки.Ако числото е отрицателно или по - голямо 50, тогава то е невалидно.В началото на играта резултата е
# 0 и на всеки ход се прибавят точки по следният начин:
#     • От 0 до 9  20 % от числото
#     • От 10 до 19  30 % от числото
#     • От 20 до 29  40 % от числото
#     • От 30 до 39  50 точки
#     • От 40 до 50  100 точки
#     • Невалидно число  резултата се дели на 2
# Освен резултата програмата трябва да изкарва статистика за проценти числав дадените интервали.
# Вход
# Входът се чете от конзолата:
#     • Първи ред - колко хода ще има по време на играта – цяло число в интервала[1...100]
#     • За всеки ход – числата, които се проверяватв кой интервал са – целичисла в интервала[-100...100]
# Изход
# Да се отпечата на конзолата 7 реда:
#     • 1ви ред: "{Краен резултат}"
#     • 2ри ред: "From 0 to 9: {процент в интервала}%"
#     • 3ти ред: "From 10 to 19: {процент в интервала}%"
#     • 4ти ред: "From 20 to 29: {процент в интервала}%"
#     • 5ти ред: "From 30 to 39: {процент в интервала}%"
#     • 6ти ред: "From 40 to 50: {процент в интервала}%"
#     • 7ми ред: "Invalid numbers: {процент в интервала}%"
# Всички числа трябва да са форматирана до вторият знак след запетаята.
def percentage(part, whole):
    return 100 * float(part) / float(whole)


turns = int(input())
counter_0 = 0
counter_10 = 0
counter_20 = 0
counter_30 = 0
counter_40 = 0
counter_wrong = 0
result = 0
for turn in range(0, turns):
    score = int(input())
    if 0 <= score <= 9:
        result += score * 0.2
        counter_0 += 1
    elif 10 <= score <= 19:
        result += score * 0.3
        counter_10 += 1
    elif 20 <= score <= 29:
        result += score * 0.4
        counter_20 += 1
    elif 30 <= score <= 39:
        result += 50
        counter_30 += 1
    elif 40 <= score <= 50:
        result += 100
        counter_40 += 1
    elif score >= 51 or score < 0:
        result = result / 2
        counter_wrong += 1

print(f"{result:.2f}")
print(f"From 0 to 9: {percentage(counter_0, turns):.2f}%")
print(f"From 10 to 19: {percentage(counter_10, turns):.2f}%")
print(f"From 20 to 29: {percentage(counter_20, turns):.2f}%")
print(f"From 30 to 39: {percentage(counter_30, turns):.2f}%")
print(f"From 40 to 50: {percentage(counter_40, turns):.2f}%")
print(f"Invalid numbers: {percentage(counter_wrong, turns):.2f}%")
