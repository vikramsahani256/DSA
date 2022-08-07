#include<bits/stdc++.h>
using namespace std;
int main(){
  int n=0,i,j;
  cout<<"n value"<<endl;
  cin>>n;
  
  for(i = 0; i < n; i++)
  {
    for(j=0;j<n;j++){
      if(i==j || n=i+j+1){
        cout<<"*";
      }else{
        cout<<" ";
      }
    }
    cout<<endl;
  }
  
  return 0 ;
}