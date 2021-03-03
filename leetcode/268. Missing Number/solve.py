class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        gauss = n*(n+1) // 2
        sum_n = sum(nums)

        return gauss - sum_n
