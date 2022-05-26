# Словари

bookshelf = dict()  # Пустой словарь

# dictionary = {key1: value1, key2: value2}
# key - ключ, по которому мы ищем данные
# value - сами данные (значение)

# Создать словарь, наполненный данными
bookshelf = {
    "Руслан и людмила": 354,
    "Война и мир": 2587,
    "Мертвые души": 412,
}

# Просто получить элемент из словаря
pages = bookshelf["Руслан и людмила"]
print(pages)

# print(bookshelf["Сказка о царе Салтане"])  # Вызовет ошибку

print(bookshelf.get("Сказка о царе Салтане", 0))  # Более безопасный метод

books = bookshelf.keys()
print(books)

for book in bookshelf.keys():
    print(f"В книге {book} {bookshelf.get(book)} страниц")

book = "Мертвые души"


# Проверка, присутствует ли ключ в словаре
if book in books:
    print(f"{book} присутствует в словаре")
else:
    print(f"{book} - такой книги нет")

if book in bookshelf:
    print(f"{book} присутствует в словаре")
else:
    print(f"{book} - такой книги нет")

# Добавление элементов в словарь
bookshelf["Дубровский"] = 430

print(bookshelf)

# Изменение значения словаря
bookshelf["Дубровский"] = 429
print(bookshelf)

# Удаление элементов из словаря
del bookshelf["Дубровский"]
print(bookshelf)
