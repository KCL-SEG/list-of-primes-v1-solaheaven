"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes ==0:
        return []
    else:
        for i in range(number_of_primes):
            if i % 1==0 and i % i ==0:
                list.append(i)
    return list
