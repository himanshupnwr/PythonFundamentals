# Passing an Entire List to a Function
def modify_elements(items):
    """"Multiplies all element values in items by 2."""
    for i in range(len(items)):
        items[i] *= 2

numbers = [10, 3, 7, 1, 9]

modify_elements(numbers)

print(numbers)
#[20, 6, 14, 2, 18]

numbers_tuple = (10, 20, 30)
modify_elements(numbers_tuple)
print(numbers_tuple)
# TypeError: 'tuple' object does not support item assignment
# tuples are immutable and non modifiable

