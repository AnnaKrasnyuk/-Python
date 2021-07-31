from sys import argv

name, time, rate, bonus = argv

print("Имя скрипта: ", name)
print("Выработка в часах: ", time)
print("Ставка в час: ", rate)
print("Премия: ", bonus)
print((int(time)*int(rate))+int(bonus))
