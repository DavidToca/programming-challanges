s = input()


def solve(s):
    has_repeated = True
    while has_repeated:
        has_repeated = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2 :]
                has_repeated = True
                break
    return s


print(solve(s))