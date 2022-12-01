# l = [1, 2, 3, 4, 'hello', ['test', 10], 'world', True] # создаю масив (список)

# l2 = list('hello')
# l3 = list((1, 2, 3, 4, ))

# l4 = [i for i in 'hello']
# #l5 = [i for i in 'hello world' if i != ' ' and i != 'e']
# l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']] # убираем из текста все гласные и пробелы 

# print(l, l2, l3, l4, l5, sep='\n')

# print(list(range(1, 11))) # от 1 до 11
# print(list(range(0, 11, 2))) # от 0 до 11 только чётные

for i in range(1,3):
    print(f'Внешний цикл #{i}')
    for j in range(1,3):
        print(f'\tВнутрений цикл #{j}')