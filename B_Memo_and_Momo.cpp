#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,k;
    cin>>a>>b>>k;
    if(k == 0) {
        cout << "No One";
        return 0;
    }
    if(a%k==0 && b%k!=0) cout<<"Memo";
    if(b%k==0 && a%k!=0) cout<<"Momo";
    if(a%k==0 && b%k==0) cout<<"Both";
    if(a%k!=0 && b%k!=0) cout<<"No One";
}

