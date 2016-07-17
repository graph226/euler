NUM = 10001

def prime_order(num):
    prime_list = [2]
    count = 2
    while len(prime_list) < num:
        for prime in prime_list:
            if count % prime == 0:
                break
        else:
            prime_list.append(count)
        count += 1
    return prime_list

print prime_order(NUM)
