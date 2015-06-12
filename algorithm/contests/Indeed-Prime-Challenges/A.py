from __future__ import division

def solve(n):
	print ' ' * 2 + "/\\"
	for i in range(n):
		print ' ' * 2 + '||'

	print ' /||\\'
	print '/:||:\\'

	for i in range(n - 1):
		print '|:||:|'

	print '|/||\\|'
	print '  **\n  **'

if __name__ == '__main__':
	n = int(raw_input())
	solve(n)
