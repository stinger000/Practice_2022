int_var: int = 0
float_var: float = 1.5
string_var: str = "Hello"
bool_var: bool = False

int_var = 1 + 2  # сложение
int_var = 5 - 3  # вычитание
int_var = 42 * 99  # умножение
# Деление в Python:
float_var = 15 / 10  # = 1.5 (float) - обычное деление, как в реальной жизни
int_var = 15 // 10  # = 1 (int) - целочисленное деление
int_var = 15 % 10  # = 5 (int) - остаток от деления

int_var = 5 ** 2  # = 25 - возведение в степень
float_var = 2 ** 0.5  # = 1.414... - извлечение корня

import math  # импортируем библиотеку math
float_var = math.sin(5)

# Операции "на месте":
int_var += 5  # int_var = int_var + 5
int_var += 1  # инкремент, i++ как в Си не сработает

# Приведение типов:
int_var = int(2.5)  # приведение к типу int
float_var = float(42)  # приведение к типу float

# Строки в Python:

first_string = "Hello, "
second_string = "World!"

result_string = first_string + second_string  # конкатенация строк
print(result_string)

result_string = first_string * 5  # умножение строк
print(result_string)

result_string = f"{float_var=}, {math.sqrt(float_var)=:.4}"  # форматирование строк
print(result_string)

# Вывод:

print(1)
print(1, 2)
print(1, 2, "This is a string")
print("Эта строка не будет перенесена!", end="")
print("Ну, я же говорил")  # Напечатается на одной строке
print(1, 2, "This is a string", sep="\n")

# Ввод данных:

# string_var = input("Пожалуйста, введите строку: ")
# print(f"Вы ввели строку {string_var!r}")

string_var = input("Пожалуйста, введите целое число: ")
int_var = int(string_var)
print(int_var + 5)

# Поддержка кодировок Unicode

переменная = "😹"
变量 = "🐕"

def сложить(первое_число, второе_число):
    return  первое_число + второе_число

print(сложить(переменная , 变量))

"""
Задание 1
Введите имя: Сергей
Введите ваш возраст: 42
Введите год: 2024
Привет, Сергей! В 2024 году тебе будет 44 года

"""
