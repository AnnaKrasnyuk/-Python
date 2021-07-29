def division(a, b):
    try:
        print("Частное: ", a/b)
    except ZeroDivisionError:
        print("Деление на ноль невозможно. Попробуйте снова")
        division(a=int(input("Введите делимое: ")), b=int(input("Введите делитель: ")))


division(a=int(input("Введите делимое: ")), b=int(input("Введите делитель: ")))
