# Циклы
"""
Цикл while
while условие:
    тело цикла

До тех пор, пока тело условие верно будет выполняться
тело цикла
"""
# i = 0  # Начальное значение
# end = 10  # Конечное значение
# while i < end:
#     print(f"{i = }")
#     i += 1

# color = "Красный"  # Загаданный компьютером цвет
# guess = ""
# print("Я загадал цвет, попробуй отгадай")
# while guess != color:
#     guess = input()
# print(f"Правильно, загаданный цвет - {color}")


# color = "Красный"  # Загаданный компьютером цвет
# guess = ""
# tries = 5
# print(f"Я загадал цвет, попробуй отгадай, у тебя есть {tries} попыток")
# while guess != color and tries > 0:
#     guess = input()
#     tries = tries - 1
# if guess == color:
#     print(f"Правильно, загаданный цвет - {color}")
# else:
#     print(f"Ты проиграл, загаданный цвет - {color}")

i = 0
while i < 3:
    print("Hello")
    i += 1

print("-----------------------")

i = 0
while True:
    print("Hello")
    i += 1
    if i == 3:
        break

i = 0
while i < 10:
    i += 1
    if i%2 != 0:  # Если число нечетное
        continue  # Пропускаем итерацию цикла
    print(f"{i = }")
