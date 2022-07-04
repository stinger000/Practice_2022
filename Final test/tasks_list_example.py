tasks = dict()


def sep():
    print("-" * 80)


def show_tasks():
    sep()
    print("Список активных задач:")
    for name in tasks.keys():
        print(name)
    sep()


def show_description():
    sep()
    name = input("Введите имя задачи: ")
    description = tasks.get(name, "Задача не найдена")
    print(description)
    sep()


def add_task():
    sep()
    print("Добавление новой задачи")
    name = input("Введите имя задачи: ")
    description = input("Введите описание: ")
    tasks[name] = description
    print("Задача успешно добавлена")
    sep()


def del_task():
    sep()
    print("Удаление задачи")
    name = input("Введите имя задачи: ")
    if name in tasks:
        del tasks[name]
        print(f"Задача {name} удалена")
    else:
        print("Задача не найдена")
    sep()


if __name__ == '__main__':
    while True:
        msg = """
[1] Вывести список задач
[2] Посмотреть подробности задачи
[3] Добавть задачу
[4] Удалить задачу
[5] Выход
Пожалуйста, введите соответствующую цифру: """
        num = int(input(msg))
        if num == 1:
            show_tasks()
        elif num == 2:
            show_description()
        elif num == 3:
            add_task()
        elif num == 4:
            del_task()
        elif num == 5:
            print("До свидания")
            break
        else:
            print("Введена неверная цифра")
