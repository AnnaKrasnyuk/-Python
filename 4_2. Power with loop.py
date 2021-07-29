def my_func(x, y):
    ans = 1
    if x <= 0:
        print("Неверные входные данные")
    else:
        for i in range(abs(y)):
            ans = ans*x
        print(1/ans)


my_func(x=int(input("Число: ")), y=int(input("Отрицательная степень числа: ")))
