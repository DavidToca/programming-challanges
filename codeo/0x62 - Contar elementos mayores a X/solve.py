
n = int(input())

array = list(map(int, input().split()))

cases = int(input())

for case in range(cases):
    comp = int(input())
    response = 0
    for numb in array:
        if(numb > comp):
            response+=1
    print(response)