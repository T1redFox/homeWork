# import os
# import random as r
# import random
# from random import randint, shuffle
# from random import *

# print(os.getcwd())
# # print(random.randint(1, 100))
#
# print(randint(1, 100))
# l = [1, 2, 3, 4, 5]
# shuffle(l)
# print(l)


import lib28
print(__name__)
# print(libs.get_count('hello', 'l'))
# print(libs.get_len('hello'))

f = lib28.get_count
print(f('hello', 'l'))


def get_sum(a, b):
    return a + b


func = get_sum
print(func(1, 2))