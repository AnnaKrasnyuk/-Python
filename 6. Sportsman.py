a = int(input("Сколько пробежал в первый день? "))
b = int(input("Сколько нужно пробежать? "))
day = 1

while a < b:
    a = a+(a/10)
    day+=1

print(day)