/* UVA 100 - The 3n+1 problem
   David Felipe Toca
   david.virusfel@gmail.com
   Accepted
   adhoc + simulation
*/

#include <iostream>

using namespace std;

int count(int n)
{
int result=1;

while(n!=1)
{
n=(n%2==0)?n/2:n*3+1;
result++;
}
return result;

}


int cycle(int i,int j){

int c,max=0;

for(c=i;c<=j;c++)
{
int a=count(c);
max=(max<a)?a:max;
}

return max;
}


int main(void)
{

int i,j;

while(cin>>i>>j){

cout<<i<<" "<<j<<" ";

if(i>j){

i^=j;
j^=i;
i^=j;

}

int max=cycle(i,j);

cout<<max<<endl;

}

return 0;

}
