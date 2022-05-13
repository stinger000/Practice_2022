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
