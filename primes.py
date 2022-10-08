"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes > 1:
        for num in range(2, int(number_of_primes**0.5) + 1):
            if number_of_primes % num == 0:
                return False
        return True
    return False

def main():
    primers = []
    for i in range(100, 301):
        if primes(i):
            primers.append(i)
    print(primers)

main()


