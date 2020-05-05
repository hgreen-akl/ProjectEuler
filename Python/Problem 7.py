# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

number = 7

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n > 2:
        for i in range(n,n//2)":
            if n % i == 0:
                break
        else:
            return False

is_prime(number)