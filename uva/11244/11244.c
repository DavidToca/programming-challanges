#include <stdio.h>
#include <string.h>

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
m[i][j]=getchar();
}
getchar();
}

int res=0;
for(i=1;i<=r;i++){
for(j=1;j<=c;j++){
	if(m[i][j]!='*')continue;
	          if(m[i][j-1]=='*') continue;
                  if(m[i-1][j-1]=='*') continue;
                  if(m[i-1][j]=='*') continue;
                  if(m[i-1][j+1]=='*') continue;
                  if(m[i][j+1]=='*') continue;
                  if(m[i+1][j+1]=='*') continue;
                  if(m[i+1][j]=='*') continue;
                  if(m[i+1][j-1]=='*') continue;

	res++;
	
}

}

printf("%d\n",res);

}

return 0;
}
