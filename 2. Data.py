def data(name=None, surn=None, year=None, city=None, email=None, tel=None):
    print(f"Данные о пользователе. Имя: {name}; Фамилия: {surn}; Год рождения: {year};"
          f" Город проживания: {city}; Email: {email}; Телефон: {tel}")


data(name=(input("Введите имя: ")), surn=(input("Введите фамилию: ")), year=(input("Ваш год рождения: ")),
     city=(input("Ваш город проживания: ")), email=(input("Введите email: ")), tel=(input("Ваш номер телефона: ")))
