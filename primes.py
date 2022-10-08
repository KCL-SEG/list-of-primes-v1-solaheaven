"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list =[]
    count =0
    i = 1
    if number_of_primes == 1:
        list.append[2]
    else:
        while (count <number_of_primes+2):
          if (count % i != 0):
            list.append(i)
            count+=1
          i += 1
    return list


