def is_prime(n) :
    """[determines whether a number n is a prime number]

    Arguments:
        n {[int]} -- [a postive integer]

    Returns:
        [Bool] -- [Returns True if n is a prime number]
    """    
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