#
# Периметър и лице на кръг
# Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг / окръжност
# с радиус r, като форматирате изхода в следния вид: \
# "<calculated area>"
# "<calculated parameter>".
# Форматирайте изходните данни до втория знак след десетичната запетая.
import math

r = float(input())

area = math.pi * (r*r)
perimeter = (r*2) * math.pi

print(f"{area:.2f}")
print(f"{perimeter:.2f}")
