# Rolling a Six-Sided Die

import random

for roll in range(10):
    print(random.randrange(1,7), end = ' ')


#2 5 6 5 6 1 6 4 6 3

# Seeding the Random-Number Generator for Reproducibility
random.seed(32)

for roll in range(10):
    print(random.randrange(1, 7), end=' ')

#Although the data is random as the seed data is same then the random values will also be same

random.seed(32)

for roll in range(10):
    print(random.randrange(1, 7), end=' ')


#1 2 2 3 6 2 4 1 6 1

#Challenge
    """Roll a six-sided die 6,000,000 times."""
import random

# face frequency counters
frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

# 6,000,000 die rolls
for roll in range(6_00):  # note underscore separators
    face = random.randrange(1, 7)

    # increment appropriate face counter
    if face == 1:
        frequency1 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency3 += 1
    elif face == 4:
        frequency4 += 1
    elif face == 5:
        frequency5 += 1
    elif face == 6:
        frequency6 += 1

print(f'Face{"Frequency":>13}')
print(f'{1:>4}{frequency1:>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency3:>13}')
print(f'{4:>4}{frequency4:>13}')
print(f'{5:>4}{frequency5:>13}')
print(f'{6:>4}{frequency6:>13}')

#1          124
#2          107
#3           93
#4           97
#5           94
#6           85

# Exercise 3
import random

for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T', end=' ')
#produces values either 0 or 1 and then we display h ot t based on that
#T T T T H H T H T T H H H T H H T T T H
