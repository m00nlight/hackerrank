from __future__ import division
from random import randint

def gen(n):
	q = randint(1, 10)
	print '%d %d' % (n, q)
	print ' '.join(map(lambda _: str(randint(0, 1)), range(n)))
	for _ in range(q):
		op = randint(1, 2)
		if op == 1:
			a, b = randint(1, n), randint(1, n)
			if b < a:
				a, b = b, a
			print '%d %d %d' % (op, a, b)
		else:
			a, v = randint(1, n), randint(0, 4)
			print '%d %d %d' % (op, a, v)

if __name__ == '__main__':
	gen(100)
