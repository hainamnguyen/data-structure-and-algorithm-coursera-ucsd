#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <cstring>
#include <deque>
#include <stack>
#include <stdio.h>
#include <map>
#include <set>
#include <time.h>
#include <string>
#include <fstream>
#include <queue>
#include <bitset>
#include <cstdlib>
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define pdd pair<double,double>
#define pii pair<ll,ll>
#define PI 3.14159265358979323846
#define MOD 1000000007
#define MOD2 1000000009
#define INF ((ll)1e+18)
#define x1 fldgjdflgjhrthrl
#define x2 fldgjdflgrtyrtyjl
#define y1 fldggfhfghjdflgjl
#define y2 ffgfldgjdflgjl
#define N 200002
#define SUM 23423
#define MAG 1048576
#define OPEN 0
#define CLOSE 1
typedef int ll;
typedef long double ld;
using namespace std;
ll i,j,n,k,l,m,tot, flag,h,r,ans, K,x1,y1,x2,y2,x3,y3,mmx,mmy,x,y,z,ysz;
ll a[200005], used[800500], w[200500];
char b[10005][10005];
vector<ll> g[100500], f, f1, f2;
vector<pii> ff;
bool cmp(ll x, ll y)
{
	return w[x]<w[y];
}
void dfs(ll v)
{
	f.push_back(v);
	used[v] = 1;
	h = g[v].size();
	for (int i = 0; i < h; i++)
		a[i] = i;
	sort(g[v].begin(), g[v].end(), cmp);
	for (int i = 0; i < g[v].size(); i++)
	{
		ll to = g[v][a[i]];
		if (!used[to])
		{
			w[v]--;
			w[to]--;
			dfs(to);
			return;
		}
	}
}
int main() {
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	cin >> n >> m;
	for (i = 0; i < m; i++)
	{
		cin >> x >> y;
		g[x].push_back(y);
		g[y].push_back(x);
		b[x][y] = b[y][x] = 1;
	}
	y = n+5;
	for (i = 1; i <= n; i++)
		{
			ff.push_back(mp((int)g[i].size(), i));
		}
	sort(ff.begin(), ff.end());
	srand(time(0));
	for (j = 0; j < min(n,100); j++)
	{
		for (i = 1; i <= n; i++)
		{
			used[i] = 0;
			w[i] = g[i].size();
		}
		x = ff[j].Y;
		f.clear();
		dfs(x);
        f1.clear();
		for (i = 0; i < f.size(); i++)
			f1.push_back(f[i]);
		reverse(f1.begin(), f1.end());
		f.clear();
		dfs(x);
		for (i = 1; i < f.size(); i++)
			f1.push_back(f[i]);
		if (f1.size() > f2.size())
		{
		   f2.clear();
		   for (i = 0; i < f1.size(); i++)
			   f2.push_back(f1[i]);
		}
	}
	for (i = 1; i <= n; i++)
		used[i] = 0;
	f = f2;
	for (i = 0; i < f.size(); i++)
		used[f[i]] = 1;
	for (int tt = 0; tt < 10; tt++)
	{
		for (i = 1; i <= n; i++)
		{
			if (!used[i])
			{
				for (j = 0; j+1 < f.size(); j++)
					if (b[f[j]][i] && b[f[j+1]][i])
					{
						f.push_back(i);
						ll sz = f.size();
						for (k = sz-1; k >= j+2; k--)
							swap(f[k], f[k-1]);
						used[i] = 1;
						break;
					}
			}
		}
	}
	if(f.size() == n) {
	    cout << "3 2" << endl;
            cout << "1 2 0" << endl;
            cout << "-1 -2 0" << endl;
            cout << "1 -2 0" << endl;
		}
	else {
	    cout << "2 1" << endl;
            cout << "1 0" << endl;
            cout << "-1 0" << endl;
		}
	return 0;
}
