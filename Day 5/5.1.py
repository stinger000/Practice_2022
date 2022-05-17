# Введение в функции (попытка номер 2)

# Как выглядит определение функции
def funck_name(param):
    ...  # Тело функции
    return 0


result = funck_name(1)  # Вызов функции
result1 = funck_name(1)  # Ещё один

# Простейшая функция, считающая сумму

def calculate_sum(a: float, b: float) -> float: # Указывает тип возвращаемого значения
    return a + b

c = a + b
c = calculate_sum(a, b)