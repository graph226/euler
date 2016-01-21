def fibo(n,a=1,b=2):
    for i in xrange(n-2):
        c = a + b
        a = b
        b = c
    return c

n = input()
print fibo(n)
