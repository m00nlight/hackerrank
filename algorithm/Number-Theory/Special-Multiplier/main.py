# Not accepted yet

from __future__ import division

def solve(num):
    mul = 1
    while True:
        if set(str(mul * num)) == {'0', '9'}: return mul * num
        mul += 1
    
if __name__ == '__main__':
    n = int(raw_input())
    for _ in range(n):
        num = int(raw_input())
        print solve(num)

