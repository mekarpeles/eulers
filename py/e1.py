def multsof(ubound, ms=[3,5]):
    """Naive (unoptimized) solution to find all multiples of ms below
    ubound
    """
    def goalp(num):
       return any([not(num % n) for n in ms])
    return filter(goalp, xrange(1, ubound))

def euler_1(ubound, ms=[3,5]):
    """Find the sum of all multiple of ms below ubound"""
    return sum(multsof(ubound, ms=ms))

def golf(u, ms):
    """golf: concise solution, min(keystrokes)"""
    return sum(filter(lambda n:any([not(n%m) for m in ms]), xrange(1, u)))

if __name__ == "__main__":
    assert(golf(1000, [3,5]) == euler_1(1000, [3,5]))
    print euler_1(1000, [3,5])
