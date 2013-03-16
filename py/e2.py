
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
    
def euler_2(n):
    return fib(n)

if __name__ == "__main__":
    for i in range(10):
        print euler_2(i)

