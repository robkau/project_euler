"""
PROBLEM:   The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
           The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
           Hence the difference between the sum of the squares of the first ten numbers and the square of the sum is,

                                                     3025 − 385 = 2640.

           Find the difference between the sum of the squares of the first one hundred numbers and the square of the sum

APPROACH:  Loop over the numbers and perform the operations.

RESULT:    It works. Runtime is nearly instant.

"""

sum_of_squares = 0
square_of_sums = 0

for i in (range(1, 101)):
    sum_of_squares += i**2

for i in (range(1, 101)):
    square_of_sums += i

square_of_sums **= 2

print(square_of_sums - sum_of_squares)

"""
OUTPUT:   25164150

"""