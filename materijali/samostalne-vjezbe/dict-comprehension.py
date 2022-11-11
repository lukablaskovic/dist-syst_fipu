#Double each value in the dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

#IN RANGE
d = {n: n**2 for n in range(5)}
print(d)

# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))
#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))
print(celsius_dict)

#IF CONDITION
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Check for items greater than 2
dict1_cond = {k:v for (k,v) in dict1.items() if v>2}
print(dict1_cond)
# Multiple If Conditions
dict1_doubleCond = {k:v for (k,v) in dict1.items() if v>2 if v%2 == 0}
print(dict1_doubleCond)

#IF ELSE CONDITION
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}
# Identify odd and even entries
dict1_tripleCond = {k:('even' if v%2==0 else 'odd') for (k,v) in dict1.items()}
print(dict1_tripleCond)

#NESTED DICTIONARY COMPREHENSION

nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} 
for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)


#item price in dollars
old_price_food = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price_food = {item: value*dollar_to_pound for (item, value) in old_price_food.items()}
print(new_price_food)

#Multiple if Conditional Dictionary Comprehension
names = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_names = {k: v for (k, v) in names.items() if v % 2 != 0 if v < 40}
print("new_names:", new_names)

#if-else Conditional Dictionary Comprehension
original_names = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_names = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_names.items()}
print("new_names", new_names)

#Using enumerate() in dictionary comprehension
list = ['java', 'python', 'pandas']
my_dict = {key:value for key,value in enumerate(list)}
print(my_dict)

