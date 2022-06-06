from random import randint

upper_bound = 10 ** 35

N = randint(0, upper_bound)

print(f"Я загадал число от 0 до {upper_bound}, "
      f"попробуй отгадать его")

number_of_guesses = 1

guess = int(input("Введите ваш ответ: "))

while guess != N:
    number_of_guesses += 1
    if guess < N:
        print("Ваше число меньше, чем задумал компьютер")
    elif guess > N:
        print("Ваше число больше, чем задумал компьютер")
    guess = int(input("Введите ваш ответ: "))

print(f"Вы угадали, загаданное число равно {N}")
print(f"Вы потратили {number_of_guesses} попыток")
