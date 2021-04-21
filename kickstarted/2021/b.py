def solve(arr):
    return 0

t = int(input())

for c in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f"Case #{c}: {solve(arr)}")
    
