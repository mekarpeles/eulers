import math

def prime(p):
    '''return True if the number is prime, false otherwise'''
    if p < 2: return False
    for i in xrange(2, int(p)):
        if not(p%i):
            return False
    return True

def euler_3(n):
    """Computes the largest prime factor of n's prime factorization"""
    for factor in xrange(2, n):
        compliment = float(n) / factor
        if compliment == n / factor:
            if prime(int(compliment)):
                return int(compliment)

def gcd(a, b):
    """Greatest Common Divisor (i.e. factor) of both a & b"""
    pass

if __name__ == "__main__":
    print euler_3(600851475143)

