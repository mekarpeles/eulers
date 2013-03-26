from math import sqrt, ceil
from itertools import product

def triangle_numbers(n):
    return (n*(n+1))/2

def divs(n):
    ds = set()
    # Heuristic which leverages primality to prune the search space
    if (n % 2) or (n % 3):
        return ds
    for i in xrange(int(ceil(sqrt(n))), 0, -1):
        if not (n % i):
            ds.add(i)
            ds.add(n/i)
    return ds

def e12():
    """Learnings
    1. http://en.wikipedia.org/wiki/Highly_composite_number ->
    2. http://oeis.org/A005179 ->
    3. http://oeis.org/A005179/b005179.txt
    4. First number w/ 500 divisors: 62370000
    triangle_numbers(11169) > 62370000

    5. first # > 501 divisors: 841824943102600080885322463644579019321817144754176

    SOLUTION! 20736
    """
    i = 1
    tn = triangle_numbers(i)
    ds = divs(tn)
    while len(ds) < 501:
        tn = triangle_numbers(i)
        ds = divs(tn)
        print tn, len(ds)
        i += 1
    return i, tn

if __name__ == "__main__":
    print e12()
