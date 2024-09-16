# Creating Tuples
student_tuple = ()
print(student_tuple) #()

len(student_tuple) #0

student_tuple = 'John', 'Green', 3.3
print(student_tuple)

len(student_tuple) #3

another_student_tuple = ('Mary', 'Red', 3.3)
print(another_student_tuple)

a_singleton_tuple = ('red',)  # note the comma that means it not just a string its a tuple
print(a_singleton_tuple) #('red',)

time_tuple = (9, 16, 1)
time_tuple[0] * 3600 + time_tuple[1] * 60 + time_tuple[2]

#Assigning one tuple to another
tuple1 = (10, 20, 30)
tuple2 = tuple1
print(tuple2)

# Adding Items to a String or Tuple
# Tuples are immutable like strings
tuple1 += (40, 50)
print(tuple1) #(10, 20, 30, 40, 50)
print(tuple2) #(10, 20, 30) tuple 2 is not affected by changing the tuple1

# Appending Tuples to Lists. In python we can add one iterable type to another
numbers = [1, 2, 3, 4, 5]
numbers += (6, 7)
print(numbers) #[1, 2, 3, 4, 5, 6, 7]

# Tuples May Contain Mutable Objects like lists
student_tuple = ('Amanda', 'Blue', [98, 75, 87])
student_tuple[2][1] = 85
print(student_tuple)
