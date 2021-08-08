class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, sq_metr, depth):
        mass = (self._length*self._width*sq_metr*depth)/1000
        print(f'{self._length}м*{self._width}м*{sq_metr}кг*{depth}см = {mass} т')


l = int(input("Введите длину асфальта (м): "))
w = int(input("Введите ширину асфальта (м): "))
asph = Road(l, w)
sq = int(input("Введите массу асфальта для покрытия одного кв метра асфальтом в 1см (кг): "))
d = int(input("Введите толщину полотна (см): "))
asph.mass_of_asphalt(sq, d)
