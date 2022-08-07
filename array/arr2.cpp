/*find the len of array and size of array*/
#include<bits/stdc++.h>
using namespace std;
int main(){
  int arr[]={1,2,3,12,3,1,33,3};
  cout<<"size of array is : "<<sizeof(arr)<<endl;
  cout<<"size of array's first element: "<<sizeof(arr[0])<<endl;
  cout<<"len of array is: "<<sizeof(arr)/sizeof(arr[0]);
  return 0 ;
}