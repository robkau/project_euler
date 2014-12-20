"""
PROBLEM:  A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

          a^2 + b^2 = c^2

          For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

          There exists exactly one Pythagorean triplet for which a + b + c = 1000.

          Find the product abc.

APPROACH: The solution to this problem relies on generating the unique right triangle that satisfies the given
          conditions. So we generate possible candidates, check each one, and exit when it is found.

RESULT:   It works.

"""

import math

# Generates candidate triangles, checks given conditions, and outputs when answer is found.
for a in range(1, 500):
    for b in range(a + 1, 500):
        c = math.sqrt(a ** 2 + b ** 2)
        if c.is_integer():
            if (a + b + c) == 1000:
                print("a=" + str(a) + " b=" + str(b) + " c=" + str(c))
                print("Product is:" + str(a * b * c))

"""
OUTPUT:   a=200 b=375 c=425.0
          Product is:31875000.0

"""
