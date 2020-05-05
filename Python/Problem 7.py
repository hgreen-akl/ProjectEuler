# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

number = 7

def is_prime(n) :
    if (n < 2):
        return False
    elif (n==2):
        return True
    elif (n==3):
        return True
    else:
        for x in range(2,n//2):
            if(n % x==0):
                return False
        return True

def get_nth_prime(x):
    """[Obtains the nth prime number based on a function that is prime]

    Arguments:
        x {[int]} -- [the nth prime number wanted]
    """
    number = 0
    prime_list = []
    while len(prime_list) <=  x:
        if is_prime(number):
            prime_list.append(number)
            number += 1
        else:
            number +=1
    return prime_list[-1]


get_nth_prime(5) # this should be 11
get_nth_prime(6) # this should be 13
get_nth_prime(10001)