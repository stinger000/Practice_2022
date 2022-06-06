from random import randint

class Game:
    def __init__(self, max_number):
        self.max_number = max_number
        self.__number = randint(0, max_number)
        self.guess_count = 0

    def guess(self, number):
        self.guess_count += 1
        if number == self.__number:
            return True, f"Вы угадали, загаданное число равно {self.__number}"
        elif number < self.__number:
            return False, "Ваше число меньше, чем задумал компьютер"
        else:
            return False, "Ваше число больше, чем задумал компьютер"

    def get_guesses_count(self):
        return self.guess_count

if __name__ == '__main__':
    max_number = 10**50
    game = Game(max_number)
    print(f"Я загадал число от 0 до {max_number}")
    # Правила игры: запрещается изменять код, находящийся выше данной линии
    # Угадайте число
    # ------------------------------------------------------------------------
    while True:
        num = int(input("Пожалуйста, введите число:"))
        result, msg = game.guess(num)
        print(msg)
        if result:
            break
    print(f"Вы потратили {game.get_guesses_count()} попыток")

