import math

def prime_bool_list(num):
    num_list = [True] * num
    num_list[0] = num_list[1] = False
    limit_sqrt = math.sqrt(num)

    for count in xrange(2,num):
        if count >= limit_sqrt:
            return num_list

        for composite in range(count ** 2, num, count):
            num_list[composite] = False
NUMBER = 20
prime_list = [i for i, b in enumerate(prime_bool_list(NUMBER)) if b == True]

ans = 1
for i in prime_list:
    square = i
    while square*i < NUMBER:
        square *= i
    ans *= square

print ans
