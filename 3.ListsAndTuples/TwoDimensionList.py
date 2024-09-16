# Creating a Two-Dimensional List
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

# Illustrating a Two-Dimensional List

# Identifying the Elements in a Two-Dimensional List
for row in a:
    for item in row:
        print(item, end=' ')
    print()

#77 68 86 73
#96 87 89 81
#70 90 86 81

# How the Nested Loops Execute
for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()

#a[0][0]=77  a[0][1]=68  a[0][2]=86  a[0][3]=73
#a[1][0]=96  a[1][1]=87  a[1][2]=89  a[1][3]=81
#a[2][0]=70  a[2][1]=90  a[2][2]=86  a[2][3]=81

# Exercise 4
t = [[10, 7, 3], [20, 4, 17]]

total = 0
items = 0

for row in t:
    for item in row:
        total += item
        items += 1

print(total / items)

total = 0
items = 0

for row in t:
    total += sum(row)
    items += len(row)

print(total / items)

#10.166666666666666
