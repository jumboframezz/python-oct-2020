# Задача 2. Великденско парти
# Деси има рожден ден на Великден и иска да организира парти за своите приятели. Тя знае какъв е броят
# гости, които иска да покани и колко е кувертът за всеки гост. От броя гости зависи и каква отстъпка ще
# получи за куверта за един човек.
# Ако покани:
# • Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
# • Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
# • Над 20 човека -> 25 % отстъпка от куверта за един човек
# Деси трябва да предвиди и закупуването на торта за партито. Цената на тортата е 10% от бюджета на Деси.
# Напишете програма, която изчислява дали бюджетът на Деси ще и е достатъчен за партито.
# Вход
# От конзолата се четат 3 реда:
# 1. Брой гости – цяло число в интервала [1...99]
# 2. Цена на куверт за един човек – реално число в интервала [0.00 … 99.00]
# 3. Бюджетът на Деси – реално число в интервала [0.00 … 9999.00]
# Изход
# На конзолата да се отпечата един ред:
# • Ако бюджетът е достатъчен:
# o "It is party time! {останали пари} leva left."
# • Ако бюджетът не е достатъчен:
# o "No party! {недостигащи пари} leva needed."
# Резултатът да бъде форматиран до втория знак след десетичната запетая.
# URL to check: https://judge.softuni.bg/Contests/Practice/Index/1637#2

num_guests = int(input())
invitation_price = float(input())
budget = float(input())

if num_guests >= 10 and num_guests <= 15:
    invitation_price -= invitation_price * 0.15
elif num_guests > 15 and num_guests <= 20:
    invitation_price -= invitation_price * 0.20
elif num_guests > 20:
    invitation_price -= invitation_price * 0.25

price = num_guests * invitation_price

cake_price = budget * 0.1
sub_total = cake_price + (invitation_price * num_guests)
left = budget - sub_total

if left >= 0:
    print(f"It is party time! {left:.2f} leva left.")
else:
    left *= -1
    print(f"No party! {left:.2f} leva needed.")
