from __future__ import division

def solve(rating):
    n = len(rating)
    candies = [1] * n
    for i in range(1, n):
        if rating[i] > rating[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if rating[i] > rating[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

if __name__ == '__main__':
    n = int(raw_input())
    rating = []
    for _ in range(n):
        rating.append(int(raw_input()))

    print solve(rating)