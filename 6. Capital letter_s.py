int_func = lambda lil_word = '': lil_word.title()

whole_str = input().split()
new_str = []
for word in whole_str:
    new_str.append(int_func(word))
print(' '.join(new_str))
