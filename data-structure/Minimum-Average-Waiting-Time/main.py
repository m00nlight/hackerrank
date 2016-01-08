from __future__ import division 
from heapq import heappush, heappop

def solve(n, ts, ls):
    queue, wtime, i = [], 0, 1
    info = sorted(zip(ts, ls))

    heappush(queue, info[0][::-1])
    previous = info[0][0]
    
    while queue:
        last, arrving = heappop(queue)
        previous = previous + last
        wtime = wtime + previous - arrving
        while i < n and info[i][0] <= previous:
            heappush(queue, info[i][::-1])
            i += 1

    return wtime // n


if __name__ == '__main__':
    n = int(raw_input())
    ts, ls = [], []
    for i in xrange(n):
        t, l = map(int, raw_input().strip().split())
        ts.append(t)
        ls.append(l)
    print solve(n, ts, ls)