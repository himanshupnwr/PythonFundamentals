months = {'January':1, 'February':2, 'March':3}

months2 = {number: name for name, number in months.items()} #revert the dictionary using comprehension

print(months2)
# {1: 'January', 2: 'February', 3: 'March'}

grades = {'Sue': [98, 87, 94], 'Bob': [84, 95, 91]}

grades2 = {k: sum(v) / len(v) for k, v in grades.items()}

print(grades2)

#{'Sue': 93.0, 'Bob': 90.0}

#Exercise
dictExample = {number: number ** 3 for number in range(1, 6)}
print(dictExample)
#{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
