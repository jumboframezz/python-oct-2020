
# Задължителна литература
# За лятната ваканция в спикъка със задължителна литература на Жоро има определен брой книги, но Жоро предпочита
# да играе с приятели навън. Вашата задача е да помогнете на Жоро да изчисли колко часа на ден трябва да отделя, за да
# прочете необходимата литература, но и да прекарва максимално време навън.
# Вход
# От конзолата се четат 3 реда:
# Брой страници в текущата книга – цяло число;
# Страници, които може да прочита за 1 час – цяло число;
# Броя на дните, за които трябва да прочете книгата – цяло число;
# Изход
# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
# 1. изчисляваме общото време за четене на книгата: 212 / 20 = 10.6 часа
# 2. получения резултат делим на броя дни, за да получим необходимите часове на ден: 10.6 часа / 2 дни = 5.3 часа на ден



book_pages = int(input())
pages_per_hour = int(input())
num_days = int(input())

book_time = book_pages / pages_per_hour
days_needed = book_time /  num_days
print (days_needed)