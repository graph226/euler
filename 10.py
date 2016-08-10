import math

def get_prime_list(limit):
    limit_sqrt = int(math.ceil(math.sqrt(limit)))
    prime_bool_list = [False] * 2 + [True] * (limit - 2)
    for prime_cand in xrange(2, limit_sqrt):
        if prime_bool_list[prime_cand]:
            for composite in range(prime_cand ** 2, limit, prime_cand):
                prime_bool_list[composite] = False
    return [i for i, b in enumerate(prime_bool_list) if b]

LIMIT = 2000000
primt_list = get_prime_list(LIMIT)
print sum(primt_list)
