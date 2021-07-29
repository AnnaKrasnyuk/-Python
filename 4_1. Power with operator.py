def my_func(x, y):
    if x <= 0:
        print("Неверные входные данные")
    else:
        print(1/x**abs(y))


my_func(x=int(input("Число: ")), y=int(input("Отрицательная степень числа: ")))
