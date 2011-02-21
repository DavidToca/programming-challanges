#include <stdio.h>
#define N 1000001

unsigned int len[N];

void getlen_pre(unsigned int p)
{
    unsigned int q = p, c = 0;
    
    while(q >= p)
    {
        q = (q & 1)? (q * 3 + 1) : (q / 2);
        c++;
    }
    
    len[p] = len[q] + c;
}

unsigned int getlen(unsigned int p)
{
    unsigned int q = p, c = 0;
    
    while(q >= N)
    {
        q = (q & 1)? (q * 3 + 1) : (q / 2);
        c++;
    }
    
    return len[q] + c;
}

int main()
{
    unsigned int a, b, i, max, ptr, tmp;
    
    len[1] = 0;
    
    for(i = 2; i < N; i++)
        getlen_pre(i);
    
    len[1] = 3;
    
    while(1)
    {
        scanf("%u%u", &a, &b);
        
        if(a == 0 && b == 0)
            break;
        
        max = 0;
        
        if(a < b)
        {
            for(i = a; i <= b; i++)
            {
                tmp = getlen(i);
                
                if(max < tmp)
                    max = tmp, ptr = i;
            }
            
            printf("Between %u and %u, %u generates the longest sequence of %u values.\n", a, b, ptr, max);
        }
        else
        {
            for(i = b; i <= a; i++)
            {
                tmp = getlen(i);
                
                if(max < tmp)
                    max = tmp, ptr = i;
            }
            
            printf("Between %u and %u, %u generates the longest sequence of %u values.\n", b, a, ptr, max);
        }
    }
    
    return 0;
}
