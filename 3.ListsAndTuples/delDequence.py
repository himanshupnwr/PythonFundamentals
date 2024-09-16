# Deleting the Element at a Specific List Index
numbers = list(range(0, 10))
print(numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del numbers[-1]
print(numbers)
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

del numbers[0:2]
print(numbers)
#[2, 3, 4, 5, 6, 7, 8]

del numbers[::2]
print(numbers)
#[3, 5, 7]

del numbers[:]
print(numbers)
#[]

# Exercise 2
numbers = list(range(1, 16))
print(numbers)

del numbers[0:4]
print(numbers)

del numbers[::2] #delete every other element
print(numbers)
