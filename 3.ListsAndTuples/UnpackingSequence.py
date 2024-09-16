student_tuple = ('Amanda', [98, 85, 87])
first_name, grades = student_tuple
print(first_name, grades)

first, second = 'hi'
print(f'{first}  {second}')

number1, number2, number3 = [2, 3, 5]
print(f'{number1}  {number2}  {number3}')

number1, number2, number3 = range(10, 40, 10)
print(f'{number1}  {number2}  {number3}')

# Swapping Values Via Packing and Unpacking
number1 = 99
number2 = 22
number1, number2 = (number2, number1)

print(f'number1 = {number1}; number2 = {number2}')

# Accessing Indices and Values Safely with Built-in Function enumerate
colors = ['red', 'orange', 'yellow']

print(list(enumerate(colors)))

print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index}: {value}')

# Amanda [98, 85, 87]
# h  i
# 2  3  5
# 10  20  30
# number1 = 22; number2 = 99
# [(0, 'red'), (1, 'orange'), (2, 'yellow')]
# ((0, 'red'), (1, 'orange'), (2, 'yellow'))
# 0: red
# 1: orange
# 2: yellow

# fig05_01.py - Enumerator
"""Displaying a bar chart"""
numbers = [19, 3, 15, 7, 11]

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8}   Bar')

for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8}   {"*" * value}')

# Creating a bar chart from numbers:
#Index   Value   Bar
#    0      19   *******************
#    1       3   ***
#    2      15   ***************
#    3       7   *******
#    4      11   ***********

#Exercise
# Exercise 3
high_low = ('Monday', 87, 65)

print(high_low)

print(f'{high_low[0]}: High={high_low[1]}, Low={high_low[2]}')

day, high_low, high_high = high_low

# Exercise 4
names = ['Amanda', 'Sam', 'David']

for i, name in enumerate(names):
    print(f'{i}: {name}')
