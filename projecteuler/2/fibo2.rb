#initial values

fibo1, fibo2 = 1, 2

max = 4_000_000

sum = 2

fibo3 = fibo1 + fibo2

begin

  sum+= fibo3 if fibo3.even?

  fibo1,fibo2 = fibo2 , fibo3

  fibo3 = fibo1 + fibo2

end while(fibo3 <= max)

puts sum






