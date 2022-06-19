//
    // Author: Malloumario
//
#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull ;
typedef long long ll ;
const int MOD = 1000000007;
const ll PI = acos(-1.0);
#define INF  0x3f3f3f3f3f3f3f3f
#define re register
#define F(i,a,b) for(ll re i=a;i<b;++i)
#define D(i,a,b) for(ll re i=a;i>=b;--i)
#define fi first
#define se second
#define pb push_back
#define all(v) v.begin(),v.end()
const int dx[4] = { -1,1,0,0 };
const int dy[4] = { 0,0,-1,1 };
ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
ll n,m,x,y,z,a,b,sum,res,ans;
string s1,s2;
map < ll , ll > store ;
set<char> st;
 
/*ll binarySearch(ll *arr, ll l, ll r, ll x)
{
   if (r >= l)
   {
        ll mid = l + (r - l)/2;
 
        if (arr[mid] == x)  
            return mid;
 
       
        if (arr[mid] > x) 
            return binarySearch(arr, l, mid-1, x);
 
        
        return binarySearch(arr, mid+1, r, x);
   }
 
   return -1;
}
*/
/*
ll Pow(ll a, ll p) {
   a%=MOD;
    ll r = 1;
    while (p) {
        if (p % 2) {
            r = r * a % MOD;
        }
 
        a = a * a % MOD;
        p /= 2;
    }
 
    return r;
     //z = (z%MOD + MOD) % MOD;
}*/
 
// CIN >>>>>>>
// COUT <<<<<<<

void solve()
{
   cin >> n;
   sum=n%10;
   n/=10;
   sum+=n%10;
   n/=10;
   sum+=n%10;
   n/=10;
   ans=n%10;
   n/=10;
   ans+=n%10;
   n/=10;
   ans+=n%10;
   if (ans!=sum)
    cout << "NO"<<endl;
    else cout << "YES"<<endl;

}

int main()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    //freopen("zone.in","r",stdin);

    ll T=1;
    cin>>T;
    while(T--){
        // cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}