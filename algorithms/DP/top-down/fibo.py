UNSET = -1


def fibo_memo(n, lu_table):
    if lu_table[n] != UNSET:
        return lu_table[n]

    lu_table[n] = fibo_memo(n - 1, lu_table) + fibo_memo(n - 2, lu_table)
    return lu_table[n]


def fibo(n):
    if n < 2:
        return n
    lookup_table = [UNSET] * (n + 1)
    lookup_table[0] = 0
    lookup_table[1] = 1

    return fibo_memo(n, lookup_table)


def fibo_recursive(n):
    if n < 2:
        return n

    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


n = 900
print(fibo(n))
# print(fibo_recursive(n))
