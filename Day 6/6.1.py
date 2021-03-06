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

def print_students(students):
    i = 0
    while i < len(students):
        print(students[i])
        i += 1

# Определение размера списка

students_count = len(students) # Количество студентов (размер списка)

# Вывод всех элементов из списка
print_students(students)

# Изменения элементов массива
student_to_dismiss_idx = 1  # Индекс элемента, который будет изменен
new_student_name = "Ананас"  # Новое значение
print(f"Студент {students[student_to_dismiss_idx]}, его место занял {new_student_name}")
students[student_to_dismiss_idx] = new_student_name

print_students(students)

sep()
# Добавление элементов
students.append("Бычков")

print_students(students)

sep()
# Удаление элементов - метод 1
del students[0]

print_students(students)

sep()
# Удаление элементов - метод 2
students.remove("Ананас")
print_students(students)

# students.remove("Кокос")  # Error