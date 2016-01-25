num = 600851475143

for i in xrange(1,num,2):
    if(num%i==0):
        print i
        num = num/i
    if(num<i):
        break
