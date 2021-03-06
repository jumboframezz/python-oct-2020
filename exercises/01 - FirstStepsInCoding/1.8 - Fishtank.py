
# * Аквариум
# За рождения си ден Любомир получил аквариум с формата на паралелепипед. Трябва да се пресметне колко литра
# вода ще събира аквариума, ако се знае, че определен процент от вместимостта му е заета от пясък, растения, нагревател
# и помпа. Размерите му – дължина, широчина и височина в сантиметри ще бъдат въведени от конзолата.
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.
# Да се напише програма, която изчислява литрите вода, която са необходими за напълването на аквариума.
# Вход
# От конзолата се четат 4 реда:
# Дължина в см – цяло число
# Широчина в см – цяло число
# Височина в см – цяло число
# Процент зает обем – реално число
# Изход
# Да се отпечата на конзолата едно число:
# литрите вода, които ще  събира аквариума.
# Примерен вход
# 85
# 75
# 47
# 17
#
# изход
# 248.68875

# Обяснения
# Изчисляваме обем на аквариум:
# обем на аквариум= 85*75*47=299625 см3
# общо литри, които ще събере: 299625 * 0.001=299.625 литра
# процент: 17*0.01=0.17
# литрите, които ще трябват : 299.625*(1-0.17) = 248.68875 литра


length = int(input())
width =  int(input())
height = int(input())
percent = float(input())
volume = length * width * height
volume_ltr = volume / 1000

volume_ltr -= volume_ltr * (percent*0.01)
print(volume_ltr)
