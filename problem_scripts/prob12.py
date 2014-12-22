"""       
PROBLEM:  The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would
          be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

          1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

          Let us list the factors of the first seven triangle numbers:

           1: 1
           3: 1,3
           6: 1,2,3,6
          10: 1,2,5,10
          15: 1,3,5,15
          21: 1,3,7,21
          28: 1,2,4,7,14,28

          We can see that 28 is the first triangle number to have over five divisors.

          What is the value of the first triangle number to have over five hundred divisors?
          
APPROACH: Generate one million triangle numbers and check each for factor count. See if the running time is acceptable.

RESULT:   It completes successfully in less than 10 seconds.
           
"""


import functools


# Function to factor a number efficiently.
def factors(n):
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Generate the first million triangle numbers and see if we find one with more than 500 factors.
nums = list()
nums.append(0)
for j in range(1, 1000001):
    nums.append(nums[j-1] + j)
    if len(factors(nums[j])) > 500:
        print("Found first 500 factor num: " + str(nums[j]) + " with " + str(len(factors(nums[j]))) + " factors")
        break


"""
OUTPUT:   Found first 500 factor num: 76576500 with 576 factors
          
"""