"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes == 1:
        list.append()
    else:
        for i in range(2, number_of_primes):
            if i/1 ==i and i / i ==1 and (i%2 != 0 or i == 2):
                list.append(i)
    return list
