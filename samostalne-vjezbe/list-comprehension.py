#Syntax: newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]


new_fruits = [f for f in fruits if 'a' in f] 
print("new_fruits:", new_fruits)

#You can use the range() function to create an iterable:
newlist1 = [x for x in range(10)]
print("newlist1:", newlist1)


#With condition
newlist2 = [x for x in range(10) if x < 5]
print("newlist2:", newlist2)

new_fruits2 = [x if x != "banana" else "orange" for x in fruits]
print("newlist2:", newlist2)

#Example: Iterating through a string Using List Comprehension
h_letters = [ letter for letter in 'human' ]
print("h_letters:", h_letters)

#Example: List Comprehensions vs Lambda functions
letters = list(map(lambda x: x+"o", 'human'))
print("letters:", letters)


#Example: Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print("num_list:",num_list)

#Example: if...else With List Comprehension
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

#Example: Transpose of a Matrix using List Comprehension
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print ("transpose:", transpose)

"""
Key Points to Remember
List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and loops for creating list.
However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
"""


