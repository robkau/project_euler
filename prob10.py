"""       
PROBLEM:  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

          Find the sum of all the primes below two million.
          
APPROACH: Try the Sieve of Eratosthenes and see if the time scale is acceptable.
          
RESULT:   Runtime is nearly instant.
           
"""

from tools import generate_primes as gp

print(sum(gp.sieve(2000000)))

"""
OUTPUT:   142913828922
          
"""