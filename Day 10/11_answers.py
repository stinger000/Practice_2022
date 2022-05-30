# 0
food = {
    "Еда": {
        "Суп": 215,
        "Салат": 75
    },

    "Напитки": {
        "Чай": 35,
        "Компот": 45
    }
}

food_cn = {
    "Еда": {
        "Фо-Бо": 215,
        "Кимчи": 75
    },

    "Напитки": {
        "Соевый соус": 35,
        "Саке": 45
    }
}


# 0.5

def in_dict(food_name: str, food_dict: dict) -> bool:
    for dishes in food_dict.values():
        if food_name in dishes:
            return True
    return False


# 0.6
def category(food_name: str, food_dict: dict) -> str:
    if not in_dict(food_name, food_dict):
        return ""
    for kind, dishes in food_dict.items():
        if food_name in dishes:
            return kind


# 1
def category_calories(kind: str, food_dict: dict) -> int:
    if kind not in food_dict:
        return 0
    return sum(food_dict[kind].values())


# print(category_calories("Еда", food))

# 3

def add_kind(kind: str, food_dict: dict):
    if kind not in food_dict:
        food_dict[kind] = dict()


# 2

def add_dish(name: str, kind: str, calories: int, food_dict: dict):
    add_kind(kind, food_dict)
    food_dict[kind][name] = calories


add_dish("Греча", "Еда", 5, food)
add_dish("Медовик", "Десерты", 500, food)


# print(food)

# 5

def most_calories(food_dict: dict):
    for kind, dishes in food_dict.items():
        # Простой и нехитрый метод
        maximal_calories = 0
        maximal_calories_name = ""
        for name, cal in dishes.items():
            if cal > maximal_calories:
                maximal_calories = cal
                maximal_calories_name = name
        # print(f"{kind} - {maximal_calories_name} - {maximal_calories}")

        # Более компактный метод
        max_name, max_cal = max(dishes.items(), key=lambda x: x[1])
        print(f"{kind} - {max_name} - {max_cal}")


# most_calories(food)


# 6

def fat_dishes(name: str, food_dict: dict):
    """
    Данная функция принимает имя блюда и печатает
    все блюда в данной категории, калорийность которых больше,
    чем у переданного.
    :param name: Имя блюда
    :param food_dict: Словарь с блюдами
    :return: None
    """
    kind = category(name, food_dict)
    if not kind:
        return
    min_cal = food_dict[kind][name]
    for dish, cal in food_dict[kind].items():
        if cal > min_cal:
            # print(dish, cal)
            pass
    # Решение в одну строку
    dishes = list(filter(lambda x: x[1] > min_cal, food_dict[kind].items()))
    print(dishes)


# fat_dishes("Греча", food)
# fat_dishes("Рис", food)

def test_05():
    print(in_dict("Компот", food))
    print(in_dict("Колбаса", food))
    print(in_dict("Саке", food_cn))


def test_06():
    print(category("Салат", food))
    print(category("Гречка", food))


if __name__ == '__main__':
    # test_05()
    test_06()
