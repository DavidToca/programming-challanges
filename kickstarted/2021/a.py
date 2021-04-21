def solve(s):
    s = list(s)
    solution = ['1']
    longest = 1
    last_character = s[0]
    for c in s[1:]:
        if ord(c) <= ord(last_character):
            longest=1
        else:
            longest+=1
        
        solution.append(str(longest))
        last_character = c
    return ' '.join(solution)
    

t = int(input())

for c in range(t):
    n = int(input())
    s = input()
    print(f"Case #{c}:",solve(s))
