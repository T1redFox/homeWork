#t1 = (1, 2, 3)
#l1 = [1, 2, 3]
#t1 = 1, 2, 3
#t1 = tuple((1, 2, 3))
#t1 = ()
#t1 = (1,)
#t1 = tuple('hello')

#print(t1.__sizeof__()) # узнаём обьём занимаемой памяти
#print(l1.__sizeof__())

#t1 = tuple('hello')
#t2 = tuple(' world')
#t3 = t1 + t2


#print(t3.count('a'))

#if 'l' in t3:
#    print(t3.index('l'))
#else: 
#    print('No')

#for i in t3:
#    if i == ' ':
#        continue
#    print(i, end="  ")


#t1 = (10, 11, [1, 2, 3], [4, 5, 6,], ['hello', 'world'])

#print(t1, id(t1))
#t1[4][0] = 'new'
#t1[4].append('hello')
#print(t1, id(t1))

#t1 = (1, 2, 3)
#x, y, z = t1

#print(x, y, z)

#x = 1
#y = 2

#print(x, y)
#x, y = y, x
#print(x, y)
