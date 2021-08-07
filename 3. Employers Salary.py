summ = 0
with open('Employers_salary', 'r', encoding="utf-8") as file_obj:
    for i in (file_obj.readlines()):
        salary = int(i[i.index(' ')+1::])
        summ += salary
        if salary < 20000:
            print('Оклад менее 20 тыс. имеет: ', i[0:i.index(' ')])
    file_obj.seek(0)
    print("Средняя величина дохода = ", summ/(len(file_obj.readlines())))
