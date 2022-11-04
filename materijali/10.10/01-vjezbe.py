"""
List Comprenhesion
newlist = [expression for item in iterable if condition == True]
ex.
newlist = [x for x in fruits if x!= "apple"]

"""

lista = [x for x in range(19)]

print(lista)
d = {k:v if v%3==0 else 0 for k,v in enumerate(lista)}

print(d)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

#Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24
#Now let’s try it with reduce:

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24