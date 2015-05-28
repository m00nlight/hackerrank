#include <cstdio>
#include <vector>
using namespace std;

const int max_nodes = 200010;
const int log_max_nodes = 20;
int num_nodes, log_num_nodes, root;

vector<int> children[max_nodes];	// children[i] contains the children of node i
int A[max_nodes][log_max_nodes+1];	// A[i][j] is the 2^j-th ancestor of node i, or -1 if that ancestor does not exist
int L[max_nodes];			// L[i] is the distance between node i and the root

// floor of the binary logarithm of n
int lb(unsigned int n) {
	if(n==0)
	return -1;
	int p = 0;
	if (n >= 1<<16) { n >>= 16; p += 16; }
	if (n >= 1<< 8) { n >>=  8; p +=  8; }
	if (n >= 1<< 4) { n >>=  4; p +=  4; }
	if (n >= 1<< 2) { n >>=  2; p +=  2; }
	if (n >= 1<< 1) {           p +=  1; }
	return p;
}

void DFS(int i, int l)
{
	L[i] = l;
	for(int j = 0; j < children[i].size(); j++)
		DFS(children[i][j], l+1);
}

int LCA(int p, int q)
{
	// ensure node p is at least as deep as node q
	if(L[p] < L[q])
	swap(p, q);

	// "binary search" for the ancestor of node p situated on the same level as q
	for(int i = log_num_nodes; i >= 0; i--)
	if(L[p] - (1<<i) >= L[q])
		p = A[p][i];
	
	if(p == q)
	return p;

	// "binary search" for the LCA
	for(int i = log_num_nodes; i >= 0; i--)
	if(A[p][i] != -1 && A[p][i] != A[q][i])
	{
		p = A[p][i];
		q = A[q][i];
	}
	
	return A[p][0];
}

int main(int argc,char* argv[])
{
	// read num_nodes, the total number of nodes
	int N, Q;
	scanf("%d %d", &N, &Q);
	num_nodes = N;
	log_num_nodes = lb(num_nodes);

	for (int i = 1; i < N; ++i) {
		int fa;
		scanf("%d", &fa);
		A[i][0] = fa - 1;
		children[fa - 1].push_back(i);
	}
	
	root = 0;
	A[0][0] = -1;

	for (int j = 1; j <= log_num_nodes; ++j) {
		for (int i = 0; i < num_nodes; ++i) {
			if (A[i][j - 1] != -1)
				A[i][j] = A[A[i][j - 1]][j - 1];
			else
				A[i][j] = -1;
		}
	}

	DFS(root, 0);

	
	for(int i = 0 ;i < Q; ++i) {
		int a, b, lca;
		scanf("%d %d", &a, &b);
		a--; b--;
		lca = LCA(a, b);
		if (lca == a) {
			printf("%d %d\n", L[a] + 1, L[b] - L[a]);
		} else if (lca == b) {
			printf("%d %d\n", L[a] - L[b], L[b] + 1);
		} else {
			printf("%d %d\n", L[a] + 1, L[b] - L[lca]);
		}
	}
	
	return 0;
}