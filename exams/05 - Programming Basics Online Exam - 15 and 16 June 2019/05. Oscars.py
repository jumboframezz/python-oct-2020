# Оскари
# Поканени сте от академията да напишете софтуер, който да пресмята точките за актьор/актриса. Академията ще ви
# даде първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките, които актьора получава
# се формират от: дължината на името на оценяващия умножено по точките, които дава делено на две.
# Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне и да се отпечата, че дадения актьор е
# получил номинация.
# Вход
#   •	Име на актьора – текст
#   •	Точки от академията - реално число в интервала [2.0... 450.5]
#   •	Брой оценяващи n – цяло число в интервала[1… 20]
#       На следващите n-на брой реда:
#           o	Име на оценяващия – текст
#           o	Точки от оценяващия – реално число в интервала [1.0... 50.0]
# Изход
# Да се отпечата на конзолата един ред:
#   •	Ако точките са над 1250.5:
#       "Congratulations, {име на актьора} got a nominee for leading role with {точки}!"
#   •	Ако точките не са достатъчни:
# 	    "Sorry, {име на актьора} you need {нужни точки} more!"
# Резултатът да се форматирана до първата цифра след десетичния знак!

actor = input()
score = float(input())
jury = int(input())
for _ in range(jury):
    jury_name = input()
    jury_score = float(input())
    add_score = len(jury_name) * jury_score / 2
    score += add_score
    if score > 1250.5:
        break

if score > 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {score:.1f}!")
else:
    print(f"Sorry, {actor} you need {1250.5 - score:.1f} more!")