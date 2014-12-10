"""
A few methods to generate prime numbers
"""


# An implementation of the Sieve of Eratosthenes.
# Returns a list of all primes below the number n
# While this method will work for relatively small numbers of primes, the others in this file are more efficient.
def sieve(n):

    # Generates a boolean list of length n with True elements representing prime indexes
    primes = [True] * n
    for i in range(2, n):
        if primes[i]:
            check_value = i**2
            while check_value < n:
                primes[check_value] = False
                check_value += i

    # Collapses the primes list into a list of only prime numbers and returns
    primes_list_actual = []
    for index in range(2, len(primes)):
        if primes[index]:
            primes_list_actual.append(index)

    return primes_list_actual



