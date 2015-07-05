#include <iostream>
#include <cstdio>
#include <cstring>
#include <string.h>
#include <cmath>
#include <iomanip>
#include <algorithm>
using namespace std;

const double eps = 1e-4;
const int maxn = 220;
const int mod = 1000000007;

double a[maxn][maxn], x[maxn];
int equ, var;

int Gauss() {
    int i, j, k, col, max_r;
    for (k = 0, col = 0; k < equ && col < var; ++k, ++col) {
        max_r = k;
        for (i = k + 1; i < equ; ++i) {
            if (fabs(a[i][col] > fabs(a[max_r][col])))
                max_r = i;
        }
        if (fabs(a[max_r][col]) < eps)
            return var - k;
        if (k != max_r) {
            for (j = col; j < var; ++j) {
                swap(a[k][j], a[max_r][j]);
            }
            swap(x[k], x[max_r]);
        }
        x[k] /= a[k][col];
        for (j = col + 1; j < var; ++j) {
            a[k][j] /= a[k][col];
        }
        for (i = 0; i < equ; ++i) {
            if (i != k) {
                x[i] -= x[k] * a[i][k];
                for (j = col + 1; j < var; ++j) 
                    a[i][j] -= a[k][j] * a[i][col];
                a[i][col] = 0;
            }
        }
    }
    return 0;
}

void pri() {
    for (int i = 0; i < equ; ++i) {
        for (int j = 0; j < var; ++j) {
            printf("%lf ", a[i][j]);
        }
        printf(" = %lf\n", x[i]);
    }
}

int main() {
    int n;
    cin >> n;
    equ = var = n;
    for (int i = 0; i < n; ++i) {
        int k, temp;
        a[i][i] = -1.0;
        x[i] = 0;
        cin >> k;
        for (int j = 0; j < k; ++j) {
            cin >> temp;
            a[i][temp -1] = 1.0;
        }
    }

    //pri();
    int freedom = Gauss();
    //pri();
    long long ans = 1;
    for (int i = 0; i < freedom; ++i) {
        ans = ans * 99991 % mod;
    }
    cout << ans << endl;
}
