#def getSum(a, b, c=0, d=1):
#    return(a + b + c + d)

#print(getSum(1, 2, 5, 7))

#def getSum(*args, **kwargs):
#    print(sum(args))

#getSum(1 ,3, 4, 2, 13)

#def func(**kwargs):
#    print(kwargs)

#func(a=1, b=5, c=56)

def f(a, x, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

f(1, 2, 3, 4, b='test', c = 'hi')