from itertools import cycle
new_list = input("Введите значения в список через пробел: ").split()
num = int(input("Введите число раз повтора элементов списка: "))
count = 0
for i in cycle(new_list):
    if count >= num:
        break
    count += 1
    print(i)
