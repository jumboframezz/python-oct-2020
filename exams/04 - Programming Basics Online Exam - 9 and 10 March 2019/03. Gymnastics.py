# Художествена гимнастика
# На световно първенство по художествена гимнастика три от държавите се изявяват като лидери в
# класирането (Русия, България, Италия). Вашата задача е да изчислите каква е оценката дадена от журито за
# конкретно съчетание, като знаете държавата, която е играла и с кой уред е играла - лента, обръч или въже. За
# съчетанието си, отбора е получил две оценки: оценка за трудност и оценка за изпълнение на съчетанието,
# като крайната оценка е сбор на двете оценки. В таблицата са показани какви оценки за трудност и
# изпълнение са получили ансамблите за всеки един уред.
# Уред	              Русия	            България	            Италия
# Лента(ribbon)	Трудност: 9.100         Трудност: 9.600         Трудност: 9.200
#               Изпълнение: 9.400       Изпълнение: 9.400       Изпълнение: 9.500
#
# Обръч(hoop)	Трудност: 9.300         Трудност: 9.550         Трудност: 9.450
#               Изпълнение: 9.800       Изпълнение: 9.750       Изпълнение: 9.350
#
# Въже(rope)	Трудност: 9.600         Трудност: 9.500         Трудност: 9.700
#               Изпълнение: 9.000       Изпълнение: 9.400       Изпълнение: 9.150
# Напишете програма, която изчислява каква е оценката на дадена държава за определен уред и колко
# процента не им достигат, за да имат максималната оценка, която е 20.
# Вход
# Входът се чете от конзолата и се състои от два реда:
# • Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# • Втори ред – уред - текст ("ribbon", "hoop" или "rope")
# Изход
# На конзолата трябва да се отпечатат два реда:
# • Първи ред: "The team of {държава} get {обща оценка} on {уред}."
# • Втори ред: "{процентът, който не им достига до максималния брой точки}%"
# Общата оценка да бъде форматирана до третата цифра след десетичния знак, а процентът да бъде
# форматиран до втората цифра след десетичния знак.

score_severity = {"ribbon": {"Russia": 9.100, "Bulgaria": 9.600, "Italy": 9.200},
                  "hoop": {"Russia": 9.300, "Bulgaria": 9.550, "Italy": 9.450},
                  "rope": {"Russia": 9.600, "Bulgaria": 9.500, "Italy": 9.700}
                  }

score_performance = {"ribbon": {"Russia": 9.400, "Bulgaria": 9.400, "Italy": 9.500},
                  "hoop": {"Russia": 9.800, "Bulgaria": 9.750, "Italy": 9.350},
                  "rope": {"Russia": 9.000, "Bulgaria": 9.400, "Italy": 9.150}
                  }

country = input()
instrument = input()

total_score = score_severity[instrument][country] + score_performance[instrument][country]
missed_score = 20 - total_score
missed_percent = missed_score / 20 * 100

print(f"The team of {country} get {total_score:.3f} on {instrument}.")
print(f"{missed_percent:.2f}%")
