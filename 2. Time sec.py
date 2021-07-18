sec = int(input('Введите секунды: '))

while sec<0:
    sec = int(input('Введите секунды (Это может быть только положительное число): '))

minutes = sec//60
hours = sec//3600

if sec >= 60:
    sec = sec % 60
if minutes >= 60:
    minutes = minutes % 60

print(f'{hours}:{minutes}:{sec}')
