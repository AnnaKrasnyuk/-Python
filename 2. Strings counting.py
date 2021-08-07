n = 0
with open('Text_for_second', 'r', encoding="utf-8") as file_obj:
    print('Количество строк: ', len(file_obj.readlines()))
    file_obj.seek(0)
    for i in (file_obj.readlines()):
        n += 1
        print(f'В {n} строке {len(i)-1} символов')
