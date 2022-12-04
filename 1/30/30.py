import os

path = os.walk('One app')
for i in path:
    print(i[0])
    print(i[-1])