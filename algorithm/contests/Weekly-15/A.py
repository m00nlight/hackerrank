from __future__ import division

pairs = [(a, b) for a in range(9) for b in range(9)]

def valid(sudoku):
    def valid_row(r):
        nums = set()
        for j in xrange(9):
            nums.add(sudoku[r][j])

        return len(nums) == 9

    def valid_col(c):
        nums = set()
        for i in xrange(9):
            nums.add(sudoku[i][c])
        return len(nums) == 9

    def valid_block(r, c):
        nums = set()
        for i in xrange(3):
            for j in xrange(3):
                nums.add(sudoku[r * 3 + i][c * 3 + j])
        return len(nums) == 9

    for i in xrange(9):
        if not valid_row(i): return False

    for j in xrange(9):
        if not valid_col(j): return False

    for i in xrange(3):
        for j in xrange(3):
            if not valid_block(i, j):
                return False

    return True

def solve(sudoku):
    if valid(sudoku):
        print 'Serendipity'
    else:
        for (x, y) in [(a, b) for a in range(9) for b in range(9)]:
            for (p, q) in [(a, b) for a in range(x, 9) for b in range(9)]:
                sudoku[x][y], sudoku[p][q] = sudoku[p][q], sudoku[x][y]
                if valid(sudoku) and (x, y) <= (p, q):
                    print '(%d,%d) <-> (%d,%d)' % (x+1, y+1, p+1, q+1)
                sudoku[x][y], sudoku[p][q] = sudoku[p][q], sudoku[x][y]

if __name__ == '__main__':
    t = int(raw_input())
    for i in range(1, t+1):
        sudoku = []
        print "Case #%d:" % i
        for r in range(9):
            sudoku.append(map(int, raw_input().strip().split()))

        solve(sudoku)
