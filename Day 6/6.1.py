# Введение в структуры данных

# List (список) - структура для хранения данных

students = ["Иван", "Русланбек", "Максим", "Дмитрий"]

print(students[0])  # Иван
print(students[1])  # Русланбек

smartest_student = students[1]
print(f"{smartest_student=}")

# Операция обращения по индексу - опасная
# print(students[4])  # Выведет ошибку

def sep():
    print("-"*120)
sep()

# Определение размера списка

students_count = len(students) # Количество студентов (размер списка)

# Вывод всех элементов из списка
i = 0
while i < students_count:
    print(students[i])
    i += 1

# Изменения элементов массива
student_to_dismiss_idx = 1
new_student_name = "Ананас"
print(f"Студент {students[student_to_dismiss_idx]}, его место занял {new_student_name}")
students[student_to_dismiss_idx] = new_student_name

i = 0
while i < students_count:
    print(students[i])
    i += 1

