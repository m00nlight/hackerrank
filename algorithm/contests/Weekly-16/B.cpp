#include "cstdio"
#include "algorithm"
using namespace std;

const int maxn = 105;
typedef long long ll;

const int mod = 1000000007;
ll four[maxn], five[maxn], six[maxn];
pair<ll, ll> dp[maxn][maxn][maxn][3];

void preprocessing() {
    ll base = 4;
    for (int i = 1; i <= 100; ++i) {
	four[i] = (four[i - 1] + base) % mod;
	base = base * 10 % mod;
    }

    base = 5;
    for (int i = 1; i <= 100; ++i) {
	five[i] = (five[i - 1] + base) % mod;
	base = base * 10 % mod;
    }

    base = 6;
    for (int i = 1; i <= 100; ++i) {
	six[i] = (six[i - 1] + base) % mod;
	base = base * 10 % mod;
    }
  
    for (int i = 0; i < maxn; ++i) {
	for (int j = 0; j < maxn; ++j) {
	    for (int k = 0; k < maxn; ++k) {
		for (int p = 0; p < 3; ++p) {
		    dp[i][j][k][p] = make_pair(-1, -1);
		}
	    }
	}
    }
}

pair<ll, ll> solve(int x, int y, int z, int l) {
    if (dp[x][y][z][l].first != -1) {
	return dp[x][y][z][l];
    }
    if (x == 0 && y == 0 && z == 0) {
	return dp[0][0][0][l] = make_pair(1, 0);
    } else {
	if (l == 0) {
	    if (x > 0 && y == 0 && z == 0) {
		return (dp[x][y][z][l] = make_pair(1, four[x]));
	    } else if (x > 0) {
		pair<ll, ll> r1 = solve(x - 1, y, z, 0);
		pair<ll, ll> r2 = solve(x - 1, y, z, 1);
		pair<ll, ll> r3 = solve(x - 1, y, z, 2);
		ll nn = (r1.first + r2.first + r3.first) % mod;
		ll aa = (r1.second + r2.second + r3.second) % mod;
		return dp[x][y][z][l] = make_pair(nn,(aa * 10 + 4 * nn) % mod);
	    } else {
		return make_pair(0, 0);
	    }
	} else if (l == 1) {
	    if (y > 0 && x == 0 && z == 0) {
		return dp[x][y][z][l] = make_pair(1, five[y]);
	    } else if (y > 0) {
		pair<ll, ll> r1 = solve(x, y - 1, z, 0);
		pair<ll, ll> r2 = solve(x, y - 1, z, 1);
		pair<ll, ll> r3 = solve(x, y - 1, z, 2);
		ll nn = (r1.first + r2.first + r3.first) % mod;
		ll aa = (r1.second + r2.second + r3.second) % mod;
		return dp[x][y][z][l] = make_pair(nn,(aa * 10 + 5 * nn) % mod);
	    } else {
		return make_pair(0, 0);
	    }
	} else {
	    if (z > 0 && x == 0 && y == 0) {
		return dp[x][y][z][l] = make_pair(1, six[z]);
	    } else if (z > 0) {
		pair<ll, ll> r1 = solve(x, y, z - 1, 0);
		pair<ll, ll> r2 = solve(x, y, z - 1, 1);
		pair<ll, ll> r3 = solve(x, y, z - 1, 2);
		ll nn = (r1.first + r2.first + r3.first) % mod;
		ll aa = (r1.second + r2.second + r3.second) % mod;
		return dp[x][y][z][l] = make_pair(nn,(aa * 10 + 6 * nn) % mod);
	    } else {
		return make_pair(0, 0);
	    }
	}
    }
}


int main() {
    int x, y, z;

    preprocessing();
    scanf("%d %d %d", &x, &y, &z);
  
    ll ans = 0;
    for (int i = 0; i <= x; ++i) {
	for (int j = 0; j <= y; ++j) {
	    for (int k = 0; k <= z; ++k) {
		for (int ld = 0; ld < 3; ++ld) {
		    pair<ll, ll> tmp = solve(i, j, k, ld);
		    ans = (ans + tmp.second) % mod;
		}
	    }
	}
    }
    printf("%lld\n", ans);
}
