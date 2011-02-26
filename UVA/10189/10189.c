/* UVA 10189 - Minesweeper
   David Felipe Toca Avila
   david.virusfel@gmail.com
   Accepted
   adhoc
*/
#include <stdio.h>

#define MAX 103

char matriz[MAX][MAX];


int dx[]={0,1,1,-1,0,-1,-1,1};
int dy[]={1,0,1,0,-1,-1,1,-1};
int calc(int x,int y)
{
int result=0;
int k;
for(k=0;k<8;k++)
result+=(matriz[x+dx[k]][y+dy[k]]=='*'?1:0);

return result;
}

void print(int n, int m){
int i,j;
for(i=1;i<=n;i++){
for(j=1;j<=m;j++){
if(matriz[i][j]!='*')
printf("%d",calc(i,j));
else
printf("%c",'*');
}
printf("\n");

}


}

int main(int argc, char* argv)
{
int n,m;

int k,l;

int cases;
for(cases=1;scanf("%d %d",&n,&m) && n!=0;cases++)
{

for(k=0;k<=n+1;k++)
{

for(l=0;l<=m+1;l++)
{
matriz[k][l]='.';

}

}

if(cases>1){
printf("\n");
}
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
print(n,m);

}
return 0;
}

