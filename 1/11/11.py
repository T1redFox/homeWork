name = 'Denis'
age = 20


# old vertion
print('My name is ' + name + '. I am ' + str(age)) # получаем "My name is Denis. I am 20"
print('My name is %(name)s. I am %(age)d' %{'name': name, "age": age}) # получаем "My name is Denis. I am 20"
print('My name is %s. I am %d' %(name,age)) # получаем "My name is Denis. I am 20"

print('Title: %s, Prise: %f ' %('sony', 40)) # получаем "Title: sony, Prise: 40.000000"
print('Title: %s, Prise: %.2f ' %('sony', 40)) # получаем "Title: sony, Prise: 40.00"

# format
print('My name is {}. I am {}'.format(name, age)) # получаем "My name is Denis. I am 20"
print('My {1} name is {0}. I am {1}'.format(name, age)) # получаем "My 20 name is Denis. I am 20"

print('My {age} name is {name}. I am {age}'.format(name=name, age=age)) # получаем "My 20 name is Denis. I am 20"

# f-strings
print(f'My name is {name}. I am {age}') # получаем "My name is Denis. I am 20"
print(f'My name is {name}. I am {age + 5}') # получаем "My name is Denis. I am 25"
print(f'5 + 2 = {5 + 2}') # получаем "5 + 2 = 7"