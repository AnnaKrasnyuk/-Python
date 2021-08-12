class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for count in self.matrix:
            for el in count:
                my_str += f'{el:>5}'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        result = []
        if len(self.matrix) != len(other.matrix):
            print('Размеры матриц не совпадают')
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Размеры матриц не совпадают')
                return
            value = []
            for n in range(len(self.matrix[i])):
                value.append(self.matrix[i][n] + other.matrix[i][n])
            result.append(value)
        return Matrix(result)


ok = Matrix([[2, 3, 4], [3, 4, 5], [2, 3, 4]])
ok2 = Matrix([[3, 4, 7], [4, 4, 8], [2, 3, 4]])
print(ok+ok2)
