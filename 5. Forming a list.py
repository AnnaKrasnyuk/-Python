from functools import reduce
new_list = [i for i in range(100, 1000, 2)]
print(reduce(lambda x, y: x*y, new_list))
