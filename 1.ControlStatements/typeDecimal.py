amount = 112.31

print(amount)

print(f'{amount:.20f}')

#importing Type Decimal from the decimal Module
from decimal import Decimal

#Creating Decimals
principal = Decimal('1000.00')
print(principal)

rate = Decimal('0.05')
print(rate)

#Decimal Arithmetic
x = Decimal('10.5')
y = Decimal('2')
print(x+y)
print(x//y)
print(x)

#calculating compound Interest
for year in range(1,11):
    amount = principal * (1+rate) ** year
    print(f'{year:>2}{amount:>10.2f}') #:>2 take year and right align by one space

    #:>2 field width is two spaces now this helps in aligning 1 and 10 in similar spaces

#1   1050.00
#2   1102.50
#3   1157.62
#4   1215.51
#5   1276.28
#6   1340.10
#7   1407.10
#8   1477.46
#9   1551.33
#10   1628.89

#challenge
#Assume that the tax on a bill is 6.25% and that the bill amount is $37.45.
#Use type decimal to calculate the bill total then print the result with two
#digits to the right of the decimal point
print(f'{Decimal(37.45) * Decimal('1.0625'):.2f}')
