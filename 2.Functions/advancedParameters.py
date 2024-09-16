#pass by reference

x = 7

print(id(x))

def cubeFirst(number):
    print('id(number)', id(number))
    return number ** 3

cubeFirst(7)

#140731921201784
#id(number) 140731921201784

def cube(number):
    print('id(number) before modifying number:', id(number))
    number **= 3
    print('id(number) after modifying number:', id(number))
    return number

cube(x)

print(f'x = {x}; id(x) = {id(x)}')

#id(number) before modifying number: 140731921201784
#id(number) after modifying number: 2005215516976
#x = 7; id(x) = 140731921201784

# Exercise 3
width = 15.5

print('id:', id(width), ' value:', width)

width = width * 3

print('id:', id(width), ' value:', width)

#id: 1848239342352  value: 15.5
#id: 1848235830352  value: 46.5
