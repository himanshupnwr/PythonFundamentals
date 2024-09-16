# Section 5.5 snippets

# Specifying a Slice with Starting and Ending Indices
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

print(numbers[2:6])
#[5, 7, 11, 13]

# Specifying a Slice with Only an Ending Index
print(numbers[:6])
print(numbers[0:6])
#[2, 3, 5, 7, 11, 13]

# Specifying a Slice with Only a Starting Index
print(numbers[6:])
print(numbers[6:len(numbers)])
#[17, 19]

# Specifying a Slice with No Indices
print(numbers[:]) #prints the list as it is

# Slicing with Steps
print(numbers[::2])
#[2, 5, 11, 17]

# Slicing with Negative Indices and Steps
print(numbers[::-1]) #reversing the list
#[19, 17, 13, 11, 7, 5, 3, 2]

numbers[-1:-9:-1]
#[19, 17, 13, 11, 7, 5, 3, 2]

# Modifying Lists Via Slices
numbers[0:3] = ['two', 'three', 'five']
print(numbers)
#['two', 'three', 'five', 7, 11, 13, 17, 19]

#deleting a slice of list
numbers[0:3] = []
print(numbers)
#[7, 11, 13, 17, 19]

numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers[::2] = [100, 100, 100, 100] #add after every other element
print(numbers)
#[100, 3, 100, 7, 100, 13, 100, 19]

print(id(numbers))
#2067102880128

#empty a list
print(numbers[:])

# Exercise 3
numbers = list(range(1, 16))
print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers[1:len(numbers):2]) #only the even integers
#[2, 4, 6, 8, 10, 12, 14]

numbers[5:10] = [0] * len(numbers[5:10])
print(numbers)
#[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 11, 12, 13, 14, 15]

numbers[5:] = []
print(numbers)
#[1, 2, 3, 4, 5]
