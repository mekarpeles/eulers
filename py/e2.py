def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memod(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)
        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret
    return memod().__getitem__

@memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

def even(x):
    return not(x % 2)

def euluer_2():
    goalp = False
    i = 1
    accum = 0
    tmp = 0
    while not(goalp):
        prev = tmp
        tmp = fib(i)
        print tmp
        if tmp + prev > 4000000:
            goalp = True
        if not(tmp % 2):
            accum += tmp
        i += 1
    return accum

if __name__ == "__main__":
    print euluer_2()
