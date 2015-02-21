"""       
PROBLEM:  Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
          exactly 6 routes to the bottom right corner.

                                            (Image Omitted).

          How many such routes are there through a 20×20 grid?
          
APPROACH: Look at this as a problem of combinations and permutations.

          If the grid is n x n, we need to make n moves right and n moves down. Let a right move be a 1, and a down move
          be a 0, and the answers now look like binary strings.

          For a 2x2 grid, here are the answers:
          1100
          1010
          1001
          0011
          0101
          0110

          This is a Permutation with Repetition of Indistinguishable Objects
             - http://www.regentsprep.org/regents/math/algebra/apr2/LpermRep.htm

          Our formula for a n x n grid now looks like -   (2n)! / (n! * n!)

          
RESULT:   It works but the final digits got cut off. Try reformatting the output.1
           
"""
import math

print((math.factorial(2*20) / (math.factorial(20) * math.factorial(20))))





"""
OUTPUT:   137846528820
          
"""