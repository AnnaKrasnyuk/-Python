def func(numbers):
    summa = 0
    while "/" not in numbers:
        for i in numbers:
            summa += int(i)
        print(f"Сумма чисел = {summa}. Чтобы перестать складывать числа нажмите '/'")
        numbers = input().split()
    else:
        for k in (numbers[0:numbers.index('/')]):
            summa += int(k)
        print(f"Сумма чисел = {summa}.")


func(input("Введите строку из чисел через пробел: ").split())
