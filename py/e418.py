import json
from math import ceil, sqrt

def fac(n):
    return 1 if n < 2 else n * fac(n - 1)

def divs(n):
    ds = set()
    # Heuristic which leverages primality to prune the search space
    if (n % 2) or (n % 3):
        return ds
    upper = int(ceil(sqrt(n)))
    lower = 1
    with open('e418.out', 'w') as fout:
        while lower <= upper:
            if not (n % lower):
                #ds.add(upper)
                #ds.add(n/upper)
                json.dump((lower, n/lower), fout)
            lower += 1
    return ds

if __name__ == "__main__":
    print divs(fac(43))
    #fac(43) == 60415263063373835637355132068513997507264512000000000
    #n == a * b * c
