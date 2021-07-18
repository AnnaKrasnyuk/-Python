n = int(input("Введите число: "))

maxim = 0

while n != 0:
    k = n % 10
    n = n//10
    if k > maxim:
        maxim = k

print(maxim)