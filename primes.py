"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes > 1:
        for num in range(2, int(number_of_primes**0.5) + 1):
            if number_of_primes % num != 0:
                for j in range(2,number_of_primes):
                    list.append(num)
            return list
    else:
        list.append[2]


