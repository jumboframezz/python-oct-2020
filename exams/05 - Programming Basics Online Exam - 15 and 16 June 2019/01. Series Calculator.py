# Калкулатор за сериали
# Напишете програма, която изчислява колко време ще ви отнеме да изгледате всички епизоди на един сериал в минути.
# Ще разполагате с брой сезони, брой епизоди на сезон и времетраене на един епизод. Във всеки епизод има реклами,
# които са с продължителност 20% от времето на един епизод. Също така знаете, че всеки сезон завършва със специален
# епизод, който е с 10м по-дълъг от обичайното.
# Вход
# От конзолата се четат 4 реда:
#   •	Име на сериал - текст
#   •	Брой сезони – цяло число в диапазона [1… 10]
#   •	Брой епизоди  – цяло число в диапазона [10… 80]
#   •	Времетраене на обикновен епизод без рекламите – реално число в диапазона [40.0… 65.0]
# Изход
# Да се отпечата на конзолата времето, необходимо за изглеждане на всички епизоди, закръглено до най-близкото
# цяло число надолу в следния формат:
# "Total time needed to watch the {име на сериал} series is {време} minutes."
import math

show_name = input()
seasons = int(input())
episodes = int(input())
duration = int(input())

total_time = seasons * episodes * duration
total_time *= 1.2
total_time += seasons * 10

print(f"Total time needed to watch the {show_name} series is {math.floor(total_time)} minutes.")
