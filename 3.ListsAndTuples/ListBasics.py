#should be homogenous but can be heterogenous well
#python does not has arrays, closest to it we have lists

numList = [-45, 6, 0, 72, 1543]

# Accessing Elements of a List
numList[0]
numList[4]

listLen = len(numList)

# Accessing Elements from the End of the List with Negative Indices
numList[-1]
numList[-5]

# Lists Are Mutable
numList[4] = 17

# Some Sequences Are Immutable like strings
s = 'hello'
s[0]
#s[0] = 'H' # exception 'str' object does not support item assignment

# Appending to a List with +=
a_list = []

for number in range(1, 6):
    a_list += [number]


letters = []
letters += 'Python'
print(letters) #['P', 'y', 't', 'h', 'o', 'n']

list1 = [10, 20, 30]
list2 = [40, 50]
concatenated_list = list1 + list2
print(concatenated_list) #[10, 20, 30, 40, 50]

# Using for and range to Access List Indices and Values
for i in range(len(concatenated_list)):
    print(f'{i}: {concatenated_list[i]}')

# Comparison Operators
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3, 4]

print(a == b)
print(a == c)
print(a < c)
print(c >= b)

#True
#False
#True
#True

# Exercise 3

def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cube_list(numbers)

print(numbers)

# Exercise 4
characters = []
characters += 'Birthday'
print(characters)

#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#['B', 'i', 'r', 't', 'h', 'd', 'a', 'y']
