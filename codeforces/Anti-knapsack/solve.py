def solve(n, k):
    response = [x for x in range(k+1, n+1)]
    options = [x for x in range(1, k)]

    while(options):

        if(len(options) == 1):
            response.append(options[0])
            del options[0]
        elif(options[0] + options[-1] == k):
            del options[0]
            response.append(options[-1])
            del options[-1]
        else:
            response.append(options[-1])
            del options[-1]
    return response


t = int(input())

for i in range(t):
    n,k = list(map(int, input().split()))


    r = solve(n, k)

    print(len(r))
    if r:
        print(' '.join(map(str, r)))
