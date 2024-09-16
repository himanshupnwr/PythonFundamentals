def square(number):
    print("""Calculate the square of number.""")
    return number ** 2

print(square(7))

print(square(2.5))

# Returning a Result to a Function’s Caller
print('The square of 7 is', square(7))

# Exercise 3
def square_root(number):
    return number ** 0.5  # or number ** (1 / 2)

print(square_root(6.25))
