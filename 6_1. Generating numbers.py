from itertools import count
fr = int(input("С какого числа начать? "))
to = int(input("До какого числа генерировать? "))
for i in count(fr):
    if i >= to:
        break
    print(i)
