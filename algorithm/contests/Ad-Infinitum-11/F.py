from __future__ import division

def init(n):
    phi = [i for i in range(n + 1)]
    prm = [i for i in range(n + 1)]
    two = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i): 
                phi[j] -= phi[j] // i
                prm[j] = i
        j = i
        while j > 1:
            p = prm[j]
            two[i] += two[p - 1]
            j //= p

    two[1] = 0

    return (phi, two)

if __name__ == '__main__':
    phi, two = init(2 * 10 ** 6 + 11)
    t = input()
    queries = []
    for _ in range(t):
        queries.append(map(int, raw_input().strip().split()))

    def solve(a, b, c, d, e, f, g, h):
        ret = 0
        if a > 1 or c > 1 or e > 1 or g > 1:
            ret = ret +  b * two[a] + d * two[c] + f * two[e] + h * two[g]
            if a & c & e & g & 1 != 0: ret += 1
        return ret

    for i in range(t):
        print solve(*queries[i])

