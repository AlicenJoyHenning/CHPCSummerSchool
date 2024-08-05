# -*- coding: utf-8 -*-

my_list = [1, 2]
my_list.append(3)
len(my_list)


x = [1,2,3]
y = x[1:] # everything after index 1 (1 and 2)
print(y) 
# OUTPUT y = [2, 3]

x = {'a':1, 'b':2}
x.update({'c':3})
print(x)
# OUTPUT : {'a': 1, 'b': 2, 'c': 3}

x = {'a':1, 'b':2}
del x['a']
print(x)
# OUTPUT : {'b' : 2}