# оператор IF
x = 1
# если x True то возращает True в ином случае возращает False
if x: 
    print(True)
else: 
    print(False)
    
light = 'red'

if light == 'red':
    print('stop')
elif light == 'yellow':
    print('Wait')
elif light == "green":
    print('go')
else:
    print("What?")
    
age = int(input('сколько вам лет?'))

if age >= 18:
    print('Werlcome')
else:
    print(f'Вы сказали что вам {age}')
    print(f'вам не хватает {18 - age} лет')
    print('Go to the back')

time = 715455
day = 'st'

if time > 8 and day != 'su':
    print('Мы открыты')
else:
    print('Мы закрыты')
    
x = 1 
if not x: 
    print('ok')
else:
    print('no')
    
x = 1 

res = 'ok' if x else 'no'