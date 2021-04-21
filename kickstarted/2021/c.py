MAX_SIZE = 10**9

isprime = [True] * MAX_SIZE 
prime = [] 
SPF = [None] * (MAX_SIZE) 

def manipulated_seive(): 
    isprime[0] = False
    isprime[1] = False
    for i in range(2, MAX_SIZE): 
      
        if isprime[i] == True:           
            prime.append(i) 
            SPF[i] = i 

        j = 0
        while (j < len(prime) and
               i * prime[j] < MAX_SIZE and
                   prime[j] <= SPF[i]):
          
            isprime[i * prime[j]] = False
  
            # put smallest prime factor of i*prime[j] 
            SPF[i * prime[j]] = prime[j]
              
            j += 1

manipulated_seive()

choices = []
last_prime = 2
for i in range(3, MAX_SIZE):
    if isprime[i]:
        choices.append(last_prime * i)
        last_prime = i

print(10**18 - choices[-1])

def solve(z):
    solution = 6
    for c in choices:
        if c == z:
            return c
        if c > z:
            return solution
        solution = c
    return solution

t = int(input())

for c in range(1, t+1):
    z = int(input())
    print(f"Case #{c}: {solve(z)}")
