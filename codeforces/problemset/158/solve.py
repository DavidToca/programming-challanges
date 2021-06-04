n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def solve():
    response = 0
    clasified = a[k - 1]
    for n in a:
        if n != 0 and n >= clasified:
            response += 1
    return response


print(solve())