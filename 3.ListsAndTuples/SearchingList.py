# List Method index
numbers = [3, 7, 1, 4, 2, 8, 5, 6]
print(numbers.index(5))
# 6

numbers *= 2
print(numbers)
#[3, 7, 1, 4, 2, 8, 5, 6, 3, 7, 1, 4, 2, 8, 5, 6]

#search value 5 from index 7 onwards
print(numbers.index(5, 7))
#14

# Specifying the Starting and Ending Indices of a Search
# value 7 starting from index 0 and to stop at index 4
print(numbers.index(7, 0, 4))
#1

print(1000 in numbers)
#false

print(5 in numbers)
#true

# Using Operator in to Prevent a ValueError
key = 5

if key in numbers:
    print(f'found {key} at index {numbers.index(key)}')
else:
    print(f'{key} not found')
#found 5 at index 6

# Exercise 3
numbers = [67, 12, 46, 43, 13]
numbers.index(43)

if 44 in numbers:
    print(f'Found 44 at index: {numbers.index(44)}')
else:
    print('44 not found')
