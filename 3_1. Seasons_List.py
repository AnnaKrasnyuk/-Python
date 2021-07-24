month = int(input("Введите номер месяца: "))
seasons = ["Зима", "Весна", "Лето", "Осень"]
while (month <= 0) or (month > 12):
    print("Месяца под таким номером не существует. Попробуйте ещё раз.")
    month = int(input("Введите номер месяца: "))
if (month == 1) or (month == 2) or (month == 12):
    print(seasons[0])
elif (month >= 3) and (month <= 5):
    print(seasons[1])
elif (month >= 6) and (month <= 8):
    print(seasons[2])
elif (month >= 9) and (month <= 11):
    print(seasons[3])
