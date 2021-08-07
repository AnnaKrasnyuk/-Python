from functools import reduce
my_dict = {}
with open('Lessons', 'r', encoding="utf-8") as file_obj:
    for i in file_obj:
        i = i.split()
        hours = [int(k.rstrip('(л)(пр)(лаб)')) for k in i[1::] if k != '—']
        my_dict.update({i[0].rstrip(":"): sum(hours)})
    print(my_dict)
