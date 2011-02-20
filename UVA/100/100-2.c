 /* UVA 100 - The 3n+1 problem
   David Felipe Toca
   david.virusfel@gmail.com
   Accepted
   adhoc + simulation + DP 
*/

#include <stdio.h>

#define MAX 1000000

int len[MAX];

int cycle(int n){

	if(n>=MAX){

	int temp=0;

		while(n>=MAX){
		n=(n%2==0?n/2:n*3+1);
		temp++;
		}

	return cycle(n)+temp;

	}	


if(len[n]==0)
{

if(n%2==0)
	len[n]=cycle(n/2)+1;
else
	len[n]=cycle(3*n+1)+1;


}
return len[n];

}



int maxCycle(int i,int j){

int max=0;

int c;

for(c=i;c<=j;c++)
{
int count=cycle(c);
max=(max<count)?count:max;
}

return max;
}

int main(void)
{
	int i,j,max;
	len[1]=1;
	while(scanf("%d %d",&i,&j)!=EOF)
	{
	printf("%d %d ",i,j);

	if(i>j)
	{
	 i^=j;
	 j^=i;
	 i^=j;
	}



	int max	=maxCycle(i,j);	
	printf("%d\n",max);

	}


return 0;
}
