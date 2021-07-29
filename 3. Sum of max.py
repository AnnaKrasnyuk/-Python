def my_func(a, b, c):
    z = 0
    maxim = [a, b, c]
    for i in range(2):
        z = max(maxim) + z
        maxim = [a, b, c]
        try:
            maxim.remove(z)
        except ValueError:
            continue
    print("Сумма двух максимальных чисел = ", z)


print("Введите 3 числа: ")
my_func(a=int(input()), b=int(input()), c=int(input()))
