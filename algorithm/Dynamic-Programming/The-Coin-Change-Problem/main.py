
def solve(M, coins):
    res = [0] * (M + 1)
    res[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], M + 1):
            res[j] = res[j] + res[j - coins[i]]

    return res[M]

if __name__ == '__main__':
    M, N = map(int, raw_input().strip().split())
    coins = map(int, raw_input().strip().split())
    print solve(M, coins)