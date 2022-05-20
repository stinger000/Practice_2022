# Цикл for
# for var in iterable:
# var - переменная
# iterable - то, что мы перебираем

# range - создает диапазон чисел
n = 10
for i in range(n):
    print(i)


print('')

start = 5
stop = 10
for i in range(start, stop):
    print(i)

print('')

start = 5
stop = 10
step = 2
for i in range(start, stop, step):
    print(i)

# цикл for можно проводить по любому итерируемому объекту

students = ["Ананас", "Руслан", "Алексей", "Кокос"]

for student in students:
    print(f"{student} отчислен")

print(students)

for i in range(len(students)):
    students[i] = ""

print(students)



