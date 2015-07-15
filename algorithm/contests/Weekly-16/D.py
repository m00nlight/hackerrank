from __future__ import division
from sys import stdin

mod = 10 ** 9 + 7

def subset(n, m, skills, target):
    dp = [0] * ((1 << m) + 1)
    twomod = [0] * ((1 << 21) + 1)
    twomod[0] = 1
    for i in range(1, 1 << 21):
        twomod[i] = (twomod[i - 1] * 2) % mod

    twomod = map(lambda x: (x - 1 + mod) % mod, twomod)


    for s in skills:
        dp[s] += 1

    for i in range(m):
        for j in range(1 << m):
            if (j & (1 << i)):
                dp[j] += dp[j ^ (1 << i)]

    ret = 0
    for i in range(target, -1, -1):
        if (i | target) <= target:
            if bin(i^target)[2:].count('1') % 2 == 0:
                ret = (ret + twomod[dp[i]]) % mod
            else:
                ret = (ret - twomod[dp[i]] + mod) % mod
    return ret

if __name__ == '__main__':
    n, m = map(int, stdin.readline().strip().split())
    skills = []
    for _ in range(n):
        skills.append(int(stdin.readline().strip(), 2))

    target = int(stdin.readline().strip(), 2)
    print subset(n, m, skills, target)
