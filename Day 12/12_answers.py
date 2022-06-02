goods = {
    "Ноутбук": {
        "price": 99000,
        "amount": 1,
        "kind": "Электроника"
    },
    "Смартфон": {
        "price": 20000,
        "amount": 8,
        "kind": "Электроника"
    },
    "Холодильник": {
        "price": 40000,
        "amount": 9,
        "kind": "Бытовая техника"
    }
}

money = 0


def add_money(amount: int):
    global money
    money += amount


# 2
def buy(product: str, goods_dict: dict) -> bool:
    if product not in goods_dict:
        return False
    if goods_dict[product].get("amount", 0) <= 0:
        return False
    goods_dict[product]["amount"] -= 1
    add_money(goods_dict[product]["price"])
    return True


# 3
def buy_by_list(shopping_list: dict, goods_dict: dict) -> dict:
    cart = dict()
    for name, amount in shopping_list.items():
        for i in range(amount):
            if not buy(name, goods_dict):
                break
            if name not in cart:
                cart[name] = 1
            else:
                cart[name] += 1
    return cart


# 4
def analogs(product: str, goods_dict: dict) -> list:
    analogs_list = []
    if product not in goods_dict:
        return analogs_list
    for name, parameters in goods_dict.items():
        if parameters.get("kind", "") == goods_dict[product].get("kind", "") \
                and 0 < parameters.get("price", -1) < goods_dict[product].get("price", -1):
            analogs_list.append(name)
    return analogs_list


# 5
def buy_by_list_with_limited_money(shopping_list: dict, goods_dict: dict, money: int) -> dict:
    cart = dict()
    names = list(shopping_list.keys())
    # names.sort(key=lambda name: goods_dict.get(name, dict()).get("price", -1), reverse=True)
    for name in names:
        amount = shopping_list[name]
        for i in range(amount):
            if not 0 < (price := goods_dict.get(name, dict()).get("price", -1)) < money:
                break
            if not buy(name, goods_dict):
                break
            if name not in cart:
                cart[name] = 1
            else:
                cart[name] += 1
            money -= price
    return cart


def test_2():
    print(buy("Ноутбук", goods))
    print(buy("Смартфон", goods))
    print(buy("Тостерница", goods))
    print(money)


def test_3():
    shopping_list = {

        "Смартфон": 9,
        "Ноутбук": 3,
        "Тостерница": 1
    }
    print(buy_by_list(shopping_list, goods))
    print(money)


def test_4():
    print(analogs("Ноутбук", goods))

def test_5():
    shopping_list = {
        "Ноутбук": 3,
        "Смартфон": 9,
        "Тостерница": 1
    }
    print(buy_by_list_with_limited_money(shopping_list, goods, 120000))
    # print(money)


if __name__ == '__main__':
    # test_2()
    # test_3()
    # test_4()
    test_5()