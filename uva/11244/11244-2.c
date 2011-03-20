#include <stdio.h>
#include <string.h>
#define OP 8


int dx[]={1,0,1,0,-1,1,-1,-1};
int dy[]={0,1,1,-1,0,-1,1,-1};

int main()
{

while(1){

int r,c;

scanf("%d %d",&r,&c);

if(r==0 && c==0)
break;

getchar();

char m[r+2][c+2];

int i,j,k;

memset(m,46,sizeof(m));

for(i=1;i<=r;i++){
for(j=1;j<=c;j++){
/*cin>>m[i][j];*/
m[i][j]=getchar();
}
getchar();
}

int res=0;
for(i=1;i<=r;i++){
for(j=1;j<=c;j++){
	if(m[i][j]!='*')continue;
	int isStar=1;
	for(k=0;k<OP;k++)
		if(m[i+dx[k]][j+dy[k]]=='*'){
		isStar=0;
		break;
		}
	if(isStar)
	res++;
	
}

}

printf("%d\n",res);

}

return 0;
}
