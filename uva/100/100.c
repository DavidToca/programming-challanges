// uva 100  The 3n+1 Problem
// still TLE :'(

#include <stdio.h>

int count(int n)
{
int result=1;

while(n!=1){

n=(n%2==0?n/2:3*n+1);
result++;

}

return result;

}


int cycle(int a,int b)
{
int result=0;

int i;
for(i=a;i<=b;i++){
int c= count(i);
result=c>result?c:result;
}

return result;

}


int main(void)
{

int i,j;

while(scanf("%d %d",&i,&j))
{

printf("%d %d ",i,j);

if(i>j)
{
i^=j;
j^=i;
i^=j;
}

int result=cycle(i,j);

printf("%d\n",result);
}
return 0;

}
