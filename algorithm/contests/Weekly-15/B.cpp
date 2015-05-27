#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

const int maxn = 300001;

typedef struct node {
	int l, r, mid, sum;
	node() {}
	node(int _l, int _r, int _mid, int _sum) :l(_l), r(_r), mid(_mid), sum(_sum) {}
} node;

node seg[5 * maxn];
int ls[maxn];
int hs[maxn];

void build(int l, int r, int num) {
	int mid = (l + r) / 2;
	seg[num] = node(l, r, mid, 0);
	if (l + 1 != r) {
		build(l, mid, num * 2);
		build(mid, r, num * 2 + 1);
	}
}


void insert(int l, int r, int num) {
	int left, right, mid, sum;
	left = seg[num].l; right = seg[num].r;
	mid = seg[num].mid; sum = seg[num].sum;

	if (l == left && r == right) {
		seg[num] = node(left, right, mid, sum + 1);
		return;
	}
	if (r <= mid) {
		insert(l, r, num * 2);
	} else if (l >= mid) {
		insert(l, r, num * 2 + 1);
	} else {
		insert(l, mid, num * 2);
		insert(mid, r, num * 2 + 1);
	}
}

int query(int idx) {
	int ret = 0;
	int num = 1;
	while (seg[num].l != idx || seg[num].r != idx + 1) {
		ret += seg[num].sum;
		if (idx < seg[num].mid) {
			num = num * 2;
		} else {
			num = num * 2 + 1;
		}
	}
	ret += seg[num].sum;
	return ret;
}

int solve(int ls[], int hs [], int n) {
	build(0, maxn, 1);
	for (int i = 0; i < n; ++i) {
		insert(ls[i], hs[i] + 1, 1);
	}

	for (int i = n; i >= 0; --i) {
		if (query(i) >= i)
			return i;
	}
	return 0;
}

int main() {
	int n, tmp;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &tmp);
		ls[i] = tmp + 1;
		scanf("%d", &tmp);
		hs[i] = tmp + 1;
	}
	printf("%d\n", solve(ls, hs, n));
}