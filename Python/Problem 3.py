# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# This is a very slow method and takes a very long time to run obtian the factors let alone the highest prime number
# TODO: 
#   Need to find a way to improve the efficiency of this code.
#   Could potentially work backwards finding a factor and then if it is a prime number present this value

import numpy as np

def find_prime_factors(number):
    """ Finds the factors in any given number.
        Returns a list of values that are prime factors of that number

    Arguments:
        number {int} -- [must be any integer above 2]

    Returns:
        factors {list} -- [a list of integers that are prime factors of the given number]
    """


    prime_factors = []
    for i in range(2,number):
        if number % i == 0:
            print(i, " is a factor")
            for j in range(2,i//2):
                if (i % j) == 0:
                    break
            else:
                prime_factors.append(i)
    return prime_factors


test = find_prime_factors(13195)
print(test)
answer = find_prime_factors(600851475143)
print(max(answer))