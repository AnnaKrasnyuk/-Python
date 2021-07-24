number = int(input("Введите количество товаров: "))
i = 1
goods = []
names = []
prices = []
amounts = []
units = []
while i <= number:
    name = input(f"Введите название товара №{i}: ")
    price = int(input(f"Введите цену товара №{i}: "))
    amount = int(input(f"Введите количество товара №{i}: "))
    unit = input(f"Введите единицу измерения товара №{i}: ")
    charact = {'название': name, 'цена': price, 'количество': amount, 'единица измерения': unit}
    prod = (i, charact)
    goods.append(prod)
    names.append(name)
    prices.append(price)
    amounts.append(amount)
    units.append(unit)
    anka = {'название': names, 'цена': prices, 'количество': amounts, 'ед': units}
    i += 1
print('Структура данных «Товары»: ', goods)
print('Аналитика о товарах: ', anka)
