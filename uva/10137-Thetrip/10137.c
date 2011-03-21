/* UVA 10137 - Thetrip
   David Felipe Toca Avila
   david.virusfel@gmail.com
   Accepted
   some math
*/
#include <stdio.h>

int main()
{

while(1)
{
int n;
scanf("%d",&n);

if(!n)break;

int amount[n];

int i;
float avg=0;

for(i=0;i<n;i++){
float money;
scanf("%f",&money);
/*printf("money=%f\n",money);*/
double aux=money*100;
/*printf("money*100=%f\n",aux);*/
amount[i]=(int)(aux+0.5);
/*printf("amount=%d\n",amount[i]);*/
avg+=amount[i];
}
avg/=n;
/*printf("avg=%f\n",avg);*/

int positive=0;
int negative=0;

for(i=0;i<n;i++){
double diff=0;
diff=amount[i]-avg;
/*diff=avg-amount[i];*/
if(diff>=0)
positive+=diff;
else
negative-=diff;

}
/*printf("positive=%d\n",positive);
printf("negative=%d\n",negative);*/

printf("$%.2f\n",(negative>positive?(negative)/100.0:positive/100.0));


}
return 0;
}
