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

if __name__ == "__main__":
    n = fac(100)
    print sum(map(int, list(str(n))))
