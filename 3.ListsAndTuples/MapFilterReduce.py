# Filtering a Sequence’s Values with the Built-In filter Function

#Filter and map are higher order functions - functions that receive other functions as arguments
# Functions are objects - can be assigned to variables, passed to functions, returned from functions
# you can pass named functions or lambdas

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 != 0

print(list(filter(is_odd, numbers)))
#[3, 7, 1, 9, 5]

list1 = [item for item in numbers if is_odd(item)]
print(list1)
#[3, 7, 1, 9, 5]

#Using a lambda rather than a function
print(list(filter(lambda x:x %2!=0, numbers)))
#[3, 7, 1, 9, 5]

print(list(map(lambda x: x**2, numbers)))
#[100, 9, 49, 1, 81, 16, 4, 64, 25, 36]

#combining filer and map
list3 = list(map(lambda x:x **2, filter(lambda x:x % 2 !=0, numbers)))
print(list3)
#[9, 49, 1, 81, 25]

list2 = [x ** 2 for x in numbers if x % 2 != 0]
print(list2)
#[9, 49, 1, 81, 25]


#Exercise
numbersList = list(range(1,6))
print(numbersList)
#[1, 2, 3, 4, 5]

listEx1 = list(filter(lambda x:x % 2 == 0, numbersList))
print(listEx1)
#[2, 4]

listEx2 = list(map(lambda x:x ** 2, numbersList))
print(listEx2)
#[1, 4, 9, 16, 25]

listEx3 = list(map(lambda x:x ** 2, filter(lambda x:x % 2 == 0, numbersList)))
print(listEx3)
#[4, 16]

fahrenheit = [41, 32, 212]
print(list(map(lambda x:(x - 32) * 5/9, fahrenheit)))
#[5.0, 0.0, 100.0]
