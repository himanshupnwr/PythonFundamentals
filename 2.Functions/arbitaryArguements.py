# Defining a Function with an Arbitrary Argument List
def average(*args):
    return sum(args) / len(args)

average(5, 10)

average(5, 10, 15)

average(5, 10, 15, 20)

# Passing an Iterable’s Individual Elements as Function Arguments
grades = [88, 75, 96, 55, 83]

average(*grades)
