#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

typedef long long ll;
const int maxn = 200100;
const ll MOD = 1000000007;

#define lson(x) ((x)<<1)
#define rson(x) (((x)<<1)|1)
int lc[maxn * 10], rc[maxn * 10], v[maxn * 10];
ll nd[maxn * 10], ad[maxn * 10], s[maxn * 10];

void pushup(int u);
void pushdown (int u);

inline int length(int u) {
    return rc[u] - lc[u] + 1;
}

inline void change (int u, ll a) {
    v[u] = 1;
    ad[u] = 0;
    nd[u] = a;
    s[u] = a * length(u);
    s[u] %= MOD; nd[u] %= MOD;
}

inline void maintain (int u, ll a, ll d) {
    if (v[u] && lc[u] != rc[u]) {
        pushdown(u);
        pushup(u);
    }

    v[u] = 0;
    nd[u] += a;
    ad[u] += d;
    ll n = length(u);
    s[u] += a * n + (((n-1) * n) / 2) * d;
    nd[u] %= MOD; ad[u] %= MOD;
    s[u] %= MOD;
}

inline void pushup (int u) {
    s[u] = s[lson(u)] + s[rson(u)];
    s[u] %= MOD;
}

inline void pushdown (int u) {
    if (v[u]) {
        change(lson(u), nd[u]);
        change(rson(u), nd[u]);
        v[u] = nd[u] = 0;
    } else if (nd[u] || ad[u]) {
        maintain(lson(u), nd[u], ad[u]);
        maintain(rson(u), nd[u] + length(lson(u)) * ad[u], ad[u]);
        nd[u] = ad[u] = 0;
    }
}

void build (int u, int l, int r) {
    lc[u] = l;
    rc[u] = r;
    nd[u] = ad[u] = s[u] = 0;

    if (l == r)
        return;
    int mid = (l + r) / 2;
    build(lson(u), l, mid);
    build(rson(u), mid + 1, r);
    pushup(u);
}

void modify(int u, int l, int r, ll a, ll d) {
    if (l <= lc[u] && rc[u] <= r) {
        maintain(u, a + d * (lc[u] - l), d);
        return;
    }

    pushdown(u);
    int mid = (lc[u] + rc[u]) / 2;
    if (l <= mid)
        modify(lson(u), l, r, a, d);
    if (r > mid)
        modify(rson(u), l, r, a, d);
    pushup(u);
}


ll query (int u, int l, int r) {
    if (l <= lc[u] && rc[u] <= r)
        return s[u];

    pushdown(u);
    ll ret = 0;
    int mid = (lc[u] + rc[u]) / 2;
    if (l <= mid)
        ret += query(lson(u), l, r);
    if (r > mid) 
        ret += query(rson(u), l, r);
    pushdown(u);
    return ret;
}

ll N, M, Q;

int diag_num(int r, int c) {
    return c + (N - r);
}

int main () {
    string op;
    ll a, b, c, d, e, l, r, m;
    cin >> N >> M >> Q;
    build(1, 1, N + M);

    for (int i = 0; i < Q; ++i) {
	cin >> op;
	if (op.substr(0, 2).compare("Qc") == 0) {
	    cin >> a >> b;
	    l = diag_num(1, a) - N + 1;
	    r = diag_num(1, a);
	    modify(1, l, r, N * b, -b);
	} else if (op.substr(0, 2).compare("Qr") == 0) {
	    cin >> a >> b;
	    l = diag_num(a, 1);
	    r = l + M - 1;
	    modify(1, l, r, b, b);
	} else if (op.substr(0, 2).compare("Qs") == 0) {
	    ll x1, y1, x2, y2;
	    ll down_left, up_left, down_right, up_right;
	    cin >> x1 >> y1 >> x2 >> y2 >> d;
	    down_left = diag_num(x2, y1);
	    up_left = diag_num(x1, y1);
 	    down_right = diag_num(x2, y2);
	    up_right = diag_num(x1, y2);
	    
	    if (up_left - down_left < down_right - down_left) {
		modify(1, down_left, up_left, d, d);
		modify(1, up_left + 1, down_right, 
		       (up_left - down_left + 1) * d, 0);
		modify(1, down_right + 1, up_right, 
		       (up_left - down_left) * d, -d);
	    } else if (down_right - down_left < up_left - down_left) {
		modify(1, down_left, down_right, d, d);
		modify(1, down_right + 1, up_left,
		       (down_right - down_left + 1) * d, 0);
		modify(1, up_left + 1, up_right,
		       (down_right - down_left) * d, -d);
	    } else { // square case
		modify(1, down_left, down_right, d, d);
		modify(1, down_right + 1, up_right,
		       (down_right - down_left) * d, -d);
	    }
	} else {
	    cin >> a >> b;
	    cout << ((query(1, 1, b) - query(1, 1, a - 1)) % MOD + MOD) % MOD
		 << endl;
	}
    }
    return 0;
}
