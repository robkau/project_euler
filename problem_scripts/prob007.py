"""
PROBLEM:   By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
           What is the 10001st prime number?

APPROACH:  Generate list of all primes below 1,000,000.
           If the number of primes in that list is less than 10001, generate a new list up to (previous maximum)*10.
           Repeatedly do this until we have enough primes.
           Not too efficient but lets see if the time scale is acceptable.

RESULT:    It works. Runs in less than one second.
           There is a lot of room for optimization here if performance was a requirement or we needed a lot of primes.
           Could use a segmented sieve or other method instead of repeatedly making primes blindly.

"""


def generate_primes(n):
    p = [True] * n

    for i in range(2, n):
        if p[i]:
            check_value = i**2
            while check_value < n:
                p[check_value] = False
                check_value += i
    return p


prime_list_logical = []
prime_list_actual = []
num = 10000

# Keep making more and more primes until we have enough.
while len(prime_list_actual) < 10001:
    prime_list_logical = generate_primes(num)
    prime_list_actual = []
    num *= 10
    num = round(num)

    # Iterate over the boolean list and collapse into a list of primes
    count = 0
    for index in range(2, len(prime_list_logical)):
        if prime_list_logical[index]:
            prime_list_actual.append(index)
            count += 1
    print("Checked {} numbers".format(num))


print("10001st prime is: {}".format(prime_list_actual[10000]))


"""
OUTPUT:   Checked 100000 numbers
          Checked 1000000 numbers
          Checked 10000000 numbers
          10001st prime is: 104743

"""