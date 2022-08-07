/*find the sum of the array having len=5*/
#include<bits/stdc++.h>
using namespace std;
int main(){
int arr[] = {1,24,2,5,63};
int sum = 0;
for(int i=0;i<5;i++){
sum = sum+arr[i];
}
cout<<"sum "<<sum<<endl;
  return 0;
}