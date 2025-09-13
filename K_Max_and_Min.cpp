#include<bits/stdc++.h>
using namespace std;
int main(){
   int a,b,c;
   cin>>a>>b>>c;

    int minm = a;

    if( minm > b)
    {
        minm = b;
    }
    if(minm > c)
    {
        minm = c;
    }

    int mxm = a;
    if(mxm<b)
    {
        mxm = b;
    }
    
    if(mxm<c)
    {
        mxm=c;
    }


    cout << minm << " " << mxm;
   
  
}