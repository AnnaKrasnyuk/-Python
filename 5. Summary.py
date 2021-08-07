from functools import reduce
with open('Sum', 'w+', encoding="utf-8") as file_obj:
    print(input('Введите числа через пробел: '), file=file_obj)
    file_obj.seek(0)
    s = file_obj.read()
    print(reduce(lambda x, y: x+y, list(map(int, s.split()))))
