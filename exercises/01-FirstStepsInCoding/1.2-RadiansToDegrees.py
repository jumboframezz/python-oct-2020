
# Конзолен конвертор: от радиани в градуси
# Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).  Принтирайте получените градуси
# като цяло число използвайки math.floor.
# Използвайте формулата: градуси = радиани * 180 / π.
# Числото π в Python може да достъпите чрез модула math. За да ползвате функционалността му, първо
# трябва да включите констатата pi.
# ￼
# Aко използвате първия вариант, в програмата ви методът ще бъде достъпен посредством кода math.pi,
# ако използвате втория – само pi. Може да упражните и двата варианта.

#from math import pi
import math
radians = float(input())
degrees = radians *180 / math.pi

print(math.floor(degrees))