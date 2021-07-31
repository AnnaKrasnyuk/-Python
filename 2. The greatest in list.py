first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [first_list[el] for el in range(1, len(first_list)) if first_list[el] > first_list[el-1]]
print(new_list)
