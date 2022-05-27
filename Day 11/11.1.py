# Словари. Продолжение.

bookshelf = {
    "Руслан и людмила": 354,
    "Война и мир": 2587,
    "Мертвые души": 412,
}

# Список ключей
print(bookshelf.keys())

# Список значений
pages = list(bookshelf.values())
print(pages)

# Более простой способ итерирования словаря
for name, page_count in bookshelf.items():
    print(name, page_count)

# Встроенный операции

# Максимальное и минимальное значение
print(max(pages), min(pages))

# Сумма элементов
print(sum(pages))

# Среднее значение
print(sum(pages) / len(pages))

# Сортировка списка
print(sorted(pages))  # Метод 1, не изменят список

pages.sort()  # Метод 2, список будет изменен

print(pages)
