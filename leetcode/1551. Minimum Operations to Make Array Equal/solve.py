class Solution:
    def minOperations(self, n: int) -> int:
        arr = [i * 2 + 1 for i in range(n)]

        average = round(sum(arr) / len(arr))

        operations = 0

        for numb in arr:
            operations += abs(numb - average)

        return operations // 2