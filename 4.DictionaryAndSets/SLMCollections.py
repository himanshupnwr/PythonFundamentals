""" Standard library module collections"""

# Python Standard Library Module ‘collections‘
from collections import Counter

text = ('this is sample text with several words '
        'this is more sample text with some different words')


# count occurrences of each unique word
# for word in text.split():
#     if word in word_counts:
#         word_counts[word] += 1  # update existing key-value pair
#     else:
#         word_counts[word] = 1  # insert new key-value pair

# one word method to replace the above code
counter = Counter(text.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of unique keys:', len(counter.keys()))

#Exercise - Challenge

import random
numbers = [random.randrange(1,6) for i in range(50)]

from collections import Counter
counter = Counter(numbers)

for value, count in sorted(counter.items()):
    print(f'{value:<4}{count}')

# 1   12
# 2   7
# 3   13
# 4   7
# 5   11
