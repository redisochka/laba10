import json

def xd1():

    with open('json1.json', encoding='utf-8') as file:
        data = json.load(file)
    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()

def xd2():

    with open('json.json', encoding='utf-8') as file:
        data = json.load(file)

    new_product = {}
    new_product["name"] = input("Введите название продукта: ")
    new_product["price"] = input("Введите цену продукта: ")
    new_product["weight"] = input("Введите вес продукта: ")
    available = input("Есть ли он в наличии (да/нет): ")
    if available == "да":
        new_product["available"] = True
    else:
        new_product["available"] = False

    file = open("json.json", "w", encoding="UTF8")
    data["products"].append(new_product)
    json.dump(data, file)

    for product in data['products']:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии")
        print()

def xd3():

    with open('en-ru.txt', 'r') as file:
        eng_ru = {}
        for line in file:
            key, value = line.strip().split(' - ')
            eng_ru.setdefault(value, []).append(key)

    with open('ru-en.txt', 'w') as file:
        for key in sorted(eng_ru.keys()):
            file.write(f"{key} - {', '.join(sorted(eng_ru[key]))}\n")

xd1()
xd2()
xd3()