rating = [7, 5, 3, 3, 2]
new_rating = rating.copy()

new = int(input("Введите число: "))

if new > rating[0]:
    new_rating.insert(0, new)
elif new < rating[-1]:
    new_rating.append(new)
else:
    for index in rating:
        if new == index:
            new_rating.insert(rating.index(index)+rating.count(index), new)
            break
        elif new < index:
            continue
        elif new > index:
            new_rating.insert(rating.index(index), new)
            break
print(new_rating)
