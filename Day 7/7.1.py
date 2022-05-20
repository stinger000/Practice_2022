# Списки - продолжение

# Базовые операции

# 1 - обращение к элементу
students = ["Иван", "Ананас", "Ананас"]
print(students[0])

# 2 - получение размера
students_count = len(students)

# 3 - изменение элементов
students[0] = "Русланбек"

# 4 - удаление элемента
del students[0]  # Удаление по индексу
students.remove("Ананас")  # Удаление по значению
# Метод remove удаляет только первый найденный элемент
print(students)

# 5 - добавление элементов
students.append("Студент 1")

# 6 - слияние списков
group_23 = ["Ананас", "Кокос"]
group_24 = ["Страус", "Петух"]

new_group = group_23 + group_24
print(new_group)

# 7 - расширение списка
noobies = ["Картошка", "Огурчик Рик"]
new_group.extend(noobies)
print(new_group)
students = new_group
# 8 - списковые срезы
# new_list = my_list[start:stop:step]
# start - начальный элемент
# stop - конечный элемент (не включая)
# step - шаг
print(f"{students[0:3] = }")  # Первые три элемента
print(f"{students[:3] = }")  # Первые три элемента
print(f"{students[2:4] = }")  # Со второго по четвертый
print(f"{students[2:] = }")  # Со второго до конца
print(f"{students[::2] = }")  # Каждый второй элемент
print(f"{students[::-1] = }")  # Элементы в обратном порядке