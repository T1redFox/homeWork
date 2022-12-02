words = ['мадам', 'топот', 'madam', 'word']
t = []

for i in words:
    if i == i[::-1]:
        t.append(i)
        
print(t)

my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
r = []

for c in my_str:
    d = c.replace(' ', '') # переворачиваем строку
    d = d.lower() # пделаем все элементы одного регистра
    if d == d[::-1]:
        r.append(c)
        
print(r)