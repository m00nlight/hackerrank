from __future__ import division
from operator import mul

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    prime_list = [2]
    for i in range(4,limit + 1, 2):
        is_prime[i] = False
    
    i, j = 3, 0
    for i in range(3, limit + 1, 2):
        if is_prime[i]: prime_list.append(i)
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False
    
    while i <= limit:
        if is_prime[i]: prime_list.append(i)
        i += 2
    return prime_list
    
primes = sieve(40000)
    
def factor(num):
    i = 0
    ret = []
    while i < len(primes) and num != 1:
        if num % primes[i] == 0:
            cc = 0
            while num % primes[i] == 0:
                num /= primes[i]
                cc += 1
            ret.append((primes[i], cc))
        i += 1
    
    if num > 1: 
        ret.append((num, 1))
    return ret
    
def solve(num):
    if num == 1: return 0
    facts = factor(num)
    if facts[0][0] != 2:
        return 0
    else:
        return facts[0][1] * reduce(mul, map(lambda x: x[1] + 1, facts[1:]), 1)
    
if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        print '%d' % solve(n)