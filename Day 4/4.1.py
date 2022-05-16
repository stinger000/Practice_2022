# Функции

# Простая функция без аргументов
def my_function():
    print("hello")


my_function()

# Функция с аргументами
def print_sum(x: int, y: int):
    print(f"{x=}, {y=}, {x+y = }")


print_sum(1, 2)
print_sum(3, 4)

# Возвращаемое значение функци
def reverse(string: str) -> str:
    return string[::-1]


origin_string = "Hello, world!"
reversed_string = reverse(origin_string)
print(reversed_string)

# Возврат нескольких значений из функции
def minmax(a: int, b: int, c: int) -> (int, int):
    if a > b < c:
        _min = b
    elif a > c < b:
        _min = c
    else:
        _min = a
    if a < b > c:
        _max = b
    elif a < c > b:
        _max = c
    else:
        _max = a

    return _min, _max


minimal, maximal = minmax(1, 5, 7)
print(f"{minimal=}, {maximal=}")

# Аргументы по умолчанию
def say_n_times(word: str, n=10, shout=False):
    i = 0
    while i < n:
        if shout:
            print(word.upper())
        else:
            print(word)
        i += 1

# Keyword-аргументы
say_n_times("Питон лучший", shout=True)

def minmax(a: int, b: int, c: int) -> (int, int):
    if a == b == c:
        return a, a
        print("Эта строка никогда не напечатается")
    if a > b < c:
        _min = b
    elif a > c < b:
        _min = c
    else:
        _min = a
    if a < b > c:
        _max = b
    elif a < c > b:
        _max = c
    else:
        _max = a

    return _min, _max
