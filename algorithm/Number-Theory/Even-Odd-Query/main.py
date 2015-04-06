from __future__ import division

def query(arr,x, y):
    if x == y:
        return 'Even' if arr[x] % 2 is 0 else 'Odd'
    else:
        if arr[x + 1] == 0:
            return 'Odd'
        else:
            return 'Even' if arr[x] % 2 is 0 else 'Odd'

if __name__ == '__main__':
    _ = raw_input()
    arr = map(int, raw_input().strip().split())
    q = int(raw_input())
    arr = [0] + arr
    for _ in xrange(q):
        x, y = map(int, raw_input().strip().split())
        print query(arr, x, y)