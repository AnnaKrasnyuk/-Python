class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        print('Полное имя сторудника:', self.name, self.surname)

    def get_total_income(self):
        print('Доход с премией:', self._income["wage"]+self._income["bonus"])


s = {"wage": int(input('Введите сумму оклада: ')), "bonus": int(input('Введите сумму премии: '))}
p = Position(input('Введите имя: '), input('Введите фамилию: '), input('Введите название должности: '), s)
p.get_full_name()
print('Должность:', p.position)
p.get_total_income()
