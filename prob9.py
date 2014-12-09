"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

import math

# The ranges might check 1 or 2 non-possible values, verify the output
for a in range(1, 501):
    for b in range(a, 501):
        c = math.sqrt(a**2 + b**2)
        if (a + b + c) == 1000:
            print("a=" + str(a) + " b=" + str(b) + " c=" + str(c))
            print("Product is:" + str(a * b * c))

