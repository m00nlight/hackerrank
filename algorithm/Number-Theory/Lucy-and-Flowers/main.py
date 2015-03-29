from __future__ import division

MAXN = 5050
MOD = 10 ** 9 + 9

def modinv(n, p):
    return pow(n, p - 2, p)

def gen_catalan(n):
    res = [1]
    for i in range(1, n + 1):
        res.append(2 * (2 * i - 1) * res[-1] * modinv(i + 1, MOD) % MOD)

    return res

def gen_answers(n):
    catalans = gen_catalan(MAXN)
    ret = [0] * (n + 1)
    C = [1]
    for i in range(1, n + 1):
        res = 0
        C = map(lambda (x, y): (x + y) % MOD, zip(C + [0], [0] + C))
        for j in range(1, i + 1):
            res = (res + C[j] * catalans[j]) % MOD

        ret[i] = res
    return ret

def solve(i, ans):
    return ans[i]

if __name__ == '__main__':
    n = int(raw_input())
    ans = gen_answers(MAXN - 1)
    for _ in range(n):
        idx = int(raw_input())
        print solve(idx, ans)
