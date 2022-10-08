"""List of prime numbers generator."""
"""Salihah Alnahdi K20055346"""

def primes(number_of_primes):
    list = []
    count = 1
    while True:
        if number_of_primes <= 0:
            return list
            break
        if count > 1:
            for i in range(2,count):
                if (count % i) == 0:
                    break
            else:
                list.append(count)
        if (len(list) == number_of_primes):
            print(list)
            break
        else:
            count += 1
            continue
    return list

