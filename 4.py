ans = 0
for i in xrange(1,1000):
    for j in xrange(1,1000):
        tmp = i*j
        normal = str(i*j)
        reverse = normal[::-1] # get reversed string
        if normal==reverse and tmp>ans:
            ans = tmp   # tmp is max

print ans
