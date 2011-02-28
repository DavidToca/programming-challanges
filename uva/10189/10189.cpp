/*UVA 10189 - Minesweeper
	David Felipe Toca Avila
	david.virusfel@gmail.com
	AC
	adhoc
*/


#include <iostream>
#include <string.h>
#include <stdio.h>

#define MAX 102

using namespace std;

int dx[]={1,0,1,-1,0,-1,1,-1};
int dy[]={0,1,1,0,-1,1,-1,-1};

int calc(int matriz[][MAX],int x, int y)
{

int result=0;

for(int i=0;i<8;i++)
result+=matriz[x+dx[i]][y+dy[i]];


return result;
}

int main(void)
{

int N,M;

for(int cases=1;cin>>N && cin>>M && N!=0;cases++)
{

if(cases>1)cout<<endl;

char c;

int matriz[MAX][MAX];

bzero(matriz,MAX*MAX*sizeof(int));
/*memset(matriz,0,sizeof(matriz));*/

for(int I=1;I<=N;I++)
{
for(int J=1;J<=M;J++){

cin>>c;

matriz[I][J]=(c=='*')?1:0;

}

}

cout<<"Field #"<<cases<<":"<<endl;

for(int I=1;I<=N;I++)
{
for(int J=1;J<=M;J++){
if(matriz[I][J]==1)
cout<<"*";
else
cout<<calc(matriz,I,J);
}
cout<<endl;

}


}


return 0;
}
