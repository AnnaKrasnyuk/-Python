data = 'new'
with open('New_file', 'w', encoding='utf-8') as file_obj:
    while data != '':
        data = input()
        print(data, file=file_obj)
