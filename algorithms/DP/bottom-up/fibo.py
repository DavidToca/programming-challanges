def fibo(n):
    if n < 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for num in range(2, n + 1):
        dp[num] = dp[num - 1] + dp[num - 2]

    return dp[n]


def fibo_recursive(n):
    if n < 2:
        return n

    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


n = 900
print(fibo(n))
# print(fibo_recursive(n))
