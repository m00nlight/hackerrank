r9, r3 = range(9), range(3)
bd = [[0 for _ in r9] for _ in r9]
row = lambda r: {bd[r][j] for j in r9}-{0}
col = lambda c: {bd[i][c] for i in r9}-{0}
grid = lambda (r,c): {bd[r*3+i][c*3+j] for i in r3 for j in r3}-{0}
def dfs():
	r,c = f()
	if r is -1 and c is -1: return 1
	else:
		for ch in range(1, 10):
			if sf(r,c,ch):
				bd[r][c]=ch
				if dfs():return 1
				bd[r][c]=0
		return 0		
def f():
	n,x,y = 9,-1,-1
	for i in r9:
		for j in r9:
			if bd[i][j]==0:
				t = ccs(i,j)
				if t<n:n,x,y = t,i,j
	return x,y
def sf(r,c,ch):
	gr, gc = r//3, c//3
	sr = lambda (r,ch):all(x!=ch for x in row(r))
	sc = lambda (c,ch):all(x!=ch for x in col(c))
	sg = lambda (r,c,ch):all(x!=ch for x in grid((gr, gc)))
	return sr((r,ch)) and sc((c,ch)) and sg((gr,gc,ch))
def ccs(r, c):
	cc = set(range(1, 10))
	gr, gc = r//3, c//3
	return len(cc-row(r)-col(c)-grid((gr, gc)))
n = input()
for i in range(n):
	for i in r9:
		bd[i]=map(int,raw_input().split())
	dfs()
	for r in bd: print ' '.join(map(str,r))