c = 0
MAX = 4000000
ans = 2
a = 1
b = 2

while c < MAX:
    c = a + b
    a = b
    b = c
    print c,
    if c%2==0:
        ans += c

print "ans:"+str(ans)
