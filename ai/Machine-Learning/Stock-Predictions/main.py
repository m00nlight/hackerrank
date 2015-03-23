from __future__ import division
from math import sqrt
from operator import add
from heapq import heappush, heappop

def printTransactions(money, k, d, name, owned, prices):
    def mean(nums):
        return sum(nums) / len(nums)

    def sd(nums):
        average = mean(nums)
        return sqrt(sum([(x - average) ** 2 for x in nums]) / len(nums))

    def info(price):
        cc, sigma, acc = 0, 0.0, 0
        for i in range(1, 5): 
            if price[i] > price[i - 1]: cc += 1
        sigma = sd(price)
        mu = mean(price)
        c1, c2, c3 = mean(price[0:3]), mean(price[1:4]), mean(price[2:5])
        
        return (c1, c2, c3, (price[-1]- price[0]) / price[0])

    
    infos = map(info, prices)
    res = []
    
    up = filter(lambda x: x[0] < x[1] and x[1] < x[2] and x[-1] > 0, infos)
    down = filter(lambda x: x[0] > x[1] and x[1] > x[2] and x[-1] < 0, infos)
    
    up_sum = sum(map(lambda x: x[-1], up))
    down_sum = sum(map(lambda x: x[-1], down))
    
    for i in range(k):
        c1, c2, c3, rate = info(prices[i])
        if c2 >= c1 and c3 >= c2 and owned[i] > 0:
            res.append((name[i], 'SELL', str(owned[i])))
        elif c2 <= c1 and c3 <= c2:
            amount = int(money * rate / down_sum / prices[i][-1])
            if amount > 0: res.append((name[i], 'BUY', str(amount)))
    
    print len(res)
    for r in res:
        print ' '.join(r)
    
    

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