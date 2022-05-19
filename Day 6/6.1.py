# Введение в структуры данных

# List (список) - структура для хранения данных

students = ["Иван", "Русланбек", "Максим", "Дмитрий"]

print(students[0])  # Иван
print(students[1])  # Русланбек

smartest_student = students[1]
print(f"{smartest_student=}")

# Операция обращения по индексу - опасная
# print(students[4])  # Выведет ошибку

# Определение размера списка

students_count = len(students) # Количество студентов (размер списка)

# Вывод всех элементов из списка
i = 0
while i < students_count:
    print(students[i])
    i += 1


