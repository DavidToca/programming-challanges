
/* UVA 10055 - Hashmat the Brave Warrior
   David Felipe Toca
   david.virusfel@gmail.com
   Accepted
   adhoc 
*/

#include <stdio.h>


int main(void)
{
long long a,b;

while(scanf("%lld %lld",&a,&b)!=EOF){

if(a>b)
printf("%lld\n",(a-b));
else
printf("%lld\n",(b-a));

}

return 0;
}
