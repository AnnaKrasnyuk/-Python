proceeds = int(input("Значение выручки компании: "))
expenses = int(input("Значение издержек компании: "))

if proceeds > expenses:
    profit = proceeds-expenses
    print(f"Фирма в прибыли ({profit})")
    rent = profit/proceeds
    print(f"Рентабельность = {rent}")
    workers = int(input("Сколько сотрудников в фирме? "))
    print(f"На одного сотрудника приходится {profit/workers}")
elif proceeds == expenses:
    print("Выручка фирмы равна издержкам")
else:
    print(f"Компания в убытке ({expenses-proceeds})")
