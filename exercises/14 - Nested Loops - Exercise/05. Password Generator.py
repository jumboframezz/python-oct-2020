#
# Генератор за пароли
# Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред всички
# възможни  пароли, които се състоят от следните 5 символа:
# Символ 1: цифра от 1 до n;
# Символ 2: цифра от 1 до n;
# Символ 3: малка буква измежду първите l букви на латинската азбука;
# Символ 4: малка буква измежду първите l букви на латинската азбука;
# Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
# Вход
# Входът се чете от конзолата и се състои от две цели числа n и l, по едно на ред.
# Изход
# На конзолата трябва да се отпечатат всички пароли по азбучен ред, разделени с интервал.
# Вход          Изход
# 4             11aa2 11ab2 11ac2 11ad2 11ba2 11bb2 11bc2 11bd2 11ca2 11cb2 11cc2 11cd2 11da2 11db2 11dc2 11dd2
# 2
#
# 3             11aa2 11aa3 12aa3 21aa3 22aa3
# 1


n = int(input())
l = int(input())
alpha_start = ord("a")
ii = ""
i = ""
last_digit = ""
for i in range(1, n + 1):
    for ii in range(1, n + 1):
        for first_letter in range(alpha_start, alpha_start + l + 2 ):
            for second_letter in range(alpha_start, alpha_start+l + 2):
                    #for last_digit in range(2, n):
                    # if last_digit > i and last_digit > ii:
                print(f"{i}{ii}{chr(first_letter)}{chr(second_letter)}{last_digit}", end=" ")
