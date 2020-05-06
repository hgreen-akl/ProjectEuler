# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
# This is a very Slow function due to the large amount of processing and memory storage
import sys, os
from tqdm import tqdm
from useful_functions.prime import is_prime
import numpy as np

prime_below_2m = 0
for i in tqdm(range(1,2000000)):
    if is_prime(i) == True:
        prime_below_2m += i

print(prime_below_2m)
