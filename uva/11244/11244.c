#include <stdio.h>

#define OP 8
#define TRUE 1
#define FALSE 0

typedef int bool;

int dx[]={1,0,1,-1,1,0,-1,-1};
int dy[]={1,1,0,-1,-1,0,1};

int main(void)
{

int r,c;

while(scanf("%d %d",&r,&c) && (r!=0 && c!=0))
{
	printf("case %d %d\n",r,c);
	char mat[r+1][c+1];

	int i,j;

		for(i=1;i<=r;i++)
		{
			for(j=1;j<=c;j++)
			{
			char d;
			scanf("%c",&d);
			mat[i][j]=d;

			}
		}

int res=0;

	for(i=1;i<=r;i++)
	{
		for(j=1;j<=c;j++)
		{

		if(mat[i][j]!='*')
		continue;
		
		int k;
		bool isStar=TRUE;
		for(k=0;k<OP;k++)
		{
		if(mat[i+dx[k]][j+dy[k]]=='*'){
		isStar=FALSE;
		break;
		}
	if(isStar)res++;

		}	

	}

}
printf("%d\n",res);
}


return 0;
}
