from random import randint

s = randint(1, 100)
t = 0

print(' ')
print(' Угадай число '.center(60, '*'),)
print('игра "Угадай число"- ваша задача состоит в том что бы угодать\nчисло от 1 до 100. У вас в запасе бесграничное количество\nпопыток, поэтому по скорее вводи своё число и проверь свою удачу!!')
n = int(input('Введите число от 1 до 100: '))

while n != s:
    if t == 0:
        t = 1
        if n <= 100 and n > 0:
            if n > s:
                print('Ваше число больше загадоного числа')
            elif n == s:
                print(f'Поздравляю вы угадали число!!!, количество затраченых попыток: {t} ')
            else:     
                print('Ваше число меньше загадоного числа')
        elif n < 0:
            print('Ваше число меншье 1!')
        else:
            print('Ваше чесло больше 100!')
    else:
        n = int(input('Попробуйте ещё раз, введите число от 1 до 100: '))
        t += 1
        if n <= 100 and n > 0:
            if n > s:
                print('Ваше число больше загадоного числа')
            elif n == s:
                print(f'Поздравляю вы угадали число!!!, количество затраченых попыток: {t} ')
            else:     
                print('Ваше число меньше загадоного числа')
        elif n < 0:
            print('Ваше число меншье 1!')
        else:
            print('Ваше чесло больше 100!')
