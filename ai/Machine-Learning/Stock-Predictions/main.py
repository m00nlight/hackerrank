from __future__ import division
from math import sqrt

def printTransactions(m, k, d, name, owned, prices):
    def avg(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = avg(nums)
        return sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        cc, sigma, acc = 0, 0.0, 0
        for i in range(1, 5): 
            if price[i] > price[i - 1]: cc += 1
        sigma = sd(price)
        acc = price[-1] - price[0]
        return (cc, sigma, price[-1], acc)

    
    infos = map(info, prices)
    print infos

if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)