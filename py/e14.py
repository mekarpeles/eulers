def collatz(n):    
    if type(n) is not list:
        n = [n]
    x = n[-1]
    if x == 1:
        return n
    if x % 2: # leaves remainder (aka odd)
        n.append((3 * x) + 1)
    else:
        n.append(x / 2)
    return collatz(n)

if __name__ == "__main__":
    longest = 1, len(collatz(1))
    for i in xrange(2,1000000):
        c = collatz(i)
        longest = (i, len(c)) if  len(c) > longest[1] else longest
    print "answer: %s, %s" % longest
