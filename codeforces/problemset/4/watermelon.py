# https://codeforces.com/problemset/problem/4/A

a = int(input())

if a < 4:
    print("NO")
elif a % 2 == 0:
    print("YES")
else:
    print("NO")