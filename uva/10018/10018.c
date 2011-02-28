#include <stdio.h>

unsigned int reverse(unsigned int a){

unsigned int b=0;
int i;
while(a)
{
b=b*10+a%10;
a/=10;
}

return b;
}

int main()
{

unsigned int a;

int count;
scanf("%d",&count);

while(count--)
{

unsigned int a;
scanf("%u",&a);

unsigned int b;
int i;

for(i=0;(b=reverse(a))!=a;i++){
a+=b;

}

printf("%d %u\n",i,a);


}

return 0;
}
