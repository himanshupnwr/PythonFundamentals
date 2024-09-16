# Finding the Minimum and Maximum Values Using a Key Function
'Red' < 'orange'
# false as R is bigger than smaller o

ord('R')
#82

ord('o')
#111

colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
print(min(colors, key=lambda s:s.lower()))
print(max(colors, key=lambda s: s.lower()))
#Blue
#Yellow

# Iterating Backwards Through a Sequence
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
reversed_numbers = [item ** 2 for item in reversed(numbers)]
print(reversed_numbers)
#[36, 25, 64, 4, 16, 81, 1, 49, 9, 100]

# Combining Iterables into Tuples of Corresponding Elements
names = ['Bob', 'Sue', 'Amanda']

grade_point_averages = [3.5, 4.0, 3.75]

for name, gpa in zip(names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')

#Name=Bob; GPA=3.5
#Name=Sue; GPA=4.0
#Name=Amanda; GPA=3.75

# Exercise 3
foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']

print(min(foods))
#Bacon

print(min(foods, key=lambda s: s.lower()))
#apples

# Exercise 4
print([(a + b) for a, b in zip([10, 20, 30], [1, 2, 3])])
#[11, 22, 33]
