#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int board[9][9] = {
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0}
};

bool check[10] = {false};

bool alltrue() {
	for (int i = 1; i < 10; ++i) {
		if (!check[i])
			return false;
	}
	return true;
}

bool check_row(int r) {
	for (int i = 0; i < 10; ++i) check[i] = false;
	check[0] = true;
	for (int j = 0; j < 9; ++j) {
		check[board[r][j]] = true;
	}
	return alltrue();
}

bool check_col(int c) {
	for (int i = 0; i < 10; ++i) check[i] = false;
	check[0] = true;
	for (int i = 0; i < 9; ++i) {
		check[board[i][c]] = true;
	}
	return alltrue();
}

bool check_block(int r, int c) {
	for (int i = 0; i < 10; ++i) check[i] = false;
	check[0] = true;
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j) {
			check[board[r * 3 + i][c * 3 + j]] = true;
		}
	}
	return alltrue();
}

bool valid() {
	for (int i = 0; i < 9; ++i) {
		if (! check_row(i)) {
			//printf("row = %d, valid false", i);
			return false;
		}
	}
	for (int j = 0;j < 9; ++j) {
		if (! check_col(j)) {
			//printf("col = %d, valid false", j);
			return false;
		}
	}
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < 3; ++j) {
			if (!check_block(i, j)) {
				//printf("block r = %d c = %d, valid false", i, j);
				return false;
			}
		}
	}
	return true;
}

void solve() {
	if (valid()) {
		printf("Serendipity\n");
	} else {
		for (int x1 = 0; x1 < 9; ++x1) {
			for (int y1 = 0; y1 < 9; ++y1) {
				for (int x2 = x1; x2 < 9; ++x2) {
					for (int y2 = 0; y2 < 9; ++y2) {
						swap(board[x1][y1], board[x2][y2]);
						if (valid()) {
							if (x1 < x2 || (x1 == x2 && y1 < y2)) {
								printf("(%d,%d) <-> (%d,%d)\n", x1 + 1, y1 + 1, x2 + 1, y2 + 1);	
							}
						}
						swap(board[x1][y1], board[x2][y2]);
					}
				}
			}
		}
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d:\n", t);
		for (int i = 0; i < 9; ++i) {
			for(int j = 0; j < 9; ++j) {
				int tmp;
				scanf("%d", &tmp);
				board[i][j] = tmp;
			}
		}
		//printf("%d\n", valid());
		solve();
	}
}