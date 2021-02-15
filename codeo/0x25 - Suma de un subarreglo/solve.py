n = int(input())

array = list(map(int, input().split()))

cases = int(input())

total = 0

for i in range(n):
    total+=array[i]
    array[i] = total


for _ in range(cases):
    p, q = list(map(int, input().split()))

    if p == 0:
        print(array[q])
    else:
        print(array[q] - array[p-1])
