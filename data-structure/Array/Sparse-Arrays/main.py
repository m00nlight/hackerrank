from __future__ import division
from sys import stdin
from collections import defaultdict

if __name__ == '__main__':
    n = int(stdin.readline())
    words = []
    for _ in range(n):
        words.append(stdin.readline().strip())

    freq = defaultdict(int)
    for word in words:
        freq[word] += 1

    q = int(stdin.readline())
    for _ in range(q):
        qword = stdin.readline().strip()
        print('%d' % freq[qword])
