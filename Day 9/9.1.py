# Что же ещё можно делать со списками

# Списки могут быть аргументами функции

words = ["питон", "лучший", "язык"]


def shout(wordlist):
    for word in wordlist:
        print(word.upper() + "!!!!!!1")


# shout(words)

# Функции могут изменять содержимое списков

def modify(wordlist):
    wordlist.append("Hello, world!")

modify(words)
# print(words)

def not_modify(wordlist): # Список не будет изменен
    wordlist = []

not_modify(words)
# print(words)

def really_clear_the_list(wordlist): # Список будет изменен
    wordlist.clear()

really_clear_the_list(words)
# print(words)

# Списки могут быть вложенными

# Пример создания вложенного списка

library = [
    ["Гоголь", "Есенин", "Пушкин"], # 1 полка
    ["Перышкин", "Эйнштейн"], # 2 полка
    ["Бредберри", "Хоккинг"]  # 3 полка
]
print(library)

# Допустим, мы хотим добавить полку к библиотеке
library.append(["Стругацкие"])
print(library)

# Добавить книгу на существующую полку
library[0].append("Толстой")
print(library)

i = 1
for bookshelf in library:
    print(f"На книжной полке {i} стоят следующие книги:")
    for book in bookshelf:
        print(book)
    print("-"*80)
    i += 1