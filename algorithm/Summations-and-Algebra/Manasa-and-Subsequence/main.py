from __future__ import division

MOD = 10 ** 9 + 7

def solve(s):
    ret = 0
    for idx, ch in enumerate(s):
        ret = (ret + int(ch) * pow(2, idx, MOD) * \
            pow(11, len(s) - idx - 1, MOD)) % MOD
    return ret

if __name__ == '__main__':
    s = raw_input()
    print solve(s)
