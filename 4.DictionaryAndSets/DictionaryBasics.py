#Keys are case sensitive
country_codes = {'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
print(country_codes)

# Determining if a Dictionary Is Empty
len(country_codes)

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

country_codes.clear()

if country_codes:
    print('country_codes is not empty')
else:
    print('country_codes is empty')

# Exercise 3
states = {'VT': 'Vermont', 'NH': 'New Hampshire', 'MA': 'Massachusetts'}

print(states)

days_per_month = {'January': 31, 'February': 28, 'March': 31}

print(days_per_month)

for month, days in days_per_month.items():
    print(f'{month} has {days} days')

#Basic Dictionary Operations

# 6.2.3 Basic Dictionary Operations
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}

# Accessing the Value Associated with a Key
roman_numerals['V']

# Updating the Value of an Existing Key–Value Pair
roman_numerals['X'] = 10

# Adding a New Key–Value Pair
roman_numerals['L'] = 50

# Removing a Key–Value Pair
del roman_numerals['III']

roman_numerals.pop('X')
print(roman_numerals)


# Attempting to Access a Nonexistent Key
roman_numerals['III']
roman_numerals.get('III')
roman_numerals.get('III', 'III not in dictionary')

roman_numerals.get('V')

# Testing Whether a Dictionary Contains a Specified Key
'V' in roman_numerals
'III' in roman_numerals
'III' not in roman_numerals

# Exercise 3
roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
roman_numerals['x'] = 10
print(roman_numerals)
