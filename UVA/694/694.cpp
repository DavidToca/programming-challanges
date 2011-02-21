/* UVA 694 - The 3n+1 problem
   David Felipe Toca
   david.virusfel@gmail.com
   Accepted
   adhoc + simulation
*/

#include <iostream>

using namespace std;

long long count(long long n,long long max)
{
long long result=1;
//cout<<"count\n";
while(n!=1)
{
n=(n%2==0)?n/2:n*3+1;
//cout<<"while\n";
if(n>max)
break;

result++;
}
return result;

}

int main(void)
{

int i,j;

for(int c=1;true;c++){
//cout<<"unreaded\n";
cin>>i>>j;
//cout<<"readed\n";
if((i==-1 && j==-1))break;

cout<<"Case "<<c<<": A = "<<i<<", limit = "<<j<<", number of terms = ";

long long max=count(i,j);

cout<<max<<endl;

}

return 0;

}
