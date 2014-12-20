"""
A few functions to generate prime numbers
"""


# An implementation of the Sieve of Eratosthenes.
# Returns a list of all primes below the number n
# While this function will work for relatively small numbers of primes, there are more efficient algorithms.
def sieve(n):

    # Generates a boolean list of length n with True elements representing prime indexes. Non-primes are False.
    primes = [True] * n
    for i in range(2, n):
        if primes[i]:
            check_value = i**2
            while check_value < n:
                primes[check_value] = False
                check_value += i

    # Collapses the True/False index list into a list of only prime numbers and returns
    primes_list = []
    for index in range(2, len(primes)):
        if primes[index]:
            primes_list.append(index)

    return primes_list



