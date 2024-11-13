# Creating a Set with Curly Braces , sets ignores the duplicate, does not care about the order
colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(colors)
#{'green', 'blue', 'red', 'orange', 'yellow'}

# Checking Whether a Value Is in a Set
# 'red' in colors
# 'purple' in colors
# 'purple' not in colors

# Iterating Through a Set
for color in colors:
    print(color.upper(), end=' ')
#RED BLUE ORANGE YELLOW GREEN

# Creating a Set with the Built-In set Function
numbers = list(range(10)) + list(range(5))
print(numbers)

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]

setNumbers = set(numbers)
print(setNumbers)
#{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# Exercise 3
text = 'to be or not to be that is the question'

unique_words = set(text.split())

for word in sorted(unique_words):
    print(word, end='  ')
#be  is  not  or  question  that  the  to

#Compare Sets

print({1,3,5} == {3,5,1})
#True

print({1, 3, 5} != {3, 5, 1})
# False

print({1, 3, 5} < {3, 5, 1})
# False

print({1, 3, 5} < {7, 3, 5, 1})
# True

print({1, 3, 5} <= {3, 5, 1})
# True

print({1, 3} <= {3, 5, 1})
# True

print({1, 3, 5}.issubset({3, 5, 1}))
# True

print({1, 2}.issubset({3, 5, 1}))
# False

print({1, 3, 5} > {3, 5, 1})
# False

print({1, 3, 5, 7} > {3, 5, 1})
# True

print({1, 3, 5} >= {3, 5, 1})
# True

print({1, 3, 5} >= {3, 1})
# True

print({1, 3} >= {3, 1, 7})
# False

print({1, 3, 5}.issuperset({3, 5, 1}))
# True

print({1, 3, 5}.issuperset({3, 2}))
# False

# Exercise 3 - going to check one character at a time
value = set('abc def ghi jkl mno').issuperset('hi mom')
print(value)
#True

# Union
{1, 3, 5} | {2, 3, 4}

{1, 3, 5}.union([20, 20, 3, 40, 40])

# Intersection
{1, 3, 5} & {2, 3, 4}
#{3}

{1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4])
#{1,3}

# Difference
{1, 3, 5} - {2, 3, 4}
#{1,5}

{1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4])
#{1,5,7}

# Symmetric Difference
{1, 3, 5} ^ {2, 3, 4}
#{1,2,4,5}

{1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4])
#{1,2,4,5,7}

# Disjoint
{1, 3, 5}.isdisjoint({2, 4, 6})
#true

{1, 3, 5}.isdisjoint({4, 6, 1})
#false

# Exercise 2
{10, 20, 30} - {5, 10, 15, 20}
#{30}

{10, 20, 30} ^ {5, 10, 15, 20}
#{5,10,15}

{10, 20, 30} | {5, 10, 15, 20}
#{5,10,15,20,30}

{10, 20, 30} & {5, 10, 15, 20}
#{10,20}


#Mutable Set Operations - modify the set
#|= -> update
#&= -> intersection_update
#-= -> difference update
#^= -> symmetric difference update

# Mutable Mathematical Set Operations
numbers = {1, 3, 5}
numbers |= {2, 3, 4}
print(numbers)

numbers.update(range(10))
print(numbers)

numbers.add(17)
numbers.add(3)

numbers.remove(3)
numbers.pop()

numbers.clear()
#set()

#set comprehension - similar to dict comprehension
numbers = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]

evens = {item for item in numbers if item % 2 == 0}

evens
