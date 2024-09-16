# Section 6.2.4 snippets

months = {'January': 1, 'February': 2, 'March': 3}

for month_name in months.keys():
    print(month_name, end='  ')

for month_number in months.values():
    print(month_number, end='  ')

# Dictionary Views
months_view = months.keys()

for key in months_view:
    print(key, end='  ')

months['December'] = 12
print(months)

for key in months_view:
    print(key, end='  ')
#January  February  March  December

# Converting Dictionary Keys, Values and Key–Value Pairs to Lists
list(months.keys())
list(months.values())
list(months.items())

# Processing Keys in Sorted Order

for month_name in sorted(months.keys()):
    print(month_name, end='  ')
