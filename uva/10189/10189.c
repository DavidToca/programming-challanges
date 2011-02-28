/* UVA 10189 - Minesweeper
   David Felipe Toca Avila
   david.virusfel@gmail.com
   Accepted
   adhoc
*/
#include <stdio.h>
#include <string.h>

#define MAX 102



int dx[]={0,1,1,-1,0,-1,-1,1};
int dy[]={1,0,1,0,-1,-1,1,-1};

int calc(char matriz[][MAX],int x,int y)
{
int result=0;
int k;
for(k=0;k<8;k++)
result+=(matriz[x+dx[k]][y+dy[k]]=='*'?1:0);

return result;
}

void solve(char matriz[][MAX],int n, int m){
int i,j;
for(i=1;i<=n;i++){
	for(j=1;j<=m;j++){
		if(matriz[i][j]!='*')
		printf("%d",calc(matriz,i,j));
		else
		putchar('*');
}

putchar('\n');
}


}

int main(int argc, char* argv)
{
int n,m,k,l,cases;
for(cases=1;scanf("%d %d",&n,&m) && n!=0;cases++)
{

char matriz[MAX][MAX];


memset(matriz,'.',sizeof(matriz));


if(cases>1) putchar('\n');


int i,j;
char c;

getchar();

for(i=1;i<=n;i++){
	for(j=1;j<=m;j++){
		c=getchar();
		matriz[i][j]=c;
	}
getchar();

}

printf("Field #%d:\n",cases);

solve(matriz,n,m);


}
return 0;
}

