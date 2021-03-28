def reverse_cost(i, j):
    return ((j + 1) - (i + 1)) + 1


def solve(l):
    cost = 0
    for i in range(len(l) - 1):
        min_index = None
        for j in range(i, len(l)):
            if min_index is None:
                min_index = j
            elif l[min_index] > l[j]:
                min_index = j

        cost += reverse_cost(i, min_index)
        l[i : min_index + 1] = l[i : min_index + 1][::-1]

    return cost


t = int(input())

for case in range(1, t + 1):
    n = int(input())
    l = list(map(int, input().split()))

    response = solve(l)
    print(f"Case #{case}: {response}")