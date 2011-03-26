#include <string.h>
#include <stdio.h>

/* number or regions*/
#define nREG 5
#define FOR(i,n) for(i=0;i<n;i++)

char* convert[nREG];

void putchars(int n,char c)
{
     int i;
     
     FOR(i,n)
     putchar(c);
     
}

void drawH(int digit,int s, int index){
     putchar(' ');
     putchars(s,convert[index][digit]);
     putchar(' ');
     }
     
void drawV(int digit,int s, int index){

        putchar(convert[index][digit*2]);
        putchars(s,' ');
        putchar(convert[index][(digit*2)+1]); 

}
  
 
 
int main()
{
  
convert[0]="- -- -----";
convert[1]="|| | | |||| |  |||||";
convert[2]="  ----- --";
convert[3]="|| ||  | | ||| ||| |";
convert[4]="- -- -- --";


    char numb[10];
    
    int s;
    int nline;
    

    for(nline=0;scanf("%d %s",&s,&numb) && s;nline++)
    {
    int len=strlen(numb);

    int numbLen=((s+2)*len)+(len-1);    
              
    int i,j,k,l;
    
        FOR(i,nREG)
        {
    
                                   
            FOR(l,((i%2==0)?1:s)){
            if(l!=0)putchar('\n');
                FOR(j,len){
                                if(j!=0) putchar(' ');
                                int digit=numb[j]-'0';
                                if(i%2==0)
                                drawH(digit,s,i);
                                else                                 
                                drawV(digit,s,i);
        
                           }
                           
                           }     
         putchar('\n');             
        }
    
    putchar('\n');
    
    }
    

   return 0; 
}    
