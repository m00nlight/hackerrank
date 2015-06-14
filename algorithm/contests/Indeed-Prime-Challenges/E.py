from __future__ import division

eps = 0.02

def solve(series):
	def is_square():
		for (t, f) in series:
			if abs(f - 1.0) > eps and abs(f + 1.0) > eps:
				return False
		return True

	flag = is_square()

	if flag:
		start = 0
		while start < len(series) - 1 and abs(series[start + 1][1] - 1.0) < eps:
			start += 1

		end = start + 1
		while end < len(series) - 1 and abs(series[end + 1][1] + 1.0) < eps:
			end += 1

		f = int(round(0.5 / (series[end][0] - series[start][0])))
		if f % 5 != 0:
			return ['square-wave', '20']
		return ['square-wave', str(int(round(0.5 / (series[end][0] - series[start][0]))))]
	else:
		start = 0
		while start < len(series) and abs(series[start][1] - 0.0) > eps:
			start += 1
		end = start + 1
		while end < len(series) and abs(series[end][1] - 0.0) > eps:
			end += 1

		return ['sine-wave', str(int(round(0.5 / (series[end][0] - series[start][0]))))]

if __name__ == '__main__':
	n = int(raw_input())
	series = []
	for _ in range(n):
		t, d = map(float, raw_input().strip().split())
		series.append((t, d))
	print '\n'.join(solve(series))