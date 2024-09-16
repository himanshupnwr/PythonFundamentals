"""Class average program with sequence-controlled repetition"""

# initialization phase
total = 0 # sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94] #list of 10 grades

#processing phase
for grade in grades:
    total+=grade #add current grade to the running total
    grade_counter +=1 #indicate that one more grade was processes

#termination phase
average = total / grade_counter
print(f'Class average is {average}')

# Section 3.10 Self Check snippets
number1 = 7
number2 = 5
print(f'{number1} times {number2} is {number1 * number2}')
