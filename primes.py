"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    if number_of_primes == 1:
        list.append(2)
    else:
        for i in range(2, number_of_primes+1):
            if i > 1:
                for j in range(2,i):
                    if(i%j)==0:
                        break
                else:

                    list.append(i)
    return list
