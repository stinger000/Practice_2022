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

