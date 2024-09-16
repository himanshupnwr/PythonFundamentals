# Sorting a List in Ascending Order
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

numbers.sort()

print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sorting a List in Descending Order
numbers.sort(reverse=True)
print(numbers)
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Built-In Function sorted - it does not update the original list
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
ascending_numbers = sorted(numbers)
print(ascending_numbers)
print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

letters = 'fadgchjebi'
ascending_letters = sorted(letters)
print(ascending_letters)
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

colors = ('red', 'orange', 'yellow', 'green', 'blue')
ascending_colors = sorted(colors)
print(ascending_colors)
#['blue', 'green', 'orange', 'red', 'yellow']
