numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

for value in (x**2 for x in numbers if x%2 !=0):
    print(value, end=' ')
#9 49 1 81 25

squares_of_odds = (x ** 2 for x in numbers if x % 2 != 0)
print(squares_of_odds)
#<generator object <genexpr> at 0x000001C616103780>

#Exercise generator expression
print(list(x ** 3 for x in [10, 3, 7, 1, 9, 4, 2] if x % 2 == 0))
#[1000, 64, 8]
