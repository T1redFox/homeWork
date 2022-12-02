#s = {'apple', 'orange', 'apple', 'orange', 'banana'}
#s2 = set('hello')
#s3 = {i for i in range(1, 11)}
#s4 = set()

#print(s)
#print(s2)
#print(s3)
#rint(s4)

#nums = [1, 2, 3, 1, 2, 4, 5]
#nums2 = set(nums)
#print(nums2)

#a = set('abracadabra')
#b = set('alacazam')

#c = a - b # вычитаем из a все буквы что есть в b 
#d = a | b # объединяет - буквы или в a или в b
#e = a & b # пересечение - буквы и в a и в b
#f = a ^ b # множествои из элементов - буквы в a или в b, но не в обоих 

#print(a, b, c, d, e, f, sep='\n')

s = {'apple', 'orange', 'apple', 'orange', 'banana'}

s.copy() # возращает копию множества
s.add() # добавляет элемент в множества 
s.remove() # удаляет элемент из множества
s.discard() # удаляет элемент из множества если он есть 
s.pop() # возвращает и удаляет первый элемент из множества. Чисты рандом что тебе он выдаст 
s.clear() # чистит всё множество

a = frozenset('hello')