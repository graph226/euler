"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

LIMIT = 1000
A_LIMIT = LIMIT/3

for i in range(1, A_LIMIT):
    for j in range(i+1, (LIMIT-i)/2):
        k = 1000 - i - j
        if i < j < k:
            if i**2 + j**2 == k**2:
                print i,j,k
                a = i
                b = j
                c = k
        else:
            continue

print a,b,c
print a*b*c
