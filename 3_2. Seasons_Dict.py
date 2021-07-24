month = int(input("Введите номер месяца: "))
while (month <= 0) or (month > 12):
    print("Месяца под таким номером не существует. Попробуйте ещё раз.")
    month = int(input("Введите номер месяца: "))
seasons = {
    "Зима": [1, 2, 12],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8],
    "Осень": [9, 10, 11]
}
if month in seasons["Зима"]:
    print("Зима")
elif month in seasons["Весна"]:
    print("Весна")
elif month in seasons["Лето"]:
    print("Лето")
else:
    print("Осень")
