a = [2, 2.2, 'text', False, [1, True, 3], (3, ), {"key_1": 1, "key_2": 2}]
while len(a) != 0:
    print(f"{a[-1]} имеет тип: {type(a[-1])}")
    del a[-1]
