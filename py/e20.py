import time, timeit

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

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
def fac(n):
    return 1 if n < 1 else n * fac(n-1)

#@timing
def sum_digits1(n):
    """Sums the digits of n by converting it to a string and then
    iterating over its chars as ints

    Ran in 1.7191631794 sec for n=fac(200), 10000 tests
    """
    return sum(map(int, list(str(n))))

#@timing
def sum_digits2(n):
    """Uses modulo and division to sum the digits without str case.

    Expected to be faster, took 2.8842189312 sec for n=fac(200), 10000 tests
    """
    _sum = 0
    while n:
        n, r = divmod(n, 10)
        _sum += r
    return _sum

if __name__ == "__main__":
    n = fac(100)
    print("1: %s" % timeit.timeit(setup='from __main__ import sum_digits1, fac;n=fac(200)',
                        stmt='sum_digits1(n)', number=10000))
    print("2: %s" % timeit.timeit(setup='from __main__ import sum_digits2, fac;n=fac(200)',
                        stmt='sum_digits2(n)', number=10000))
    print(sum_digits1(n))
    print(sum_digits2(n))
