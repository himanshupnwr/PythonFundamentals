def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(maximum(12, 27, 36))
#36

print(maximum(12.3, 45.6, 9.7))
#45.6

print(maximum('yellow', 'red', 'orange'))
#yellow

print(maximum(13.5, -3, 7))
#13.5

# Python’s Built-In max and min Functions
print(max('yellow', 'red', 'orange', 'blue', 'green'))
#yellow

print(min(15, 9, 27, 14))
#9

# Exercise 3
print(max([14, 27, 5, 3]))
#27

print(min('orange'))
#a
