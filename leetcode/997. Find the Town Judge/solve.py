class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        trusted_by = defaultdict(lambda: 0)
        trusted_for = defaultdict(lambda: 0)

        for edge in trust:
            start, end = edge
            trusted_by[end] += 1
            trusted_for[start] += 1

        for i in range(1, N + 1):

            if trusted_by[i] == N - 1 and trusted_for[i] == 0:
                return i
        return -1
