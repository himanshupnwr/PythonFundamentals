for number in range(5,10):
    print(number, end=' ')

#5 6 7 8 9

for number in range(0, 10, 2):
    print(number, end=' ')
#0 2 4 6 8

for number in range(10, 0, -2):
    print(number, end=' ')
#10 8 6 4 2

# Exercise 2
for number in range(10, 0, 2):
    print(number, end=' ')


# Exercise 3
for number in range(99, -1, -11):
    print(number, end=' ')

# Exercise 4
total = 0
for number in range(2, 101, 2):
    total += number

print(total)
