#while True:
#    print('Hello')

#i = 1

#while i <= 10:
#    print(i, end=' ')
#    i += 1
    
#print('Hello', 'World', end=' ')
#print('Hello', 'World', sep=' ')

#s = 'Hello World'

#for l in s:
#    if l == ' ':
#        continue # пропустит пробел
#    print(f'"{l}"', end=' ')

#for i in 'Helloworld': 
#    if i == ' ': # пропустит всё после пробела и завершит принудительно функцию 
#        break
#    print(i, end=' ')
#else:
#    print('\nNo spaces')

i = 0 # дал это число так как не было дано начальное число, а был дан только промежуток
while i <= 2022:
    if i >= 1900:
        print(i, end=' ')
        i += 1
    else:
        i += 1