"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

APPROACH:



"""

import math

for a in range(1, 500):
    for b in range(a + 1, 500):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            if (a + b + c) == 1000:
                print("a=" + str(a) + " b=" + str(b) + " c=" + str(c))
                print("Product is:" + str(a * b * c))

"""
OUTPUT:   a=200 b=375 c=425.0
          Product is:31875000.0

"""
