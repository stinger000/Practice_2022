# Ввод нескольких значений
# string = inpunt() - считывает строку целиком

# s = input("Введите координаты точки через пробел: ")
# print(int(s))  # Если ввести два числа, возникнет ошибка

# string.split() - разделяет строку

string = "1 2"
x, y = string.split()
print(f"{x=}, {y=}")
# print(x * y )  # Вызовет ошибку - нельзя перемножать строки
x, y = float(x), float(y)
print(x * y)  # Выполнится без ошибки

# Другие символы разделителя
date = "13.05.2022"
day, month, year = date.split(".")
day, month, year = int(day), int(month), int(year)
print(f"Год: {year}, месяц: {month}, день: {day}")

# Быстрый способ считать несколько чисел
# x, y = [int(x) for x in input().split()]
# print(f"{x=}, {y=}")

# Ещё один
# x, y = map(int, input().split())
# print(f"{x=}, {y=}")

# Методы строк

string = "Ооооочень длинная строка"
print(f"Строка {string=} имеет длину {len(string)}")

# Заменить подстроку в строке
string = "c++ - лучший язык в мире"
string = string.replace("c++", "Python")
print(string)

# Капс
print(string.upper())


print("-"*120)
print("Прекрасная программа")
print("Конец прекрасной программы".center(120, "-"))

# Остальные методы строк
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

string = "0123456789"
print(string[0:5])  # С нулевого по пятый (не включая)
print(string[3:6])  # С третьего по шестой
print(string[:4])   # С начала по четвертый
print(string[3:])   # С третьего до конца
print(string[::2])  # Каждый второй символ
print(string[::3])  # Каждый третий символ
print(string[::-1]) # Перевернутая строка
