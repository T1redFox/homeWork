s = 'C:\d\new.txt'
print(s) 
'''
ответ 
C:\d
ew.txt
'''

s = 'C:\d\\new.txt'
print(s) # ответ C:\d\new.txt

s = r'C:\d\new.txt'
print(s) # ответ C:\d\new.txt

s = 'Py' 'thon'
print(s) # ответ Python

s1 = 'Hello'
s2 = 'World'
# s3 = s1 s2 ошибка
s3 = s1 + s2

print(s3) #ответ "HelloWorld"

name = 'Denis'
age = 20

print('My name is ' + name) #ответ "My name is Denis"
print('My name is ' + name + ' I am ' + str(age)) #ответ "My name is Denis I am 20"

print('hi ' * 5) # ответ hi hi hi hi hi

i = 'hello world'
print(i[0]) # ответ "h" 
print(i[-1]) # ответ "d" 

#[x:y:z]

d = 'hello world'

print(d[0:10]) # ответ "hello worl"
print(d[::2]) # ответ "hlowrd"
print(d[::-1]) # ответ "dlrow olleh"
print(d[:5] + d[6:]) # ответ "helloworld"