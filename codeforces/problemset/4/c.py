t = int(input())

database = {}

def solve(s):
    if s not in database:
        database[s] = 0
        return "OK"
    database[s] += 1
    return f"{s}{database[s]}"


for _ in range(t):
    s = input()
    print(solve(s))
