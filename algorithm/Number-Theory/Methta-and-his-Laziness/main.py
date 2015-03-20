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
    
primes = sieve(1010)
    
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
    
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def solve(num):
    facts = factor(num)
    total = reduce(mul, map(lambda x: x[1] + 1, facts), 1) - 1
    if facts[0][0] != 2 or (facts[0][0] == 2 and facts[0][1] < 2): 
        return (0, total)
    else:
        num = facts[0][1] // 2
        num = num * reduce(mul, map(lambda x: x[1] // 2 + 1, facts[1:]), 1)
        
        if all(map(lambda x: x[1] % 2 == 0, facts)):
            num -= 1 
        
        g = gcd(num, total)
        if g is not 0:
            num /= g
            total /= g
        return (num, total)
        
if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        n = int(raw_input())
        a, b = solve(n)
        if a == 0:
            print '0'
        else:
            print '%d/%d' % (a, b)