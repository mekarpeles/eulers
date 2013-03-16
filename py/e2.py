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
    
def euler_2(n):
    return fib(n)

if __name__ == "__main__":
    goalp = False
    i = 1
    accum = 0
    tmp = 0
    while not(goalp):
        prev = tmp
        tmp = euler_2(i)
        if tmp + prev > 4000000:
            goalp = True
        elif even(tmp):
            accum += tmp
        i += 1
    print accum
