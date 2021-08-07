with open('Forth', 'r', encoding="utf-8") as f_obj, open('New_txt', 'w', encoding='utf-8') as new_f:
    trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    for i in (f_obj.readlines()):
        number = i[0:i.index(" ")]
        new_f.write(f'{trans[number]} {i[i.index(" ")+1::]}')
