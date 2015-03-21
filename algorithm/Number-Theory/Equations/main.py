from __future__ import division
from collections import defaultdict

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

def solve(num):
	MOD = 1000007 
	facts = defaultdict(int)
	for i in range(2, num+1):
		tmp = factor(i)
		for (base, p) in tmp:
			facts[base] += p

	return reduce(lambda acc, x: acc * (2 * x[1] + 1) % MOD, facts.iteritems(), 1)


if __name__ == '__main__':
	n = int(raw_input())
	print '%d' % solve(n)