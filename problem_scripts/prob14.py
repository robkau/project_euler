"""       
PROBLEM:  The following iterative sequence is defined for the set of positive integers:

                                 n → n/2 (n is even)
                                 n → 3n + 1 (n is odd)

          Using the rule above and starting with 13, we generate the following sequence:

                               13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

          It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
          Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

          Which starting number, under one million, produces the longest chain?
          
APPROACH: We start by defining a recursive function chain(num) that returns the chain length to 1 for a given num.
          By recursively having chain call itself with chain(next_hop) it is assumed we will eventually end at 1.
          When it finds 1, or a previously visited number in the dictionary, it updates the dict with the hop count for
          every node traversed and returns the result.
          With this algorithm, we can repeatedly call this function on a million numbers and it effectively caches
          the previous results in a dict, avoiding unnecessary calculations.
          
RESULT:   It runs in under 5 seconds. This is a successful improvement over the previous brute force method, which
          took over five minutes, and the problem is considered solved.
           
"""

# Construct the base entry in our dictionary.
chain_dict = {1: True}


# Define the function that takes num and returns (num, hops_to_one).
def chain(num):

    # Check if it is already in the dictionary.
    # If it is, return the number and the hop count associated with it.
    if chain_dict.get(num, False):
        return num, chain_dict[num]

    # If we don't know the value yet, call again with the next chain node. Once found we update the cascade with hop
    # counts and return the solution for the original number.
    if num % 2 == 0:
        chain_dict[num] = chain(num/2)[1]+1
        return num, chain_dict[num]
    else:
        chain_dict[num] = chain(num*3 + 1)[1]+1
        return num, chain_dict[num]


# Hold the highest value and loop through the search space.
highest = 0, 0

for i in range(2, 1000001):
    temp = chain(i)
    if temp[1] > highest[1]:
        highest = temp

print("Highest is " + str(highest[0]) + " with " + str(highest[1]) + " hops.")

"""
OUTPUT:   Highest is 837799 with 525 hops.
          
"""