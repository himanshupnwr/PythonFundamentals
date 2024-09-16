list1 = []
for item in range(1,6):
    list1.append(item)

print(list1)
#[1, 2, 3, 4, 5]
#using the list comprehension to create a list of integers

list2 = [item for item in range(1,6)]
print(list2)
#[1, 2, 3, 4, 5]

list3 = [item ** 3 for item in range(1,6)]
print(list3)
#[1, 8, 27, 64, 125]

list4 = [item for item in range(1,11) if item %2 == 0]
print(list4)

#List comprehension that processes another list's elements
colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [item.upper() for item in colors]
print(colors2)
#['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE']
print(colors)
#['red', 'orange', 'yellow', 'green', 'blue']

#Tuple comprehension
cubes = [(x, x**3) for x in range(1,6)]
print(cubes)
#[(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]

multiples = [x for x in range(3,30,3)]
print(multiples)
#[3, 6, 9, 12, 15, 18, 21, 24, 27]
