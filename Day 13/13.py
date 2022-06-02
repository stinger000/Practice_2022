# ООП

# 0.1 - структуризация данных
product = {
    "price": 999,
    "amount": 5,
    "name": "Тостерница"
}


# Функция печатает информацию о продукте
def print_product(prod: dict):
    print(f"На складе лежит {prod['name']} по цене {prod['price']} тугриков"
          f" в количестве {prod['amoun']}")


# print_product(product)

# Класс данных
# Он же - dataclass
class Product:
    # "магический" метод __init__
    def __init__(self, price, amount, name):  # Конструктор
        self.price = price
        self.amount = amount
        self.name = name


def print_product_1(prod: Product):
    print(f"{prod.name} по цене {prod.price} тугриков в количестве {prod.amount}")


p = Product(999, 5, "Хлеборезка")
print_product_1(p)
# print_product_1(1)  # Так делать нельзя


