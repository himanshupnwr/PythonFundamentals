color_names = ['orange', 'yellow', 'green']

# Inserting an Element at a Specific List Index
color_names.insert(0, 'red')
print(color_names)
#['red', 'orange', 'yellow', 'green']

# Adding an Element to the End of a List
color_names.append('blue')
print(color_names)
#['red', 'orange', 'yellow', 'green', 'blue']

# Adding All the Elements of a Sequence to the End of a List
color_names.extend(['indigo', 'violet'])
print(color_names)
#['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

sample_list = []
s = 'abc'
sample_list.extend(s)
print(sample_list)
#['a', 'b', 'c']

t = (1, 2, 3)
sample_list.extend(t)
print(sample_list)
#['a', 'b', 'c', 1, 2, 3]

#extend expects only one parameter
sample_list.extend((4, 5, 6))  # note the extra parentheses
print(sample_list)
#['a', 'b', 'c', 1, 2, 3, 4, 5, 6]

# Removing the First Occurrence of an Element in a List
color_names.remove('green')
print(color_names)
#['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']

# Emptying a List
color_names.clear()
print(color_names)
#[]

# Counting the Number of Occurrences of an Item
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

for i in range(1, 6):
    print(f'{i} appears {responses.count(i)} times in responses')

# 1 appears 3 times in responses
# 2 appears 5 times in responses
# 3 appears 8 times in responses
# 4 appears 2 times in responses
# 5 appears 2 times in responses

# Reversing a List’s Elements
color_names = ['red', 'orange', 'yellow', 'green', 'blue']
color_names.reverse()
print(color_names)
# ['blue', 'green', 'yellow', 'orange', 'red']

# Copying a List - shallow copy
copied_list = color_names.copy()
print(copied_list)
#['blue', 'green', 'yellow', 'orange', 'red']

rainbow = ['green', 'orange', 'violet']
rainbow.insert(rainbow.index('violet'), 'red')
print(rainbow)
#['green', 'orange', 'red', 'violet']

rainbow.append('yellow')
rainbow.reverse()
rainbow.remove('orange')
