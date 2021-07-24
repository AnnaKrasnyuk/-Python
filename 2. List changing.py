a = list(input().split())
i = 1
element = 0
for i in range(len(a)//2):
    a[element], a[element + 1] = a[element + 1], a[element]
    element = element+2
print(a)
