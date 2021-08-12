class Cell:
    def __init__(self, param):
        if param <= 0:
            param = 1
        self.param = param

    def __add__(self, another):
        return Cell(self.param+another.param)

    def __sub__(self, another):
        return Cell(self.param-another.param) if self.param-another.param > 0 else "Разность количества ячеек двух клеток меньше нуля"

    def __mul__(self, another):
        return Cell(self.param*another.param)

    def __truediv__(self, another):
        return Cell(self.param//another.param)

    def make_order(self, count):
        s = ''
        for i in range(self.param // count):
            s = s + ("*" * count + "\n")
        s = s + ("*" * (self.param % count))
        return s


cell_1 = Cell(int(input('Введите количество ячеек первой клетки (больше 0, иначе будет использована одна): ')))
cell_2 = Cell(int(input('Введите количество ячеек второй клетки (больше 0, иначе будет использована одна): ')))
summ = cell_1+cell_2
sub = cell_1-cell_2
mult = cell_1*cell_2
divid = cell_1/cell_2
print(summ.make_order(5), '\n')
try:
    print(sub.make_order(5), '\n')
except AttributeError:
    print("Разность количества ячеек двух клеток меньше либо равна нулю")
print(mult.make_order(5), '\n')
print(divid.make_order(5), '\n')


