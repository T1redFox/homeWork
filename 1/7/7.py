# не существеющаяя переменная 
#print(test) #ответ NameError: name 'test' is not defined

test = None
print(test) #ответ None

#способы записи переменных
x = 1
y = 2
x = 1; y = 2
x, y = (1, 2)

#bool
my_true = True
my_false = False

print(type(my_true), type(my_false)) #ответ <class 'bool'> <class 'bool'>

# str() int() float() bool()
x = 3.5
print(x, type(x))
x = int(x)
print(x, type(x))
'''
ответ: 
3.5 <class 'float'>
3 <class 'int'>
'''
print(x, type(x))
x = str(x)
print(x, type(x))
'''
ответ: 
3 <class 'int'>
3 <class 'str'>
'''
print(x, type(x))
x = bool(x)
print(x, type(x))
'''
ответ: 
3 <class 'str'>
True <class 'bool'>
если переменная будет ровна 0 или None то будет False
'''