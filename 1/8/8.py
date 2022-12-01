world = 'hello, world'
print(world) #ответ "hello, world"

world = 'hello, "world"'
print(world) #ответ "hello, "world""

world = 'hello, \"test\" "world"'
print(world) #ответ "hello, "test" "world""
'''
verse = 'бла бла бла бла бла 
бла бла бла бла 
бла бла'
print(verse) # ответ SyntaxError: unterminated string literal (detected at line 10)
'''
verse = 'бла бла бла бла бла \
бла бла бла бла \
бла бла'
print(verse) # ответ бла бла бла бла бла бла бла бла бла бла бла

verse = 'бла бла бла бла бла \n\
бла бла бла бла \n\
бла бла'
print(verse) 
'''
ответ 
бла бла бла бла бла
бла бла бла бла
бла бла
'''

verse = ('бла бла бла бла бла \n'
        'бла бла бла бла бла бла')
print(verse) 
'''
ответ 
бла бла бла бла бла
бла бла бла бла бла бла
'''

verse = '''\
бла бла бла бла бла 
бла бла бла бла 
бла бла\
'''
print(verse) 
'''
ответ 
бла бла бла бла бла
бла бла бла бла
бла бла
'''