"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list =[]
    count =0
    i = 1
    while (count <number_of_primes):
        if (i % 2 != 0):
            list.append(i)
            count+=1
        i += 1
    return list


