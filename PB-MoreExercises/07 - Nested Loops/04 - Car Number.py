# 4.	Номер
# Поздравления, поради вашите задълбочени знания в сферата на програмирането МВР реши да наеме точно вас за създаването
# на новата им система за генериране на специални автомобилни номера. Всеки един специален автомобилен номер се състои
# от четири числа. Условията, които разграничават специалните от обикновените номера са следните:
# •	Ако номерът започва с четна цифра, то той трябва да завършва на нечетна цифра и обратното – ако започва с нечетна,
# завършва на четна
# •	Първата цифра от номера е по-голяма от последната
# •	Сумата от втората и третата цифра трябва да е четно число
# Входа се състои от две числа - начало и край на интервал, между които трябва да се генерира всяко едно число от
# номера.
# Вход
# 1.	Първи ред - едноцифрено число - началото на интервала – цяло число в интервала [1…9]
# 2.	Втори ред - едноцифрено число - края на интервала – цяло число в интервала [1…9]
# Изход
# На конзолата трябва да се отпечатат всички специални номера, разделени с интервал.

def check_special(ds1, ds2, ds3, ds4):
    if (ds1 % 2 == 0 and ds4 % 2 != 0) or (ds1 % 2 != 0 and ds4 % 2 == 0):
        if ds1 > ds4 and (ds2 + ds3) % 2 == 0:
            return True
    return False


start_num = int(input())
end_num = int(input())

for d1 in range(start_num, end_num+1):
    for d2 in range(start_num, end_num + 1):
        for d3 in range(start_num, end_num + 1):
            for d4 in range(start_num, end_num + 1):
                if check_special(d1, d2, d3, d4):
                    print(f"{d1}{d2}{d3}{d4}", end=" ")