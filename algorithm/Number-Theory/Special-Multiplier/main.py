from __future__ import division

def solve(n):
	j = 1
	while (int(str(bin(j))[2:].replace('1', '9')) % n != 0):
		j += 1
	return str(bin(j))[2:].replace('1', '9')

if __name__ == '__main__':
	t = input()
	for _ in range(t):
		n = input()
		print solve(n)