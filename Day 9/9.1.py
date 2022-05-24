# Что же ещё можно делать со списками

# Списки могут быть аргументами функции

words = ["питон", "лучший", "язык"]


def shout(wordlist):
    for word in wordlist:
        print(word.upper() + "!!!!!!1")


shout(words)

# Функции могут изменять содержимое списков

def modify(wordlist):
    wordlist.append("Hello, world!")

modify(words)
print(words)

def not_modify(wordlist): # Список не будет изменен
    wordlist = []

not_modify(words)
print(words)

def really_clear_the_list(wordlist): # Список будет изменен
    wordlist.clear()

really_clear_the_list(words)
print(words)