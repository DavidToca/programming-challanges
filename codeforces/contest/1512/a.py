cases = int(input())

for case in range(cases):
    n = int(input())

    arr = input().split(' ')

    for index in range(len(arr) - 2):
        if arr[index] == arr[index + 1] and arr[index] == arr[index + 2]:
            continue

        if arr[index] == arr[index + 1]:
            print(index + 3)
            break

        if arr[index] == arr[index + 2]:
            print(index + 2)
            break

        print(index + 1)


# ..∗.
# ....
# ∗...
# ....

# *...
# ....
# ∗...
# ....

# *.*.
# ....
# ....
# ....